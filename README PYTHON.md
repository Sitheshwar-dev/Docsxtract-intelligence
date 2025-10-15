# 📘 AI-Powered PDF Q&A using ChromaDB and LLM

This project enables you to **upload any PDF**, automatically **extract and convert its content into metadata**, store it in a **vector database (ChromaDB)**, and then use **AI (LLM)** to answer any question based on the uploaded document.  

It’s an example of a **Retrieval-Augmented Generation (RAG)** system — where large language models are combined with document retrieval for more accurate and context-aware answers.

---

## 🚀 Features

- 📄 **PDF Upload & Processing** – Extracts text and metadata from any uploaded PDF.  
- 🧩 **Vector Embeddings** – Converts text into embeddings for semantic search.  
- 🧠 **ChromaDB Integration** – Stores and retrieves relevant document chunks efficiently.  
- 💬 **AI-Powered Q&A** – Answers user questions based on the PDF’s content using LLMs.  
- ⚡ **Fast & Scalable** – Designed for efficient retrieval even with large documents.

---

## 🏗️ Tech Stack

| Component | Technology |
|------------|-------------|
| Programming Language | Python |
| LLM | Amazon Bedrock (or OpenAI / local LLMs) |
| Vector Store | ChromaDB |
| Frameworks | LangChain / FastAPI (if used) |
| Embeddings | Bedrock Embeddings or Sentence Transformers |
| File Handling | PyPDF2 / pdfplumber |

---

## 🧭 How It Works

1. **Upload PDF**
   - You upload your document.
   - The system reads the PDF and extracts its content.

2. **Create Metadata & Store in ChromaDB**
   - Each document chunk is converted into an embedding (vector).
   - These embeddings + metadata are stored in **ChromaDB**.

3. **Ask a Question**
   - When a user asks a question, the system:
     - Converts the query into an embedding.
     - Finds the **most similar vectors** (relevant parts of the PDF).
     - Sends those to the **LLM** as context.

4. **Generate the Answer**
   - The LLM reads the retrieved metadata and generates a context-aware, accurate answer.

---

## 🧪 Example Workflow

```python
# Step 1: Load and process PDF
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import BedrockEmbeddings
from langchain.vectorstores import Chroma

loader = PyPDFLoader("example.pdf")
documents = loader.load()

# Step 2: Create embeddings and store in Chroma
embeddings = BedrockEmbeddings()
vectorstore = Chroma.from_documents(documents, embeddings)

# Step 3: Ask a question
query = "What are the key findings in this report?"
results = vectorstore.similarity_search(query, k=3)

# Step 4: Use LLM to answer
from langchain.llms import Bedrock
llm = Bedrock()
answer = llm(f"Answer this based on the context: {results}\nQuestion: {query}")
print(answer)
