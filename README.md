<p align="center">
  <svg width="300" height="300" viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg">
    <!-- Background -->
    <rect width="300" height="300" fill="#0d1117" rx="15"/>

    <!-- Laptop base -->
    <rect x="60" y="200" width="180" height="25" rx="5" fill="#2f3640"/>
    <rect x="75" y="140" width="150" height="70" rx="8" fill="#1e272e" stroke="#00a8ff" stroke-width="2"/>

    <!-- Laptop screen glow -->
    <rect x="80" y="145" width="140" height="60" rx="6" fill="#00a8ff">
      <animate attributeName="fill" values="#00a8ff;#0097e6;#00a8ff" dur="2s" repeatCount="indefinite" />
    </rect>

    <!-- Head -->
    <circle cx="150" cy="100" r="25" fill="#718093" />
    <circle cx="150" cy="100" r="22" fill="#f5f6fa" />

    <!-- Body -->
    <rect x="130" y="125" width="40" height="45" rx="10" fill="#718093" />

    <!-- Typing hands -->
    <circle cx="130" cy="185" r="8" fill="#f5f6fa">
      <animate attributeName="cy" values="185;190;185" dur="0.4s" repeatCount="indefinite"/>
    </circle>
    <circle cx="170" cy="185" r="8" fill="#f5f6fa">
      <animate attributeName="cy" values="185;190;185" dur="0.4s" begin="0.2s" repeatCount="indefinite"/>
    </circle>

    <!-- Floating code lines on the screen -->
    <rect x="90" y="155" width="70" height="5" fill="#dcdde1">
      <animate attributeName="width" values="70;100;70" dur="2s" repeatCount="indefinite" />
    </rect>
    <rect x="90" y="165" width="50" height="5" fill="#dcdde1">
      <animate attributeName="width" values="50;90;50" dur="2s" begin="1s" repeatCount="indefinite" />
    </rect>
    <rect x="90" y="175" width="90" height="5" fill="#dcdde1">
      <animate attributeName="width" values="90;110;90" dur="2s" begin="0.5s" repeatCount="indefinite" />
    </rect>

    <!-- Title Text -->
    <text x="150" y="270" font-size="16" fill="#00a8ff" text-anchor="middle" font-family="Consolas, monospace">
      Coding in Progress...
      <animate attributeName="fill" values="#00a8ff;#82ccdd;#00a8ff" dur="2s" repeatCount="indefinite" />
    </text>
  </svg>
</p>



# 🚀 Docsxtract-Intelligence

<!-- Put your animation GIF into /assets/gen_ai_animation.gif -->
<p align="center">
  <img src="./assets/gen_ai_animation.gif" alt="Gen AI Animation" width="900"/>
</p>

> Upload PDF, DOCX or any document — ask questions and get answers.  
> Converts documents → metadata → vectors in ChromaDB → LLM-powered answers.

---

## 👋 Hi there — I'm Sitheshwar

Generative AI Developer (Programmer Analyst)  
Passionate about making AI work for real-world impact.

---

## 🧠 Skills & Tech Stack
- Python  
- LangChain  
- LangGraph  
- LLM integration (Bedrock/OpenAI/local)  
- ChromaDB & vector stores

---

## 🚀 Projects & Highlights
- **Contract Intelligence** — document understanding & automation.  
- **HCP Engagement App** — AI-assisted healthcare interactions.  
- **Document Extraction** — robust PDF/DOCX ingestion and querying.

---

## ✨ RAG Workflow (animated GIF)
<p align="center">
  <!-- Optional secondary animation: put it in assets too -->
  <img src="./assets/rag_workflow.gif" alt="RAG Workflow" width="700"/>
</p>

**Flow:** Upload → Extract → Chunk → Embed → Store in ChromaDB → Retrieve → Answer

---

## 🎨 Visual Flair (badges & stats)

<!-- Reliable badges (shields.io) -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/LangChain-%20%20%20%20%20%20%20%20%20-%23ff7b00?logo=langchain" alt="LangChain" />
  <img src="https://img.shields.io/badge/ChromaDB-VectorStore-9cf" alt="ChromaDB" />
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License" />
</p>

<!-- GitHub stats: replace yourusername -->
<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=yourusername&show_icons=true&theme=radical" alt="GitHub stats" height="160"/>
</p>

---

## 🛠 Quick Start

1. Clone:
```bash
git clone https://github.com/yourusername/Docsxtract-intelligence.git
cd Docsxtract-intelligence
