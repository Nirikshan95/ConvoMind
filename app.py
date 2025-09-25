import streamlit as st
from chatbot import graph,retrive_all_threads
from langchain_core.messages import AIMessage, HumanMessage
import uuid

def generate_thread_id():
    return str(uuid.uuid4())
def reset_chat():
    st.session_state.chat_history = []
    st.session_state.thread_id = generate_thread_id()
    if st.session_state.thread_id not in st.session_state.chat_threads:
        st.session_state.chat_threads.append(st.session_state.thread_id)
def load_chat(thread_id):
    try:
        return graph.get_state(config={"configurable":{"thread_id":thread_id}}).values["messages"]
    except:
        print(f"No chat history found for this thread :{thread_id} .")
        return []

# session setup
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "chat_threads" not in st.session_state:
    st.session_state.chat_threads = retrive_all_threads()
if "thread_id" not in st.session_state:
    st.session_state.thread_id = generate_thread_id()
    st.session_state.chat_threads.append(st.session_state.thread_id)



st.title("ConvoMind")
st.header("An AI-powered conversational chatbot")

st.sidebar.header("Chats")
if st.session_state.chat_history and st.session_state.chat_history !=[None]:
    if st.sidebar.button("New Chat"):
        reset_chat()
st.sidebar.write("Your Chats")
for id in reversed(st.session_state.chat_threads):
    if st.sidebar.button(str(id)):
        st.session_state.thread_id = id
        st.session_state.chat_history = load_chat(id)

# Conversations
for msg in st.session_state.chat_history:
    if isinstance(msg,AIMessage):
        st.chat_message("assistant").markdown(msg.content)
    elif isinstance(msg,HumanMessage):
        st.chat_message("user").markdown(msg.content)
    else :
        st.empty()

text_input=st.chat_input("Ask anything..")

if text_input:
    st.chat_message("user").write(text_input)
    st.session_state.chat_history.append(HumanMessage(content=text_input))
    with st.chat_message("assistant"):
        response=st.write_stream(
            chunk.content
            for chunk,meta in graph.stream(
                {"messages": st.session_state.chat_history},
                config={"configurable":{"thread_id":st.session_state.thread_id}},
                stream_mode="messages"
                )
            )
        st.session_state.chat_history.append(AIMessage(content=response))