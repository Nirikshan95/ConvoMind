# ConvoMind
An AI-powered conversational chatbot with **hybrid memory** (sliding window + summarization) for natural, human-like dialogue — inspired by ChatGPT.

---

## Features
- **Conversational AI** using large language models (LLMs)
- **Hybrid Memory**: short-term sliding window + long-term summarization
- **Efficient Context Handling** to avoid token overflow
- Easily extendable with vector DBs (FAISS, Chroma) for retrieval-based memory
- Built with **LangGraph** and **LangChain**

---

## Project Structure
```
convomind/
  ├── state/ # Agent state definitions
  ├── nodes/ # Conversation nodes (LLM, memory update, etc.)
  ├── chatbot.py
  ├── utils/ # Helper functions (summarizer, sliding window, etc.)
  ├── main.py # Entry point to run chatbot
  ├── requirements.txt # Python dependencies
  └── README.md # Project documentation
```

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/your-Nirikshan95/ConvoMind.git
cd ConvoMind

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
