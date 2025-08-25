from states.agent_state import AgentState
from utils.model_loader import chat_model
from langchain_core.messages import AIMessage

def chatbot(state:AgentState):
    out = chat_model().invoke(state["messages"]).content
    return {"messages": [AIMessage(content=out)]}
