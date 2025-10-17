# 📚 PDF RAG Question Answering System

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/🦜_LangChain-2C3E50?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6584?style=for-the-badge)
![AI](https://img.shields.io/badge/Generative_AI-00D9FF?style=for-the-badge&logo=openai&logoColor=white)

### *Intelligent PDF Analysis powered by RAG (Retrieval-Augmented Generation)*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Architecture](#-architecture) • [Contact](#-contact)

</div>

---

## 🌟 Overview

Transform your PDF documents into an intelligent knowledge base! This project leverages cutting-edge **Retrieval-Augmented Generation (RAG)** technology to extract, store, and query information from PDF files with remarkable accuracy.

```
📄 Upload PDF → 🔍 Extract Metadata → 💾 Store in ChromaDB → 🤖 AI-Powered Q&A → 💡 Get Answers
```

---

## ✨ Features

🎯 **Smart PDF Processing** - Automatically extract and process content from PDF documents

🗄️ **Vector Database Storage** - Efficient metadata storage using ChromaDB for lightning-fast retrieval

🧠 **RAG Technology** - Combines retrieval and generation for accurate, context-aware answers

💬 **Natural Language Q&A** - Ask questions in plain English and get precise answers from your documents

🔗 **LangChain Integration** - Built with LangChain and LangGraph for robust AI workflows

⚡ **Fast & Efficient** - Optimized retrieval system for quick response times

---

## 🏗️ Architecture

```mermaid
graph LR
    A[📄 PDF Upload] --> B[🔄 Content Extraction]
    B --> C[✂️ Text Chunking]
    C --> D[🧮 Embedding Generation]
    D --> E[💾 ChromaDB Storage]
    E --> F[❓ User Question]
    F --> G[🔍 Similarity Search]
    G --> H[🤖 LLM Processing]
    H --> I[💡 Answer Generation]
    
    style A fill:#4CAF50
    style E fill:#FF6584
    style H fill:#00D9FF
    style I fill:#FFD700
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/pdf-rag-qa-system.git
cd pdf-rag-qa-system
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
# Create a .env file with your API keys
OPENAI_API_KEY=your_openai_api_key_here
# Add other required API keys
```

---

## 💻 Usage

### Basic Usage

```python
from pdf_rag_system import PDFQASystem

# Initialize the system
qa_system = PDFQASystem()

# Upload and process PDF
qa_system.upload_pdf("path/to/your/document.pdf")

# Ask questions
response = qa_system.ask("What is the main topic discussed in the document?")
print(response)
```

### Command Line Interface

```bash
# Process a PDF file
python main.py --upload document.pdf

# Ask a question
python main.py --query "What are the key findings?"

# Interactive mode
python main.py --interactive
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Core programming language |
| **LangChain** | LLM orchestration framework |
| **LangGraph** | Workflow management |
| **ChromaDB** | Vector database for embeddings |
| **OpenAI/HuggingFace** | Language models |
| **PyPDF2/PDFPlumber** | PDF processing |

---

## 📊 How It Works

### 1️⃣ **PDF Upload & Processing**
The system accepts PDF files and extracts text content while preserving document structure and metadata.

### 2️⃣ **Chunking & Embedding**
Text is intelligently split into manageable chunks and converted into vector embeddings for efficient storage and retrieval.

### 3️⃣ **ChromaDB Storage**
Embeddings and metadata are stored in ChromaDB, a high-performance vector database optimized for similarity search.

### 4️⃣ **Retrieval-Augmented Generation**
When you ask a question:
- The system searches for relevant chunks using semantic similarity
- Retrieved context is passed to the LLM
- The AI generates an accurate, context-aware answer

---

## 🎯 Use Cases

- 📚 Research paper analysis
- 📋 Legal document review
- 📖 Educational content Q&A
- 🏢 Corporate knowledge management
- 📊 Report summarization
- 🔍 Technical documentation search

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Sitheshwar**

- 💼 Data Science Associate
- 🔧 Proficient in LangChain & LangGraph
- 💡 Ask me about GenAI
- 📧 Email: [sitheshwarsp@gmail.com](mailto:sitheshwarsp@gmail.com)

---

<div align="center">

### ⭐ Star this repo if you find it helpful!

**Made with ❤️ and AI**

</div>
