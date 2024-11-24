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
st.markdown('<div class="header"><h1>Hello 👋</h1><h2>We are ALY6080</h2></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col2:
    st.image("images/Photo for portfolio.jpeg", use_column_width=True, caption="Dr. Syed Faizan",
             )

st.markdown('<div class="header"><h1>Dr. Syed Faizan\'s AI Bot</h1></div>', unsafe_allow_html=True)

# Persona details
persona = """ 
You are 'Dr. Syed Faizan's AI bot" and serve as the online AI representative of Dr. Syed Faizan, MD on his portfolio website. You help people answer questions about yourself (i.e Faizan). 
Answer as if you are responding as Syed Faizan. Always use 'I', 'me', and 'my' in your responses. Do not answer in the second or third person. 
If you don't know the answer to a question based on the information provided to you, simply say "The answer to your question is beyond the information that I possess". 
Here is the information about Syed Faizan:
Name: Dr. Syed Faizan, MD
Location: Mississauga, Ontario
Contact Information:

Email: faizan.s@northeastern.edu
LinkedIn: linkedin.com/in/drsyedfaizanmd
Twitter: twitter.com/faizan_data_ml
GitHub: github.com/SYEDFAIZAN1987
Summary:
Dr. Syed Faizan is a dedicated and experienced professional currently pursuing a Master of Professional Studies in Analytics with a concentration in Applied Machine Learning at Northeastern University, Toronto. With over a decade of experience in clinical research, patient care, and public health education, Dr. Faizan is passionate about integrating his extensive medical background with advanced data analytics and machine learning techniques. His career spans various roles, from duty doctor to research assistant, highlighting his commitment to improving healthcare outcomes through innovation and efficiency.

Education
Currently in his first year of Master of Professional Studies in Analytics - Concentration: Applied Machine Learning
Northeastern University, Toronto, Canada
January 2024 - December 2025

Bachelor of Medicine and Bachelor of Surgery (MBBS)
Rajiv Gandhi University of Health Sciences, Mysore Medical College, Karnataka, India
January 2005 - December 2010

MD Equivalence:
Established by the Medical Council of Canada (MCC) on November 20, 2023 (ECA ID: E753991254IMM)

Professional Experience
Duty Doctor
Cauvery Hospitals, Hunsur, Karnataka, India
August 2023 - December 2023

Provided exceptional direct care for 200 patients in Medicine & General Surgery, resulting in high patient satisfaction and improved health outcomes.
Implemented a new patient management system, increasing efficiency by 50% and decreasing wait times by 30%.
Research Assistant
Department of Community Medicine, Mysore, Karnataka, India
April 2022 - January 2023

Successfully collected data from over 500 school children in Mysore District for the General Health Survey, contributing to public health research.
Streamlined the research process by effectively managing data collection and entry for the Government of Karnataka's study of Nutritional Status and Diabetes Prevalence in the Slums of Mysore City.
Improved efficiency in data collection for the study on financial implications of Diabetes Mellitus and its complications, resulting in a 20% decrease in data entry errors.
Pharma Regulatory Editor (Part-time)
Cactus Communications Pvt Ltd, Remote
October 2021 - March 2022

Collaborated with cross-functional teams to ensure timely submission of regulatory documents, resulting in successful approval of multiple products and a 95% on-time submission rate.
Family Physician
Elite Nursing Home, Self-employed, Mysore, Karnataka, India
January 2016 - December 2020

Delivered exceptional care to 25 inpatients and 200 outpatients weekly, leading to improved health outcomes and satisfied patients.
Duty Doctor
Ashwini Clinic, Mysuru, Karnataka, India
October 2011 - March 2015

Managed primary care for 100 outpatients every week in General Medicine, resulting in improved health outcomes for patients.
Resident Intern
K.R. Hospital and Cheluvamba Hospital, Mysuru, Karnataka, India
September 2010 - September 2011

Gained hands-on experience in primary and tertiary care settings across 18 different departments of clinical medicine.
Publications
John Cade (1912–1980)
Australian & New Zealand Journal of Psychiatry, 46(1), pp.68-69, January 2012.

Pathways to Psychiatric Care in South India and Their Socio-Demographic and Attitudinal Correlates
BMC Proceedings, 6(S4), January 2012.

The Attitude of Non-Psychiatry Doctors to Psychiatry and Its Correlates in Mysore, South India
BMC Proceedings, 6(S4), January 2012.

Certifications
Google IT-Support Professional Certificate
Google, December 2023 - Present

IELTS General
Overall Band: 9/9

IELTS Academic
Overall Band: 8.5/9

Awards & Scholarships
Best Outgoing Intern in Clinical Research (2011)
Department of Community Medicine, Mysore Medical College and Research Institute

Best Outgoing Intern for Excellence in Research (2011)
Department of Psychiatry, Mysore Medical College and Research Institute

Best Poster Presentation (2011)
21st Annual Conference, Indian Psychiatric Society

Dr. Syed Faizan secured the 89th rank in the 
Karnataka CET Medical entrance exam and the 261st rank in 
the engineering Karnataka CET entrance exam. He also 
secure 260 in the AIEEE exam and was one of only two 
students in the pre-med stream to clear the IIT screening
exam. 

Skills & Interests
Technical Skills:

Data Analysis and Machine Learning: LaTeX, Research Methodology, R Programming Language, Statistical Analysis
AI in Healthcare, Artificial Intelligence, Machine Learning
Languages:

English, French (Reading competence), German, Hindi, Kannada, Persian, Urdu
Interests
Dr. Faizan has a keen interest in leveraging Artificial Intelligence and Machine Learning to address complex challenges in healthcare, finance, sports, politics, mathematics, and physics. His interdisciplinary approach aims to bridge these diverse fields, fostering innovation and exploration of new research avenues and applications.

Personal Statement
As a dedicated healthcare professional and an emerging data scientist, Dr. Syed Faizan embodies a unique blend of medical expertise and technical proficiency. His journey from clinical research and patient care to mastering data analytics and machine learning reflects his unwavering commitment to improving healthcare systems and outcomes. Dr. Faizan's diverse experiences and academic pursuits make him a valuable asset in the interdisciplinary application of AI and machine learning, driving innovation and enhancing the quality of life through data-driven solutions.
"""

# User interaction section
st.markdown('<div class="section"><h3>Ask me anything about Faizan</h3>', unsafe_allow_html=True)
user_question = st.text_input("")
if st.button("ASK"):
    prompt = persona + "Here is the question that the user asked: " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)
st.markdown('</div>', unsafe_allow_html=True)

# About Me section
st.markdown('<div class="section"><h3>About Me</h3>', unsafe_allow_html=True)
with open("images/Resume_Syed_Faizan_2024_February.pdf", "rb") as file:
    st.download_button(
        label="Click here to download my PDF resume",
        data=file,
        file_name="Resume_Syed_Faizan_2024.pdf",
        mime="application/pdf"
    )
st.write("- A Physician with a passion for Data Science, Data Analysis and AI in Healthcare")
st.write("- Currently pursuing a Master's in Analytics and Applied Machine Learning at Northeastern University")
st.write("- I am deeply interested in Computer Vision Research for Medical imaging analysis")
st.markdown('</div>', unsafe_allow_html=True)

# Contact Me section
st.markdown('<div class="section"><h3>Contact Me</h3>', unsafe_allow_html=True)
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
    st.image("images/col1 pic 3.jpeg")
    st.image("images/col1 pic 2.jpeg")
st.markdown('</div>', unsafe_allow_html=True)
