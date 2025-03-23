from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import streamlit as st

from dotenv import load_dotenv
load_dotenv()
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful chatbot")
    ]

model = ChatOpenAI(model="gpt-4o-mini",max_completion_tokens=100)

st.title("AI Chatbot")
st.write("Welcome to the AI Chatbot. Type your message below and get a response from the AI.")

user_input = st.text_area("You: ", height=150)
if st.button("Submit"):
    if user_input.strip():  # Ignore empty inputs
        if user_input.lower() == "exit":
            st.session_state.chat_history = [SystemMessage(content="You are a helpful chatbot")]
            st.experimental_rerun()
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    result = model.invoke(st.session_state.chat_history)
    st.session_state.chat_history.append(AIMessage(content=result.content))
    st.write("AI: ", result.content)
st.subheader("Chat History:")
for msg in st.session_state.chat_history[1:]:  # Skip system message
    role = "You" if isinstance(msg, HumanMessage) else "AI"
    st.write(f"**{role}:** {msg.content}")