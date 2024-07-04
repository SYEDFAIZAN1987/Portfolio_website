import streamlit as st
import google.generativeai as genai


api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

# Custom CSS to add background color and style subheadings
st.markdown(
    """
    <style>
    .blue-background {
        background-color: #ADD8E6;
        padding: 20px;
        border-radius: 10px;
    }
    .red-subheading h2 {
        color: red;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Apply custom CSS to the entire app
st.markdown('<div class="blue-background">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="red-subheading"><h2>Hello 👋</h2></div>', unsafe_allow_html=True)
    st.title("I am Syed Faizan")

with col2:
    st.image("images/Photo for portfolio.jpeg")

st.title("Faizan's AI Bot")

persona = """ 
You are Syed Faizan AI bot. You help people answer questions about your self (i.e Faizan). 
Answer as if you are responding . Do not answer in second or third person. 
If you don't know they answer you simply say "That's a secret". 
Here is more info about Faizan:
"""

user_question = st.text_input("Ask me anything about Faizan")
if st.button("ASK", use_container_width=True):
    prompt = persona + "Here is the question that the user asked" + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="red-subheading"><h2>Linkedin</h2></div>', unsafe_allow_html=True)
    st.markdown("[Click here to visit my Linkedin](https://www.linkedin.com/in/drsyedfaizanmd/)")
    st.write("- A Physician with a passion for Data Science, Data Analysis and AI in Healthcare")
    st.write("- Currently pursuing a Master's in Analytics and Applied Machine Learning at Northeastern University")
    st.write("- I am deeply interested in Computer Vision Research for Medical imaging analysis")
# Close the custom background div
st.markdown('</div>', unsafe_allow_html=True)


st.title("My Setup")

