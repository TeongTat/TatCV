import streamlit as st
import requests

# Page Configuration
st.set_page_config(page_title="My Resume", page_icon="📄", layout="wide")

# Chatbase API Configuration (Replace these with your actual values)
CHATBASE_API_KEY = "your-chatbase-api-key"
CHATBOT_ID = "eXS8hNi5rIpgFQkUKz6GD"

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["🏆 About Me", "📂 Resume", "💬 Ask Me Anything"])
