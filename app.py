import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure API Key
genai.configure(api_key=os.getenv("AIzaSyDBYM5oOT2uxfH1H7oRSycbgxVjPmtAUc8")) # GOOGLE_API_KEY

# Load Gemini Model
model = genai.GenerativeModel("gemini-1.5-flash") # gemini-1.5-flash

# Streamlit Page Settings
st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 Gemini AI Chatbot")

st.write("Chat with Gemini AI")

# Store Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Previous Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
user_input = st.chat_input("Type your message...")

if user_input:

    # Save User Message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Display User Message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate AI Response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = model.generate_content(user_input)

            ai_response = response.text

            st.markdown(ai_response)

    # Save AI Response
    st.session_state.messages.append(
        {"role": "assistant", "content": ai_response}
    )