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

# About Me Page
if page == "🏆 About Me":
    st.title("Hi, I'm Teong Tat 👋")
    st.write("""
    🎓 **Master's in Data Science** graduate  
    🔍 Seeking a **Cloud Associate / Data Science Role / Data Analyst**  
    💡 Passionate about **AI, data analytics, and cloud computing**  
    📍 Based in Selangor, (willing to relocate)  
    """)
    st.image("IMG_6347.JPG", width=200)  # Optional profile picture

    # Skills Section
    st.subheader("🛠 Skills & Technologies")
    st.write("""
    - **Programming:** Python, R language  
    - **Data Tools:** Power BI, Tableau, Streamlit  
    - **Cloud Platforms:** AWS, GCP  
    - **Big Data:** Hive, MongoDB, HBase  
    """)

    # Contact Info
    st.subheader("📬 Contact")
    st.write("📧 Email: teongtat@yahoo.com")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/tat-seah/) | [GitHub](https://github.com/TeongTat)")
