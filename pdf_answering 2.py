from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_aws import BedrockLLM
from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
import os
import json  
from dotenv import load_dotenv
import tempfile

load_dotenv()

# Initialize FastAPI app
app = FastAPI()

def read_config():
    try:
        config_path = os.getenv("CONFIG_PATH", "D:/GenAI/AWS bedrock/config.json")
        with open(config_path, "r") as file:
            return json.load(file)
    except Exception as e:
        raise Exception(f"Error reading config file: {str(e)}")

config = read_config()

# --- LLM ---
llm = BedrockLLM(
    model_id=config["llm_model_id"],
    model_kwargs={"temperature": config["temperature"]}
)
# Initialize Chroma vectorstore
persist_directory = "D:/GenAI/chroma_db"  # Path to store persistent Chroma data
embeddings = HuggingFaceEmbeddings(model_name=config["embedding_model"])
vectorstore = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

# Helper functions
def load_pdf_content(file_path: str) -> list:
    """Load content from a PDF file."""
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    return text_splitter.split_documents(documents)

def store_embeddings(documents: list):
    """Store documents as embeddings in ChromaDB."""
    vectorstore.add_documents(documents)

def retrieve_relevant_data(question: str) -> list:
    """Retrieve relevant data from Chroma vectorstore."""
    retriever = vectorstore.as_retriever()
    results = retriever.get_relevant_documents(question)
    return [doc.page_content for doc in results]

def generate_answer(retrieved_data: list, question: str) -> str:
    """Generate an answer using the LLM."""
    context = "\n".join(retrieved_data)
    messages = [{"role": "user", "content": f"{context}\n\nQuestion: {question}"}]
    llm = BedrockLLM(model="meta.llama3-70b-instruct-v1:0")
    response = llm.invoke(messages)
    return response.content if hasattr(response, "content") else str(response)

# API Endpoints
@app.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    """Upload a PDF file and store its content in ChromaDB."""
    try:
        # Save the uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(await file.read())
            temp_file_path = temp_file.name

        # Extract content and store embeddings
        documents = load_pdf_content(temp_file_path)
        store_embeddings(documents)
        return {"message": "PDF content processed and stored successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Clean up temporary file
        os.remove(temp_file_path)

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask/")
async def ask_question(request: QuestionRequest):
    """Ask a question based on the uploaded PDF."""
    try:
        # Retrieve relevant data and generate an answer
        relevant_data = retrieve_relevant_data(request.question)
        if not relevant_data:
            raise HTTPException(status_code=404, detail="No relevant data found.")
        answer = generate_answer(relevant_data, request.question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
