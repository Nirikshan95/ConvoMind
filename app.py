import streamlit as st
from chatbot import graph
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# session setup

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


st.title("ConvoMind")
st.header("An AI-powered conversational chatbot")

for message in st.session_state.chat_history:
    st.chat_message(message["role"]).markdown(message["content"])

text_input=st.chat_input("Ask anything..")

if text_input:
    st.chat_message("user").write(text_input)
    st.session_state.chat_history.append({"role":"user","content":text_input})
    with st.chat_message("assistant"):
        response_placeholder=st.empty()
        full_response=""
        for chunk in graph.stream({"messages":HumanMessage(text_input)},config={"configurable":{"thread_id":201}}):
            #st.markdown(chunk["chatbot"]["messages"])
            if isinstance(chunk["chatbot"]["messages"][-1], AIMessage):
                response=chunk["chatbot"]["messages"][-1].content
                full_response=response
                response_placeholder.markdown(full_response)
        st.session_state.chat_history.append({"role":"assistant","content":full_response})