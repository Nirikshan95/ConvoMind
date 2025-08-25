from typing import TypedDict,Annotated,List
from langgraph.graph import add_messages

class AgentState(TypedDict):
    messages: Annotated[List,add_messages]