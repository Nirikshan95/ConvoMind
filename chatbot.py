from langgraph.graph import StateGraph
from states.agent_state import AgentState
from nodes import chatbot
import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver

#connecting database
conn=sqlite3.connect('chatbot_checkpoints.db',check_same_thread=False)
checkpointer=SqliteSaver(conn=conn)

graph_builder=StateGraph(AgentState)

graph_builder.add_node("chatbot",chatbot)

graph_builder.set_entry_point("chatbot")

graph=graph_builder.compile(checkpointer=checkpointer)

