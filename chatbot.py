from langgraph.graph import StateGraph
from states.agent_state import AgentState
from nodes import chatbot

graph_builder=StateGraph(AgentState)

graph_builder.add_node("chatbot",chatbot)

graph_builder.set_entry_point("chatbot")

graph=graph_builder.compile()

