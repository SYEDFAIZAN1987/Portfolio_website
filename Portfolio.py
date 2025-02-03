import streamlit as st
import openai

# Configure OpenAI API
api_key = st.secrets["OPENAI_API_KEY"]
openai.api_key = api_key

# Add improved custom CSS for styling
st.markdown(
    """
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600&display=swap');

    body {
        font-family: 'Montserrat', sans-serif;
        background-color: #F4F8FB;
    }

    /* Header Styling */
    .header {
        background: linear-gradient(135deg, #6DD5FA, #2980B9);
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 26px;
        font-weight: 600;
    }

    /* Subheader Styling */
    .subheader {
        background: linear-gradient(135deg, #87CEEB, #4682B4);
        color: white;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        font-size: 20px;
        font-weight: 500;
    }

    /* Section Box */
    .section {
        background: white;
        color: #333;
        padding: 25px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }

    /* Buttons */
    .button {
        background: linear-gradient(135deg, #4682B4, #1E3C72);
        color: white;
        padding: 12px 20px;
        border-radius: 8px;
        text-align: center;
        display: inline-block;
        margin-top: 15px;
        font-weight: 500;
        transition: all 0.3s ease-in-out;
    }

    .button:hover {
        background: linear-gradient(135deg, #1E3C72, #0F1B4C);
        transform: scale(1.05);
    }

    .button a {
        color: white;
        text-decoration: none;
        font-size: 16px;
    }

    /* Centering content */
    .center {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Header section with an image
st.markdown('<div class="header"><h1>Hello 👋</h1><h2> I am Syed Faizan</h2></div>', unsafe_allow_html=True)

col1,col2,col3 = st.columns(3)

with col2:
    st.image("images/faizan.jpeg", use_container_width=False, caption="Syed Faizan, MD")

st.markdown("<div class=\"header\"><h1> Talk to my Resume Bot</h1></div>", unsafe_allow_html=True)

# Persona details
persona = """ 
You are Syed Faizan's delegated chatbot, responsible for answering queries related to his resume. 
Your primary function is to provide responses **only** based on the details present in the resume text below. 
If a question cannot be answered from the provided resume, respond with: 
"This question is beyond my purview to answer."

Syed Faizan, MD
Scarborough, Ontario • +1 289-885-4110 • faizan.s@northeastern.edu • linkedin.com/in/drsyedfaizanmd •
syedfaizaan.com
Github: https://github.com/SYEDFAIZAN1987
Huggingface: https://huggingface.co/DrSyedFaizan
Graduate Student | Data Analyst | Machine Learning & AI Enthusiast
Current GPA: 4.0
Bringing over a decade of experience as a physician, I integrate healthcare domain expertise with advanced
skills in data analytics, machine learning, and AI. Currently pursuing a Master’s in Data Analytics and Applied
Machine Learning at Northeastern University, my special interests include medical imaging analysis, predictive
modeling, retrieval augmented generation, and AI-driven decision-making for complex data challenges.
My expertise spans:
✔ Data Analysis: Exploratory Data Analysis, Statistical modeling.
✔ Machine Learning & Deep Learning: Supervised & Unsupervised Learning, NLP, Computer Vision
✔ Big Data & Cloud Technologies: SQL, Python (Pandas, Scikit-Learn, TensorFlow, PyTorch), AWS, Azure
✔ Data Visualization & Business Intelligence: Power BI, Tableau, Matplotlib, Seaborn,Plotly,GGPlot
EDUCATION

Master's in Data Analysis and Applied Machine Intelligence
Northeastern University • Toronto, Canada • 01/2024 - 12/2025

M.B.B.S (MD Equivalent, Bachelor Of Medicine and Bachelor Of Surgery)
Rajiv Gandhi University of Health Sciences, Mysore Medical College • Karnataka, India
PROJECTS

Crrently I am working on a Lung Tumour Segmentation project using UNET . 

The following are my Medical Imaging Analysis Projects - 
Projects

1. 3D Liver Segmentation: Developed a UNet-based model for liver and tumor segmentation from 3D medical images, achieving
precise results validated through visual and loss analysis.
2. Left Atrium Segmentation: Built a U-Net model for cardiac MRI images, achieving a Dice Similarity Coefficient of 0.95.
3. Cardiac Detection: Implemented a customized ResNet-18 model with PyTorch Lightning for identifying cardiac abnormalities
using medical imaging data.
4. Pneumonia Classification: Built a ResNet-18 based classifier for chest X-ray analysis, achieving 84.5% validation accuracy
with CAM visualization.

The following are my Computer Vision Projects - 
ANN for MNIST: Developed an Artificial Neural Network using PyTorch, achieving 98.5% training and 97.8% validation
accuracy.
CNN for MNIST: Implemented convolutional layers with high accuracy of 98% through supervised learning.


CommunityServiceBot • 01/2025 - 01/2025
CareFirst

• I developed the evaluation pipeline and tuned the Community Service Chatbot, which is a proprietary AIdriven assistant designed for Carefirst Ontario Services, primarily serving seniors in Toronto.

• The chatbot leverages Giskard for robust Retrieval-Augmented Generation (RAG) evaluation using varied
metrics to ensure accuracy and relevancy of responses.

RAG Enhanced Presentation Platform (REPP) • 11/2024 - 01/2025
United Way Greater Toronto
Tools & Technologies: OpenAI GPT-3.5-Turbo API, FAISS, MySQL, Firebase,Streamlit, Power BI
• Developed a web-based application to streamline academic and professional presentations, integrating
Retrieval-Augmented Generation (RAG) for interactive AI-supported reports.

• Implemented FAISS for efficient document retrieval and validated performance using the Stanford SQuAD
dataset. Future improvements include mobile applications and cloud integration.

First Aid Tutor • 12/2024 - 01/2025

Mysore Medical College and Research Institute
Tools & Technologies: Python, RAG, TF-IDF, Gradio
Description: Developed an AI-powered chatbot using Retrieval-Augmented Generation (RAG) to provide firstaid guidance based on medical literature. Evaluated response accuracy using RAGAS metrics and semantic
similarity models.

DiabetesDietBot • 01/2025 - 01/2025
Mysore Medical College and Research Institute
• DiabetesDietBot is an AI-powered chatbot developed by me for Mysore Medical College and Research
Institute as part of a research study on how chatbots can assist doctors and medical students in
recommending predefined diet plans to patients with Type 2 Diabetes.

• The bot leverages Retrieval-Augmented Generation (RAG), FAISS vector search, and OpenAI's GPT-3.5-turbo
to provide personalized diet recommendations based on patient profiles.

Airbnb Analysis of Short-Term Rentals in NYC
Tools & Technologies: R, Python, Tableau, LASSO & Ridge Regression
Description: Conducted an in-depth analysis of Airbnb rental trends in NYC using regression models and

statistical analysis. Identified neighborhood and room type impacts on pricing, and developed predictive
models to optimize rental strategies. Created Tableau dashboards for interactive visualization.

Customer Churn Prediction
Tools & Technologies: Python, Scikit-learn, SMOTE, Random Forest, Neural Networks
Description: Designed and compared machine learning models to predict customer churn, addressing class
imbalance using SMOTE. Utilized decision trees, SVMs, and neural networks to optimize predictive performance,
achieving an AUC of 0.86 with Random Forest.

Cost-Benefit Analysis of Dam Construction Projects
Tools & Technologies: Excel, Monte Carlo Simulations, Chi-Squared Tests
Description: Conducted economic feasibility analysis for two proposed dam projects using simulation-based
benefit-cost ratios. Recommended the most viable project based on probability distributions and sensitivity
analysis.

Inventory Management Decision Model
Tools & Technologies: Excel, R, Solver, EOQ Model
Description: Developed an Economic Order Quantity (EOQ) model for inventory optimization in a
manufacturing company. Used Solver to validate results and performed sensitivity analysis to determine costeffective inventory strategies.

Maximizing Profit: Optimization Model for Inventory Management
Tools & Technologies: Excel, Linear Programming, Sensitivity Analysis
Description: Designed a profit-maximizing inventory allocation model for a hardware company expanding into
a new region. Conducted sensitivity analysis to optimize inventory levels, budget, and warehouse space
allocation.

Time Series Forecasting of Stock Prices
Tools & Technologies: Excel, Exponential Smoothing, Regression Analysis
Description: Forecasted Apple Inc. and Honeywell stock prices using time series models. Applied exponential
smoothing and weighted moving averages to predict stock trends, optimizing portfolio allocation.

Transshipment Model and Risk Minimization
Tools & Technologies: Excel, Linear Programming
Description: Developed a transshipment optimization model to minimize shipping costs and balance supplydemand across warehouses. Conducted risk analysis and cost-effectiveness evaluations using sensitivity
analysis.

Electric Vehicles Market Before Tesla: R Shiny Application
Tools & Technologies: R Shiny, Tableau, Data Visualization
Description: Built an interactive dashboard to analyze electric vehicle adoption trends, evaluating
manufacturer strategies and Clean Alternative Fuel Vehicle (CAFV) incentives.

Heart Disease Prediction Using SVM
Tools & Technologies: Python, SVM, GridSearchCV
Description: Developed a predictive model using Support Vector Machines to classify heart disease cases.
Achieved 99.03% accuracy with optimized hyperparameters, demonstrating high sensitivity and specificity.

Investing in Nashville: Predictive Modeling for Real Estate
Tools & Technologies: Python, Decision Trees, Random Forest, Gradient Boosting
Description: Predicted undervalued and overvalued properties using machine learning models, assisting real
estate investors in making data-driven decisions.

Loan Approval Prediction Using Machine Learning
Tools & Technologies: Python, Logistic Regression, Random Forest, XGBoost
Description: Built machine learning models to predict loan approvals, optimizing model performance with
SMOTE and ensemble techniques.

Magazine Subscription Behavior Analysis Using Logistic Regression and SVM
Tools & Technologies: Python, SVM, GridSearchCV
Description: Analyzed customer behavior and marketing campaign effectiveness using predictive models to
optimize subscription strategies.

House Price Prediction Using Linear Regression
Tools & Technologies: R, Linear Regression, Feature Engineering
Description: Predicted housing prices in Ames, Iowa, using regression models, addressing multicollinearity and
optimizing feature selection.

Analyzing Income Inequality Using KNN

Used Car Sales Analysis
Tools & Technologies: R, Regression Modeling
Description: Analyzed used car pricing trends and key valuation factors using regression models.
WORK EXPERIENCE

Tarsal Education Technologies, Toronto, Ontario, Canada. • Remote • 03/2024 - 12/2024
Data Analyst and Scientific Advisor • Contractor

• Led NLP projects that extracted actionable insights from educational datasets, improving decision-making
processes for stakeholders.Prepared project schema, advised on educational content.

Cauvery Hospitals • Hunsur, Karnataka, India • 08/2023 - 12/2023
Resident Physician

• Provided exceptional direct care for 200 patients in Medicine & Gen Surgery, resulting in high patient
satisfaction and improved health outcomes.

Department Of Community Medicine • Mysore, Karnataka, India • 04/2022 - 01/2023
Research Assistant
• Successfully collected data from 500+ school children in Mysore District for the General Health Survey,
contributing to public health research. Analysed the data for insights and improved efficiency in data
collection.

Cactus Communications Pvt Ltd • Remote • 10/2021 - 03/2022
Pharma Regulatory Editor

• Collaborated with cross-functional teams to ensure timely submission of regulatory documents, resulting in
successful approval of multiple products and a 95% on-time submission rate.

Elite Nursing Home • Mysore, Karnataka, India • 01/2016 - 12/2020
Family Physician

• Delivered exceptional care to 25 inpatients and 200 outpatients weekly, leading to improved health
outcomes and satisfied patients.

Ashwini Clinic • Mysuru, Karnataka, India • 10/2011 - 03/2015
Resident Physician
• Managed primary care for 100 outpatients every week in General Medicine, resulting in improved health
outcomes for patients.

K. R. Hospital and Cheluvamba Hospital • Mysuru, Karnataka, India • 09/2010 - 09/2011
Resident Intern

• Hands-on experience in primary and tertiary care settings in 18 different departments of clinical medicine.

PUBLICATIONS

Abhishekh, H. and Faizan, S. (2012)

Australian & New Zealand Journal of Psychiatry
John Cade (1912- 1980), pp.68-69

Faizan, S., Raveesh, B., Ravindra, L. and Sharath,K. (2012)
BMC Proceedings

Pathways to psychiatric care in South India and their socio-demographic and attitudinal correlates.

Faizan, S., Raveesh, B,Anjali, V., Lakshmanagowda Sujatha,R. and Sharath,K. (2012)
BMC Proceedings
The attitude of non-psychiatry doctors to psychiatry and its correlates in Mysore, South India.
ENGLISH COMPETENCE

IELTS General 9/9 Overall Band
IELTS

IELTS Academic 8.5/9 Overall Band
IELTS

SKILLS
AI ​in ​Healthcare, Applied ​Machine ​Learning, Artificial ​Intelligence, Clinical ​Research, Data ​Analysis, Deep ​Learning,
LaTeX, Machine ​Learning, Python, R ​Programming ​Language, SQL, Statistical ​Analysis


"""

# Function to get OpenAI response
def ask_openai(question):
    prompt = persona + "\n\nUser's question: " + question
    response = openai.ChatCompletion.create(
        model="gpt-4",  # You can change this to "gpt-3.5-turbo" if needed
        messages=[{"role": "system", "content": persona},
                  {"role": "user", "content": question}],
        max_tokens=300  # Limiting response length to prevent overuse
    )
    return response["choices"][0]["message"]["content"]

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
st.write("""
# Welcome to my Resume Chatbot!

###
My name is **Syed Faizan**, and I am a **Data Analyst and Machine Learning Engineer**, as well as a trained **physician** with a deep passion for advancing healthcare and other sectors like **finance, banking, agriculture, and education** through technology. 

My primary research interests lie in **Computational Radiology**, particularly in **Inverse Supervised Learning for medical imaging analysis** and **Multimodal Models for healthcare applications**. I am fascinated by how cutting-edge AI techniques can address **disparities in healthcare delivery, improve diagnostic accuracy, and empower clinicians** to make data-driven decisions. Leveraging my background in **medicine and machine learning**, I aspire to contribute to **innovative solutions at the intersection of technology and healthcare**.

---

### **My Journey**
My professional life has been an **exciting journey** from **clinical practice in India** to the world of **data analytics and machine learning**. After earning my **Bachelor of Medicine and Bachelor of Surgery** from **Rajiv Gandhi University of Health Sciences**, I spent **over a decade as a physician**, excelling in **clinical research and patient care**. I further honed my skills as a **resident physician** at clinics, hospitals, and nursing homes, gaining a **nuanced understanding of healthcare systems and their challenges**.

Currently, I am pursuing a **Master of Professional Studies in Analytics** with a concentration in **Applied Machine Learning** at **Northeastern University** *(January 2024–December 2025)*. My academic achievements include maintaining a **GPA of 4.0** and contributing to several projects, including **REPP**, a **RAG-based platform** that was featured in the **Northeastern University Showcase** as a **poster presentation**.

---

### **My Research & Contributions**
Throughout my career, I have consistently blended **medical expertise** with **analytical skills**. As a **Research Assistant (April 2022–January 2023)**, I contributed to **public health studies**, including the **Government of Karnataka’s study on nutritional status and diabetes prevalence in urban slums**. My work not only **streamlined data collection processes** but also **improved data entry accuracy by 20%**. These experiences have **deepened my commitment** to leveraging **data to address real-world healthcare challenges**.

Additionally, I have collaborated in **cross-functional teams** as a **Pharma Regulatory Editor** at **Cactus Communications (October 2021–March 2022)**, ensuring **timely submission of critical documents** with a **95% on-time success rate**. My research contributions have been **recognized internationally**, including publications in esteemed journals like the **Australian & New Zealand Journal of Psychiatry** and **BMC Proceedings**.

---

### **Looking Ahead**
I am **excited** to explore opportunities in **Data Analysis and Machine Learning** that allow me to contribute to **impactful projects**. Whether it’s:

- **Analyzing financial data**
- **Integrating AI into the banking sector**
- **Solving healthcare challenges with AI**
- **Innovating new AI tools**

I am eager to bring my **unique blend of medical knowledge and data expertise** to **dynamic teams and forward-thinking organizations**.
""")

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
