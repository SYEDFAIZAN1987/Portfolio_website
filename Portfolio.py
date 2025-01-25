import streamlit as st
import openai

# Configure OpenAI API
api_key = st.secrets["OPENAI_API_KEY"]
openai.api_key = api_key

# Add custom CSS for styling
st.markdown(
    """
    <style>
    .header {
        background-color: #ADD8E6;
        color: white;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
    }
    .subheader {
        background-color: #87CEEB;
        color: white;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
    }
    .section {
        background-color: #E0FFFF;
        color: #4682B4;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .button {
        background-color: #4682B4;
        color: white;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        display: inline-block;
        margin-top: 10px;
    }
    .button a {
        color: white;
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header section with an image
st.markdown('<div class="header"><h1>Hello 👋</h1><h2> I am Syed Faizan</h2></div>', unsafe_allow_html=True)

col1, = st.columns(1)

with col1:
    st.image("images/faizan.jpeg", use_container_width=True, caption="Syed Faizan")

st.markdown("<div class=\"header\"><h1> Talk to my Resume Bot</h1></div>", unsafe_allow_html=True)

# Persona details
persona = """ 
You are Syed Faizan's delegated chatbot, responsible for answering queries related to his resume. 
Your primary function is to provide responses **only** based on the details present in the resume text below. 
If a question cannot be answered from the provided resume, respond with: 
"This question is beyond my purview to answer."

Syed Faizan, MD – Resume
Scarborough, Ontario • faizan.s@northeastern.edu  
LinkedIn: linkedin.com/in/drsyedfaizanmd  
Personal Website: syedfaizaan.com  
GitHub: https://github.com/SYEDFAIZAN1987  
Hugging Face: https://huggingface.co/DrSyedFaizan  

### **Professional Summary**
- Graduate student in Data Analytics and Applied Machine Learning at Northeastern University.
- Former physician with 10+ years of experience in clinical research, data analytics, and AI applications.
- Expertise in medical imaging analysis, predictive modeling, Retrieval-Augmented Generation (RAG), and AI-driven decision-making.
- Proficient in Python, R, SQL, Machine Learning, Deep Learning, NLP, and Cloud Technologies.
- Current GPA: 4.0.

### **Projects**
1. **CommunityServiceBot** – AI chatbot for Carefirst assisting seniors in accessing healthcare and community services.
2. **RAG Enhanced Presentation Platform (REPP)** – AI-powered tool for United Way Greater Toronto to optimize funding applications and reports.
3. **First Aid Tutor** – AI-driven RAG-based chatbot for emergency medical guidance.
4. **DiabetesDietBot** – AI chatbot for Type 2 Diabetes dietary recommendations.
5. **Customer Churn Prediction** – ML models to predict customer retention using Random Forest & Neural Networks.
6. **Heart Disease Prediction** – SVM-based classification achieving 99.03% accuracy.
7. **Investing in Nashville** – Predictive ML model for real estate investments.
8. **Loan Approval Prediction** – ML-based classification of loan approvals using Logistic Regression & XGBoost.
9. **Magazine Subscription Behavior Analysis** – Predictive analytics for customer retention.
10. **House Price Prediction Using Linear Regression** – Data-driven approach to forecasting real estate trends.

### **Work Experience**
- **Data Analyst & Scientific Advisor** at Tarsal Education Technologies (NLP-based research projects).
- **Resident Physician** at Cauvery Hospitals (direct patient care).
- **Research Assistant** at Department of Community Medicine, Mysore.
- **Regulatory Editor** at Cactus Communications (Pharmaceutical submissions).
- **Family Physician** at Elite Nursing Home.

### **Certifications & Skills**
- **IELTS General**: 9/9, **IELTS Academic**: 8.5/9  
- **Technical Skills**: Python, R, SQL, Power BI, Tableau, LaTeX, AWS, Azure.
"""

# Function to get OpenAI response
def ask_openai(question):
    try:
        prompt = persona + "\n\nUser's question: " + question
        response = openai.ChatCompletion.create(
            model="gpt-4",  # You can change this to "gpt-3.5-turbo" if needed
            messages=[{"role": "system", "content": persona},
                      {"role": "user", "content": question}],
            max_tokens=300  # Limiting response length to prevent overuse
        )
        return response["choices"][0]["message"]["content"]
    except openai.error.OpenAIError as e:
        return f"⚠️ OpenAI API Error: {str(e)}"

# User interaction section
st.markdown('<div class="section"><h3>Ask my chatbot anything about my Resume</h3>', unsafe_allow_html=True)
user_question = st.text_input("Enter your question:")
if st.button("ASK"):
    if user_question:
        response_text = ask_openai(user_question)
        st.write(response_text)
st.markdown('</div>', unsafe_allow_html=True)

# About Me section
st.markdown('<div class="section"><h3>About Me</h3>', unsafe_allow_html=True)
with open("images/sf_resume.pdf", "rb") as file:
    st.download_button(
        label="Click here to download my Resume",
        data=file,
        file_name="sf_resume.pdf",
        mime="application/pdf"
    )
st.write("Welcome to my Resume Chatbot! I am Syed Faizan, a Data Analyst and Machine Learning Engineer with a background in medicine. My research interests include computational radiology, inverse supervised learning for medical imaging analysis, and multimodal AI models for healthcare applications.")

st.markdown('</div>', unsafe_allow_html=True)

# Contact Me section
st.markdown('<div class="section"><h3>Contact Syed Faizan</h3>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col2:
     st.markdown('<div class="button"><a href="https://www.linkedin.com/in/drsyedfaizanmd/">LinkedIn</a></div>', unsafe_allow_html=True)
with col1:
     st.markdown('<div class="button"><a href="mailto:faizan.s@northeastern.edu">Email</a></div>', unsafe_allow_html=True)
with col2:
     st.markdown('<div class="button"><a href="https://twitter.com/faizan_data_ml">Twitter</a></div>', unsafe_allow_html=True)
with col3:
     st.markdown('<div class="button"><a href="https://github.com/SYEDFAIZAN1987">GitHub</a></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
