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
    st.image("IMG_6347.JPG", width=800)  # Optional profile picture
    st.write("""
    🎓 **Master's in Data Science** graduate  
    🔍 Seeking a **Cloud Associate / Data Science Role / Data Analyst**  
    💡 Passionate about **AI, data analytics, and cloud computing**  
    📍 Based in Selangor, (willing to relocate)  
    """)
    

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

# Resume Page
elif page == "📂 Resume":
    st.title("📄 My Resume")

    with open("resume.pdf", "rb") as file:
        resume_data = file.read()

    st.download_button(label="📥 Download My Resume", data=resume_data, file_name="resume.pdf", mime="application/pdf")

    st.subheader("🎯 Work Experience")
    st.write("""
    - **[Senior Operation Executive]** @ [Fortunata Remit Sdn. Bhd.] (10/2021 - Present)  
    - **[Finance Manager (Maternity Replacement)]** @ [ICMC Malaysia] (10/2020 - 3/2021)  
    - **[Senior Account & Admin Executive]** @ [Ho Car Sdn. Bhd.] (12/2014 - 10/2020)  
    - **[Intercompany Reconciliation Analyst]** @ [BASF Asia Pacific Service Center] (01/2012 - 07/2014)  
    """)

    st.subheader("📊 Projects")
    st.write("""
    - **[Heart Disease Predictor]**: The modelling will predict user on chances of having heart disease.  
    - **[Carbon Emission Predictor]**: Predict the CO2 based on Electricity Generation and locations.
    - **[Stock Price prediction]**: Predict the S&P 500 stock price.
    """)
    
# Chatbot Page (Chatbase Integration)
elif page == "💬 Ask Me Anything":
    st.title("💬 Chat With Me About My Work")

    user_question = st.text_input("Ask me about my experience, skills, or projects:")

    if user_question:
        # Send request to Chatbase API
        url = f"https://www.chatbase.co/api/v1/chat"
        headers = {
            "Authorization": f"Bearer {CHATBASE_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "messages": [{"role": "user", "content": user_question}],
            "chatbotId": CHATBOT_ID
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            bot_reply = response.json().get("messages", [{}])[0].get("content", "Sorry, I couldn't process that.")
            st.write(bot_reply)
        else:
            st.error("Error: Unable to fetch response. Check your API key and chatbot ID.")
