import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Page settings
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot")
st.write("Hi there! I’m your AI assistant. Ask me anything 👇")

# Get user input
user_input = st.chat_input("Type your message...")

# Store conversation history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are a helpful and friendly AI assistant."}
    ]

# Process user message and generate a response
if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})

    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # You can also use gpt-4o or gpt-3.5-turbo
            messages=st.session_state["messages"]
        )
        reply = response.choices[0].message.content
        st.session_state["messages"].append({"role": "assistant", "content": reply})

# Display conversation history
for message in st.session_state["messages"][1:]:  # skip system message
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])
