<!-- Animated Header -->
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=26&pause=1000&color=00A8FF&center=true&vCenter=true&width=700&lines=👋+Hi+I'm+Sitheshwar;🚀+Generative+AI+Developer;💡+LangChain+%7C+LangGraph+%7C+LLM+Integration;🤖+Building+Smart+AI+Workflows!" alt="Typing SVG" />
</p>

---

# 🧠 Docsxtract-Intelligence  
### *Upload • Extract • Ask • Answer — Powered by Generative AI*

<p align="center">
  <svg width="300" height="300" viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg">
    <!-- Background -->
    <rect width="300" height="300" fill="#0d1117" rx="15"/>
    
    <!-- Laptop -->
    <rect x="60" y="200" width="180" height="25" rx="5" fill="#2f3640"/>
    <rect x="75" y="140" width="150" height="70" rx="8" fill="#1e272e" stroke="#00a8ff" stroke-width="2"/>
    
    <!-- Screen Glow -->
    <rect x="80" y="145" width="140" height="60" rx="6" fill="#00a8ff">
      <animate attributeName="fill" values="#00a8ff;#0097e6;#00a8ff" dur="2s" repeatCount="indefinite"/>
    </rect>
    
    <!-- Head -->
    <circle cx="150" cy="100" r="25" fill="#718093" />
    <circle cx="150" cy="100" r="22" fill="#f5f6fa" />

    <!-- Body -->
    <rect x="130" y="125" width="40" height="45" rx="10" fill="#718093" />

    <!-- Typing Hands -->
    <circle cx="130" cy="185" r="8" fill="#f5f6fa">
      <animate attributeName="cy" values="185;190;185" dur="0.4s" repeatCount="indefinite"/>
    </circle>
    <circle cx="170" cy="185" r="8" fill="#f5f6fa">
      <animate attributeName="cy" values="185;190;185" dur="0.4s" begin="0.2s" repeatCount="indefinite"/>
    </circle>

    <!-- Floating Code Lines -->
    <rect x="90" y="155" width="70" height="5" fill="#dcdde1">
      <animate attributeName="width" values="70;100;70" dur="2s" repeatCount="indefinite" />
    </rect>
    <rect x="90" y="165" width="50" height="5" fill="#dcdde1">
      <animate attributeName="width" values="50;90;50" dur="2s" begin="1s" repeatCount="indefinite" />
    </rect>
    <rect x="90" y="175" width="90" height="5" fill="#dcdde1">
      <animate attributeName="width" values="90;110;90" dur="2s" begin="0.5s" repeatCount="indefinite" />
    </rect>

    <!-- Text -->
    <text x="150" y="270" font-size="16" fill="#00a8ff" text-anchor="middle" font-family="Consolas, monospace">
      Coding in Progress...
      <animate attributeName="fill" values="#00a8ff;#82ccdd;#00a8ff" dur="2s" repeatCount="indefinite"/>
    </text>
  </svg>
</p>

> 🧾 Upload a PDF or DOCX — our AI extracts metadata, stores it in **ChromaDB**, finds vector similarities, and returns precise answers.

---

## ⚙️ Tech Stack
| Language | Framework | Database | Vector Store |
|-----------|------------|-----------|---------------|
| 🐍 Python | LangChain | FastAPI | 🧠 ChromaDB |

---

## 🚀 How It Works
1. **Upload Document** → PDF/DOCX parsed  
2. **Metadata Extraction** → Key info stored  
3. **Vector Embeddings** → Using Bedrock LLM  
4. **Question Answering** → Query AI for relevant context  

---

## 💻 Example Usage
```bash
# Upload a PDF
curl -X POST -F "file=@document.pdf" http://localhost:8000/upload

# Ask a question
curl -X POST -H "Content-Type: application/json" \
-d '{"question": "Summarize the contract terms"}' \
http://localhost:8000/query
