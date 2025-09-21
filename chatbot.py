from langgraph.graph import StateGraph
from states.agent_state import AgentState
from nodes import chatbot
import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver

def retrive_all_threads():
    threads=set()
    for check in checkpointer.list(config=None):
        threads.add(check.config["configurable"]["thread_id"])
    return list(threads)

#connecting database
conn=sqlite3.connect('chatbot_checkpoints.db',check_same_thread=False)
checkpointer=SqliteSaver(conn=conn)

graph_builder=StateGraph(AgentState)

graph_builder.add_node("chatbot",chatbot)

graph_builder.set_entry_point("chatbot")

graph=graph_builder.compile(checkpointer=checkpointer)

