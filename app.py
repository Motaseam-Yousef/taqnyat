import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set the API key
api_key = os.getenv("OPENAI_API_KEY")
prompt = os.getenv("PROMPT")
openai.api_key = api_key
MODEL = "gpt-4o"

# Define a function to respond as a customer service chatbot
def chatbot_response(user_input):
    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

# Streamlit app
st.title('Taqnyat Customer Service Chatbot')

st.write("""
مرحبًا بك في خدمة دعم العملاء لشركة تقنيات الجوال. نحن هنا لمساعدتك في أي استفسارات حول خدماتنا
""")

user_input = st.text_area("كيف يمكنني مساعدتك؟")

if st.button('إرسال'):
    with st.spinner('جاري معالجة استفسارك...'):
        chatbot_reply = chatbot_response(user_input)
        st.success('تم الرد!')
        st.write(chatbot_reply)
