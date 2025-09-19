# ConvoMind

An AI-powered conversational chatbot with persistent memory and multi-threaded chat support built using **LangGraph**, **LangChain**, and **Streamlit**. Experience natural, human-like dialogue with chat history persistence powered by SQLite checkpointing.

---

##  Features

-  **Conversational AI** powered by Hugging Face language models
-  **Persistent Memory** with SQLite-based checkpointing via LangGraph
-  **Multi-threaded Chats** - Create and switch between multiple conversation threads
-  **Interactive Web UI** built with Streamlit
-  **Real-time Streaming** responses for better user experience
-  **Configurable Models** with customizable temperature and token limits
-  **Environment Variables** support for secure API key management

---

##  Project Structure

```
ConvoMind/
├── states/
│   └── agent_state.py      # Agent state definitions using TypedDict
├── utils/
│   └── model_loader.py     # Hugging Face model configuration and loading
├── app.py                  # Streamlit web application
├── chatbot.py             # LangGraph chatbot implementation with SQLite checkpointer
├── nodes.py               # Conversation processing nodes
├── config.py              # Model and server configuration
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

##  Quick Start

### Prerequisites
- Python 3.8 or higher
- Hugging Face account (for API access)

### Installation

```bash
# Clone the repository
git clone https://github.com/Nirikshan95/ConvoMind.git
cd ConvoMind

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Environment Setup

1. Create a `.env` file in the project root:
```bash
HUGGINGFACE_API_TOKEN=your_hugging_face_api_token_here
```

2. Configure model settings in `config.py` (optional):
```python
REPO_ID = "openai/gpt-oss-120b"  # Change to your preferred model
MAX_TOKENS = 1000
TEMPERATURE = 0.7
```

### Running the Application

```bash
# Start the Streamlit application
streamlit run app.py
```

The application will be available at `http://localhost:8501`

---

##  Usage

1. **Start Chatting**: Open the application and type your message in the chat input
2. **Create New Threads**: Click "New Chat" in the sidebar to start a fresh conversation
3. **Switch Between Chats**: Click on any thread ID in the sidebar to resume previous conversations
4. **Persistent History**: All conversations are automatically saved and can be resumed later

---

##  Configuration

### Model Configuration (`config.py`)
- `REPO_ID`: Hugging Face model repository ID
- `MAX_TOKENS`: Maximum number of tokens for model responses
- `TEMPERATURE`: Controls randomness in responses (0.0 = deterministic, 1.0 = very random)

### Database
- Chat history is stored in `chatbot_checkpoints.db` (SQLite)
- Automatic persistence across application restarts

---

##  Architecture

### Core Components

1. **Agent State** (`states/agent_state.py`)
   - Manages conversation messages using LangGraph's `add_messages`

2. **Model Loader** (`utils/model_loader.py`)
   - Configures and loads Hugging Face chat models
   - Supports environment variable configuration

3. **Chatbot Graph** (`chatbot.py`)
   - Implements LangGraph state machine
   - SQLite checkpointer for persistence

4. **Processing Nodes** (`nodes.py`)
   - Handles message processing and AI response generation

5. **Streamlit App** (`app.py`)
   - Web interface with chat UI
   - Multi-thread management
   - Real-time response streaming

---

##  Dependencies

- **langgraph**: State machine framework for conversational AI
- **langchain-huggingface**: Hugging Face integration for LangChain
- **streamlit**: Web application framework
- **langgraph-checkpoint-sqlite**: SQLite persistence for LangGraph
- **python-dotenv**: Environment variable management
- **fastapi & uvicorn**: API framework (for future extensions)
- **pydantic**: Data validation

---

##  Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/<feature-name>`)
3. Commit your changes (`git commit -m 'Add <feature-name> feature'`)
4. Push to the branch (`git push origin feature/<feature-name>)
5. Open a Pull Request

---

##  License

This project is open source and available under the [MIT License](LICENSE).

---

##  Future Enhancements

- [ ] Vector database integration (FAISS, Chroma)
- [ ] Advanced memory summarization
- [ ] Custom model fine-tuning support
- [ ] REST API endpoints
- [ ] User authentication
- [ ] Export chat history
- [ ] Theme customization

---

##  Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/Nirikshan95/ConvoMind/issues) page
2. Create a new issue with detailed description
3. For general questions, use the [Discussions](https://github.com/Nirikshan95/ConvoMind/discussions) tab

---

**Made with ❤️ by [Nirikshan95](https://github.com/Nirikshan95)**