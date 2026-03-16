from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

st.title("🤖 AI-Powered Conversational Question Answering Chatbot")
st.markdown('The AI-powered Q&A chatbot is a conversational system that utilizes Large Language Models and LangChain to interpret user queries and generate accurate responses. The system uses prompt templates, chaining mechanisms, and structured input processing to deliver domain-specific answers. This project demonstrates practical implementation of conversational AI and prompt engineering for building intelligent assistants.')

query= st.chat_input("Ask me ?")

if "messages" not in st.session_state:
    st.session_state.messages=[]
for message in st.session_state.messages:
    role=message["role"]
    content=message["content"]
    st.chat_message(role).markdown(content)


if query :
    st.session_state.messages.append({"role":"user", "content":query})
    st.chat_message('User').markdown(query)
    res=llm.invoke(st.session_state.messages)
    st.session_state.messages.append({"role":"ai", "content":res.content})
    st.chat_message("AI").markdown(res.content)