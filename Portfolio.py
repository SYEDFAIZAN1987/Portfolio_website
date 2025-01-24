import streamlit as st
import google.generativeai as genai

# Configure the generative AI model
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

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

col1 = st.columns(1)

with col1:
    st.image("images/Photo for portfolio.jpeg", use_container_width=True, caption="Syed Faizan")



    

st.markdown("<div class=\"header\"><h1> Talk to my Resume Bot</h1></div>", unsafe_allow_html=True)


# Persona details
persona = """ 
You are Syed Faizan's delegated chatbot, responsible for answering queries related to his resume. Your primary function is to provide responses only based on the details present in the resume text below. If a question cannot be answered from the provided resume, respond with: 
"This question is beyond my purview to answer."

Syed Faizan, MD – Resume
Scarborough, Ontario • +1 289-885-4110 • faizan.s@northeastern.edu  
LinkedIn: linkedin.com/in/drsyedfaizanmd  
Personal Website: syedfaizaan.com  
GitHub: https://github.com/SYEDFAIZAN1987  
Hugging Face: https://huggingface.co/DrSyedFaizan  

Professional Summary:
- Graduate student in Data Analytics and Applied Machine Learning at Northeastern University.
- Former physician with 10+ years of experience in clinical research, data analytics, and AI applications.
- Expertise in medical imaging analysis, predictive modeling, Retrieval-Augmented Generation (RAG), and AI-driven decision-making.
- Proficient in Python, R, SQL, Machine Learning, Deep Learning, NLP, and Cloud Technologies.
- Current GPA: 4.0.

Education:
- Master's in Data Analysis and Applied Machine Intelligence, Northeastern University (2024 - 2025).
- M.B.B.S (MD Equivalent), Mysore Medical College, Rajiv Gandhi University of Health Sciences.

Projects:
1. CommunityServiceBot – AI chatbot for Carefirst assisting seniors in accessing healthcare and community services.
2. RAG Enhanced Presentation Platform (REPP) – AI-powered tool for United Way Greater Toronto to optimize funding applications and reports.
3. First Aid Tutor – AI-driven RAG-based chatbot for emergency medical guidance.
4. DiabetesDietBot – AI chatbot for Type 2 Diabetes dietary recommendations.
5. Airbnb NYC Analysis – Statistical modeling of short-term rental pricing and trends.
6. Customer Churn Prediction – ML models to predict customer retention using Random Forest & Neural Networks.
7. Heart Disease Prediction – SVM-based classification achieving 99.03% accuracy.
8. Investing in Nashville – Predictive ML model for real estate investments.
9. Loan Approval Prediction – ML-based classification of loan approvals using Logistic Regression & XGBoost.
10. Magazine Subscription Behavior Analysis – Predictive analytics for customer retention.

Work Experience:
- Data Analyst & Scientific Advisor at Tarsal Education Technologies, focusing on NLP projects.
- Resident Physician at Cauvery Hospitals, providing direct patient care.
- Research Assistant at Department of Community Medicine, Mysore.
- Regulatory Editor at Cactus Communications, working on pharmaceutical documents.
- Family Physician at Elite Nursing Home, managing general medicine cases.

Publications:
- Psychiatric Care Pathways in South India – Published in BMC Proceedings.
- Attitudes of Non-Psychiatry Doctors to Psychiatry – Research study in BMC Proceedings.

Certifications & Language Proficiency:
- IELTS General: 9/9  
- IELTS Academic: 8.5/9  
- Fluent in Python, R, SQL, Power BI, Tableau, LaTeX, and Cloud Computing (AWS, Azure).

Behavioral Guidelines for the Chatbot:
- Always reference the resume when answering questions.
- If a query is outside the scope of the resume, respond with:
  "This question is beyond my purview to answer."
- Provide structured and concise answers without unnecessary elaboration.
- Ensure responses are aligned with Syed Faizan's listed qualifications, skills, and experiences.
"""

# User interaction section
st.markdown('<div class="section"><h3>Ask my  chatbot anything about my Resume</h3>', unsafe_allow_html=True)
user_question = st.text_input("")
if st.button("ASK"):
    prompt = persona + "Here is the question that the user asked: " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)
st.markdown('</div>', unsafe_allow_html=True)

# About Me section
st.markdown('<div class="section"><h3>About me</h3>', unsafe_allow_html=True)
with open("images/ALY_6080_Experential_learning_Group_1_Module_12_Capstone_Sponsor_Deliverable.pdf", "rb") as file:
    st.download_button(
        label="Click here to download my Resume",
        data=file,
        file_name="ALY_6080_Experential_learning_Group_1_Module_12_Capstone_Sponsor_Deliverable.pdf",
        mime="application/pdf"
    )
st.write(" Welcome to my Resume Chatbot! My name is Syed Faizan, and I am a Data Analyst and Machine Learning Engineer , trained physician with a deep passion for advancing healthcare and other sectors like finance, banking, agriculture, and education through technology. My primary research interests lie in Computational Radiology, particularly in Inverse Supervised Learning for medical imaging analysis and Multimodal Models for healthcare applications. I am fascinated by how cutting-edge AI techniques can address disparities in healthcare delivery, improve diagnostic accuracy, and empower clinicians to make data-driven decisions. Leveraging my background in medicine and machine learning, I aspire to contribute to innovative solutions at the intersection of technology and healthcare.")
st.write(" My professional life has been an exciting journey from clinical practice in India to the world of data analytics and machine learning. After earning my Bachelor of Medicine and Bachelor of Surgery from Rajiv Gandhi University of Health Sciences, I spent over a decade as a physician, excelling in clinical research and patient care. I further honed my skills as a resident physician at clinics, hospitals, and nursing homes. During this period, I developed a nuanced understanding of healthcare systems and their challenges. ")
st.write("Currently, I am pursuing a Master of Professional Studies in Analytics with a concentration in Applied Machine Learning at Northeastern University (January 2024–December 2025). My academic achievements include maintaining a GPA of 4.0 and several projects, including REPP a RAG based platform that was featured in the Northeastern University Showcase as a poster.Throughout my career, I have consistently blended medical expertise with analytical skills. As a Research Assistant (April 2022–January 2023), I contributed to public health studies, including the Government of Karnataka’s study on nutritional status and diabetes prevalence in urban slums. My work not only streamlined data collection processes but also improved data entry accuracy by 20%. These experiences have deepened my commitment to leveraging data to address real-world healthcare challenges.")
st.write("I have also collaborated in cross-functional teams as a Pharma Regulatory Editor at Cactus Communications (October 2021–March 2022), ensuring timely submission of critical documents with a 95% on-time success rate. My research contributions have been recognized internationally, including publications in esteemed journals like the Australian & New Zealand Journal of Psychiatry and BMC Proceedings.")
st.write("Looking ahead, I am excited to explore opportunities in Data Analysis and Machine Learning that allow me to contribute to impactful projects. Whether it’s analysing financial data, integrating AI into the banking sector, solving healthcare challenges with AI or innovating new AI tools, I am eager to bring my unique blend of medical knowledge and data expertise to dynamic teams and forward-thinking organizations.")
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

# Gallery section
st.markdown('<div class="section"><h3>Gallery</h3>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/col1 pic 1.jpeg")

    st.image("images/col 2 pic 3.jpeg")


with col2:
    st.image("images/col 2 pic 1.jpeg")
    st.image("images/col 2 pic 2.jpeg")

with col3:
    st.image("images/Pravalika.jpeg")
    st.image("images/VrajShah.jpeg")
st.markdown('</div>', unsafe_allow_html=True)
