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
st.markdown('<div class="header"><h1>Hello 👋</h1><h2>We are ALY6080 Group 1</h2></div>', unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.image("images/Photo for portfolio.jpeg", use_column_width=True, caption="Team Lead: Syed Faizan")

with col2:
    st.image("images/Christiana.jpeg", use_column_width=True, caption="Christiana")

with col3:
    st.image("images/Pravalika.jpeg", use_column_width=True, caption="Pravalika")

with col4:
    st.image("images/VrajShah.jpeg", use_column_width=True, caption="Vraj Shah")

with col5:
    st.image("images/Emelia.jpeg", use_column_width=True, caption="Emelia Doku")

with col6:
    st.image("images/Schicheng.jpeg", use_column_width=True, caption="Shicheng Wan")

    

st.markdown("<div class=\"header\"><h1>ALY 6080 Group Project's AI Bot</h1></div>", unsafe_allow_html=True)


# Persona details
persona = """ 
The report for United Way Greater Toronto (UWGT), led by Team Lead Syed Faizan, was developed by Group 1 ALY 6080 team members: Emelia Doku, Vraj Shah, Shicheng Wan, Pravalika Sorda, and Christiana Adjei. It aims to address socio-economic challenges in the Greater Toronto Area (GTA) through a data-driven approach, leveraging exploratory data analysis (EDA) and machine learning models to analyze trends and provide actionable insights.

The report investigates five critical domains: demographics, financial stability, housing stability, community services, and resident engagement. It draws from diverse data sources, including governmental and NGO reports, to ensure robust and accurate analyses. The findings aim to guide United Way in optimizing resource allocation and supporting vulnerable populations more effectively.

Key Findings and Insights:

Housing Stability: Eviction applications in Toronto CMA have declined, coupled with an increase in housing starts. These trends indicate gradual improvements in housing stability. However, affordability remains a significant concern, with variations across regions.

Financial Stability: The Gini Coefficient analysis reveals rising income inequality in Toronto City over decades. Predictive models indicate a further increase in income disparity. Additionally, regions like York and Peel exhibit persistently high low-income levels, highlighting the need for targeted interventions.

Living Wage Projections: Living wage requirements are projected to rise significantly, driven by increasing living costs. By 2040, York and Toronto are expected to have the highest living wage requirements, emphasizing the financial pressures on these regions.

Unemployment Trends: Observed and predicted unemployment rates demonstrate overall reductions in Toronto CMA and Peel Region. This suggests a positive trend in financial stability. However, disparities between regions necessitate customized employment policies.

Demographics and Social Equity: The GTA is experiencing a rapid growth in racialized populations, particularly South Asian, Chinese, and Black communities, expected to increase significantly by 2041. Toronto also hosts a higher concentration of recent immigrants. Educational attainment analysis reveals regional contrasts, with Halton showing a higher share of graduate degrees while Hamilton struggles with high school completion rates.

Income Inequality: The Low-Income Measure After Tax (LIMAT) data reveals younger age groups are disproportionately affected by poverty, particularly in Toronto and Hamilton. This emphasizes the need for youth-focused poverty alleviation strategies.

Actionable Recommendations: The report provides a roadmap for evidence-based policy-making and resource allocation. Recommendations include targeted interventions for high-need areas, policies addressing income inequality, and initiatives promoting affordable housing and living wages. Furthermore, fostering inclusivity and social cohesion through community engagement is highlighted as a cornerstone of long-term success.

Significance of the Study: This report highlights the interconnectedness of socio-economic indicators and their implications on quality of life. It provides UWGT with an analytical foundation to address systemic challenges and improve community outcomes. By leveraging predictive analytics and domain-specific insights, the study underscores the importance of adaptive strategies to combat inequality and support sustainable development across the GTA.

The authors have collectively contributed to creating a robust and detailed analysis that not only identifies critical challenges but also proposes impactful solutions. This collaborative effort embodies the spirit of teamwork and innovation, aiming to support UWGT in its mission to enhance community well-being and resilience.
"""

# User interaction section
st.markdown('<div class="section"><h3>Ask our report anything about the Group 1 ALY 6080 Group Project</h3>', unsafe_allow_html=True)
user_question = st.text_input("")
if st.button("ASK"):
    prompt = persona + "Here is the question that the user asked: " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)
st.markdown('</div>', unsafe_allow_html=True)

# About Me section
st.markdown('<div class="section"><h3>About Our ALY 6080 Group 1 Project Deliverables</h3>', unsafe_allow_html=True)
with open("images/ALY_6080_Experential_learning_Group_1_Module_12_Capstone_Sponsor_Deliverable.pdf", "rb") as file:
    st.download_button(
        label="Click here to download our ALY 6080 Capstone Project Report",
        data=file,
        file_name="ALY_6080_Experential_learning_Group_1_Module_12_Capstone_Sponsor_Deliverable.pdf",
        mime="application/pdf"
    )
st.write("- Our deliverables include an ArcGIS Dashboard and story for Geographic Information and demographic analysis, Power BI Dashboards, Jupyter Notebook and R files, a Github repository, a report and this app")
st.write("- Our Project focuses primarily on the demographics, housing stability and financial stability in the Toronto GTA and the interaction of these three domains")
st.write("- We have used Machine Learning predictive algorithms, Python and R for Exploratory Data Analysis, Latex for report formulation and, Github and Gemini API, HTML,CSS and streamlit for our app")
st.markdown('</div>', unsafe_allow_html=True)

# Contact Me section
st.markdown('<div class="section"><h3>Contact the Team Lead Syed Faizan</h3>', unsafe_allow_html=True)
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
