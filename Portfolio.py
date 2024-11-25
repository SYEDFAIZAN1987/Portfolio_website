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
You are 'ALY 6080 Group 1 Capstone Projects's AI bot" and serve as the online AI representative of Team Lead Syed Faizan, MD who leads the ALY 6080 Group 1. You help people answer questions about the capstone project report. 
Answer as if you are responding as Team Lead Syed Faizan. Always use 'I', 'me', and 'my' in your responses. Do not answer in the second or third person. 
If you don't know the answer to a question based on the information provided to you, simply say "The answer to your question is beyond the information that I possess". 
Here is the information about the ALY 6080 Group 1 Capstone Project:
Northeastern University

ALY 6080: Capstone Presentation and Sponsor Deliverable
Supervisor: Prof. Dr. Jay Qi, PhD

Exploration of Socio-economic Trends
in Toronto GTA with Data Analysis,
Visualization and Predictive Analytics

Authors: Syed Faizan, Emelia Doku, Vraj Shah, Shicheng Wan, Pravalika Sorda,
Christiana Adjei

November 25th, 2024

1

Contents
1

Introduction
Page 3

2

EDA : Demographics in Canada and the Greater Toronto
Area
Page 9

3

EDA: Financial Stability in the Greater Toronto Area
Page 51

4

EDA: Housing Stability in the Greater Toronto Area
Page 89

5

EDA: A Strong Community Services Sector: Exploration and
analysis of NGO’s in the Greater Toronto Area
Page 118

6

EDA: Engaged and Connected Residents
Page 135

2

7

Hypotheses testing and Predictive Analytics
Page 156

8

References
Page 187

3

Report
for
United Way Greater Toronto

4

Introduction
The purpose of this project is to develop a comprehensive data analysis and predictive
model that will provide actionable insights to United Way Greater Toronto (UWGT), a nongovernmental organization dedicated to addressing socio-economic challenges in the Greater
Toronto Area (GTA). The GTA faces significant poverty-related issues that affect a wide
range of residents, particularly vulnerable populations. To better coordinate and optimize
their programs, UWGT has identified five key domain areas where detailed insights and
evidence-based strategies are needed: Demographics, A Strong Community Services Sector,
Engaged and Connected Residents, Financial Stability, and Housing Stability. By leveraging
predictive modeling and machine learning techniques, this project aims to analyze these
critical areas to help UWGT make informed decisions, ultimately improving their ability to
alleviate poverty and foster greater financial and housing stability in the GTA.
The business problem that this project seeks to address revolves around improving the
efficiency and effectiveness of UWGT’s efforts to support vulnerable communities. Currently,
the organization is tasked with providing social services and financial support across a diverse
and growing population. However, the complexity of the socio-economic challenges in the
GTA makes it difficult to identify which areas and communities need immediate intervention
and what type of resources will yield the most substantial impact. This project will provide
UWGT with data-driven insights to address these gaps by creating predictive models that will
highlight key patterns and trends, helping the organization to proactively allocate resources
and implement targeted interventions.
The predictive models developed as part of this project yield specific forecasts that can
guide UWGT’s strategic planning. For instance, eviction applications in Toronto CMA are
projected to decline steadily, with applications decreasing from 21,267 in 2030 to 16,600 by
2050, indicating potential improvements in housing stability. Additionally, housing starts are
expected to rise from approximately 53,160 units in 2030 to 69,623 units by 2050, reflecting
an expansion in housing supply that could alleviate housing demand pressures in the region.
Unemployment rates in Toronto CMA, Ontario, and York Region are also predicted to trend
downward, suggesting improved employment prospects across the GTA. However, low-income

5
levels are anticipated to remain high in regions like York and Peel, underscoring the need
for targeted socio-economic policies in these areas. Furthermore, living wages are projected
to continue increasing in response to rising costs of living, with York Region and Toronto
projected to require the highest living wages by 2040.
These domain-specific predictions emphasize the interconnected nature of financial and
housing stability with other socio-economic indicators. The demographic analysis will provide further insights into the specific population groups at the highest risk of poverty, while
a strong community services sector will ensure the accessibility of necessary supports. Engaging and connecting residents remains essential for fostering social cohesion and collective
action in addressing poverty. By focusing on these domains, this project offers UWGT a
holistic framework for developing more efficient, sustainable, and impactful programs.
The analysis will be conducted using a combination of exploratory data analysis (EDA),
data visualization, and predictive modeling techniques. The primary goal is to identify
key variables—such as income, employment status, household size, housing costs, and demographic characteristics—that can serve as indicators of financial and housing instability.
Machine learning algorithms will be applied to these variables to develop models that predict
which communities and demographic groups are most at risk of poverty and housing instability. This will enable UWGT to make data-driven decisions that optimize their resource
allocation and program implementation, ensuring that they can make the greatest impact
with their available resources.
In summary, this project aims to equip UWGT with actionable insights that will enhance
their ability to coordinate poverty alleviation programs in the GTA. Through the use of
predictive modeling and data analysis, the project will provide a clear understanding of the
socio-economic dynamics affecting vulnerable populations, allowing UWGT to implement
targeted interventions that promote financial and housing stability.

6

A note on the sources
Before we venture to analyse the data we would do well to familiarize ourselves with the data
sources used for this report and the domains they were used in. This introduction to the
data sources serves not only to obviate the cumbersome and tedious repetition of citations
but also furnishes an upfront examination of the sources’ validity.
The sources used in this study provide a comprehensive view of factors influencing poverty,
homelessness, and related socio-economic issues in the Greater Toronto Area (GTA). These
references, drawn from governmental reports, research studies, and institutional surveys,
offer valuable insights into the various dimensions of inequality, housing, labor market dynamics, and socio-economic conditions faced by marginalized communities. This section
introduces the key sources and their relevance to the target variables and domains pertinent
to organizations like United Way Greater Toronto and other NGOs working to alleviate
poverty and advocate for the underserved.
The Study: Diverse Generations of Canadians by (Statistics Canada, 2022) offers an important demographic profile of racialized Canadians, serving as a foundational resource for
understanding the intersection of race and socio-economic outcomes, particularly in predicting racial disparities in income, housing, and employment. The data can be used to assess
target variables such as racial discrimination, income inequality, and access to essential services.
(Leon, 2020) provides a focused analysis on evictions, race, and poverty in Toronto,
highlighting the disproportionate impact on racialized and low-income communities. This
report can help inform predictive models aimed at identifying households at risk of eviction
and homelessness, and understanding how systemic factors perpetuate these cycles.
The Starts and Completions Survey Methodology by (Mortgage & Corporation, 2024)
offers housing market data that can be used to examine housing supply and demand trends,
predict future shortages, and understand their relationship with affordability and homelessness. This data can support models predicting housing market conditions and related
poverty risks.
The Affordable Housing Deficit report by (City of Toronto 2021: Affordable Housing

7
Deficit, 2021) discusses the challenges in affordable housing availability, which directly impacts the capacity to reduce homelessness in Toronto. This report can be leveraged to model
housing needs and predict which populations may be most affected by affordability issues.
The 2021 Street Needs Assessment Results by (City of Toronto 2021 Street Needs Assessment Results, 2021) provides direct insights into the demographics and needs of homeless
populations in Toronto. It can serve as a baseline for predicting homelessness trends and
understanding the demographics most at risk.
(Neighbourhood Change Research Partnership, 2020) discuss the widening gap in income
inequality, providing context for economic disparities in Toronto. The data is relevant for
models focusing on income inequality, labor market disparities, and predicting poverty levels
based on socio-economic indicators.
The 2021 Census Backgrounder by (City of Toronto, 2022) includes data on households,
marital status, and income distributions. It is useful for demographic modeling and understanding the socio-economic factors that influence poverty and housing insecurity.
(Lewis, de Wolff, King, Lopes, & Zon, 2020) highlight the relationship between income
inequality and opportunity access in Toronto. Their analysis can be utilized for models
predicting income mobility and the impact of socio-economic policies on poverty reduction.
(Calculating the Living Wage: Toronto 2019 , 2019) provide insights on living wage calculations, helping to benchmark income adequacy against local costs of living. This information is essential for analyzing the adequacy of current wage levels in lifting households
out of poverty.
The Calculation Archive by (Network, 2023) serves as a reference for tracking changes in
living wage requirements over time, which can be used to predict trends in income sufficiency
relative to inflation and cost-of-living adjustments.
The Local Labour Market Plan Report 2022 by (Workforce Planning Board of York Region, 2023) provides data on labor market conditions, which are essential for predicting
employment trends and understanding the impact of economic shifts on low-income households.
The Working Poor in the Toronto Region report by (Foundation, 2015) gives insights
into the distribution of the working poor across the region, highlighting trends and helping

8
identify areas for targeted interventions.
The 2024 State of the Sector - Policy Report by ((ONN), 2024) offers a contemporary
analysis of challenges faced by the nonprofit sector, providing insights into how NGOs can
adjust their strategies to address emerging needs in poverty alleviation.
Finally, (Statistics Canada, 2019) offer a portrait of Canadian society through the Canadian Social Survey, which provides essential data on social conditions, well-being, and public
trust, all of which can be used to understand broader socio-economic trends.
These sources collectively enable a holistic analysis of poverty, homelessness, unemployment, and racial disparities, equipping organizations like United Way Greater Toronto with
the evidence needed to allocate resources effectively, advocate for policy changes, and implement targeted interventions to alleviate socio-economic disparities in the GTA.

9

Demographics in Canada & the Greater Toronto Area:
The Present
And
The Future

10
The Toronto CMA (Census Metropolitan Area) refers to the region consisting of Toronto
and its surrounding municipalities, defined by Statistics Canada, which includes neighboring
cities that have a high degree of economic and social integration with Toronto. The GTA
(Greater Toronto Area) is a broader term, encompassing the City of Toronto and surrounding regions (Peel, York, Durham, and Halton), commonly used to describe the extended
metropolitan area. The GTA includes both urban and suburban communities and is a major economic hub in Canada. Our focus shall be primarily on the GTA in our analysis of the
5 domains of demographics, financial and housing stability,community service and engaged
and connected residents

Demographics
The 2021 population of Toronto is 2,794,356, which is 7.6% of Canada’s total population
of 36,991,981. (City of Toronto, 2022).
In our analysis of demographic data, we focused on several key target variables that are
essential for understanding socio-economic disparities and their impact on poverty, homelessness, and employment in the Greater Toronto Area. These variables include:
• Racial Discrimination: This variable captures experiences of discrimination based
on race or ethnicity. It is used to understand how racial disparities contribute to
socio-economic outcomes such as income inequality, employment barriers, and housing
instability.
• Income Levels: Income data helps to identify low-income households, track changes
in wage adequacy (e.g., living wage vs. minimum wage), and analyze the relationship
between income and access to housing and essential services.
• Employment Status: Employment-related variables, including unemployment rates,
job security, and type of employment, are used to model labor market trends and
predict poverty risks associated with precarious or low-wage work.

11
• Housing Affordability: This variable includes data on housing costs, availability of
affordable housing, and rates of homelessness. It helps to identify populations at risk
of housing insecurity and predict future trends in housing needs.
• Family and Household Composition: This demographic variable considers household size, marital status, and number of dependents. It is crucial for understanding
the economic pressures faced by different family types and the risk factors for poverty.
• Age Distribution: Age-related variables help to identify vulnerable age groups, such
as youth and elderly populations, who may face unique challenges in accessing employment, housing, and social services.
• Immigrant and Refugee Status: This variable looks at the socio-economic integration of immigrants and refugees, helping to assess the additional barriers faced by
newcomers in achieving economic stability.
• Educational Attainment: Education levels are used to analyze their correlation
with income potential, job opportunities, and social mobility.
These target variables collectively provide a multi-dimensional view of the demographic
factors influencing socio-economic outcomes in the Greater Toronto Area. By analyzing
these variables, predictive models can be developed to identify high-risk groups and design
targeted interventions for poverty alleviation.
Age
0-14
15-24
25-44
45-64
65+
85+
Total
Average Age

GTHA Toronto Rest of GTHA
1,143,360 384,300
759,130
904,130
320,460
583,670
2,078,110 890,370
1,187,480
1,956,395 722,250
1,234,450
1,199,660 476,990
722,670
160,980
71,860
89,120
7,281,725 2,794,370
4,487,355
41.5

Durham
Peel
York
Halton Hamilton
125,505
240,135
191,215 111,035
91,420
84,500
206,925
148,215
75,380
68,020
185,705
407,350
290,995 147,870
155,820
383,990
407,350
343,725 166,420
149,795
111,080
212,630
199,185
95,485
104,290
13,645
23,535
24,025
13,320
14,685
696,990 1,451,025 1,173,335 596,640
569,350
40.2
39.4
41.4
40.2
41.5

Table 1: Population Distribution by Age Group and Region in GTHA

12

Exploratory Data Analysis of Population Distribution
by Age Group and Region in GTHA
The data presented in Table 1 provides the population distribution across different age groups
and regions within the Greater Toronto and Hamilton Area (GTHA). The regions include
Toronto, the Rest of GTHA, Durham, Peel, York, Halton, and Hamilton. Each age group is
broken down into six categories: 0-14, 15-24, 25-44, 45-64, 65+, and 85+ years, along with
total population and the average age across the regions.

Data Description
The table contains the following information:
• Age groups: Population distribution across six age categories (0-14, 15-24, 25-44,
45-64, 65+, and 85+).
• Regions: The regions covered include GTHA, Toronto, the Rest of GTHA, Durham,
Peel, York, Halton, and Hamilton.
• Total Population: Summation of all age groups for each region.
• Average Age: The calculated average age of the population for each region.

Exploratory Data Analysis
1.

Five-Number Summary: The five-number summary includes the minimum, first

quartile (Q1), median, third quartile (Q3), and maximum values for the population across
different regions and age groups. Here is the five-number summary for the total population
data in each region:
• Minimum (Min): The smallest total population among the regions is for Durham,
with 696,990 people.
• First Quartile (Q1): The first quartile is around 1,199,660 (GTHA for the age group
65+), indicating that 25% of the regions have a total population below this value.

13
• Median: The median total population value is approximately 1,451,025 (Peel region),
representing the middle value of the dataset.
• Third Quartile (Q3): The third quartile is about 1,966,395 (GTHA for the age group
45-64), meaning 75% of the regions have a population below this value.
• Maximum (Max): The maximum total population recorded is for the entire GTHA,
with 7,281,725 people.
2. Measures of Central Tendency: The mean total population across the regions is
2,261,144. The average age for most regions lies between 39 and 42, with the GTHA average
being 41.5.
3. Distribution Analysis: The population distribution is skewed towards older age
groups (45-64 and 65+) in several regions, especially in the Rest of GTHA and York. The
age group 25-44 constitutes a significant portion of the population across all regions. There
is also a notable decline in population numbers as age increases from the 45-64 group to
85+.

Observations
• The GTHA, being the largest region, holds the highest population across all age groups.
• The age group 0-14 shows considerable variation in distribution across regions, indicating differences in birth rates or young population migration.
• There is a marked increase in the proportion of elderly populations (65+ and 85+) in
the Rest of GTHA and York compared to other regions.
• The regions of Peel, York, and Toronto exhibit a relatively high proportion of people
in the 25-44 and 45-64 age groups, suggesting a working-age population concentration.
• Durham and Hamilton have lower total populations, possibly due to smaller geographic
areas or differences in urbanization levels compared to other regions.

14

Conclusion
The population distribution across GTHA highlights significant demographic trends, with an
emphasis on the distribution of working-age individuals and increasing elderly populations
in certain areas. This demographic information is crucial for policy planning, especially
regarding healthcare, infrastructure, and social services.

Figure 1: Most youthful Neighborhoods in Toronto

Exploratory Data Analysis of Most Youthful Neighborhoods in Toronto
The data visualization displays the percentage distribution of children (0-14 years) and youth
(15-24 years) across various neighborhoods in Toronto. The neighborhoods are ranked based
on the proportion of these age groups, indicating areas with a higher concentration of younger
populations. The blue bars represent the percentage of children aged 0-14, while the pink
bars represent the percentage of youth aged 15-24.

Data Description
The chart includes the following neighborhoods:

15
• West Humber-Clairville
• Mount Olive-Silverstone-Jamestown
• Glenfield-Jane Heights
• Goldfield-Cedarbrae-Woburn
• West Hill
• Thorncliffe Park
• Clairlea-Birchmount
• Englemount-Lawrence
• Stonegate-Queensway
• Wexford/Maryvale
• Bay-Cloverhill
• York University Heights
• Morningside Heights
• Church-Wellesley
The analysis focuses on the percentages of children and youth in each neighborhood to
highlight the youthful demographic concentration.

Exploratory Data Analysis
1. Five-Number Summary for Children (0-14 years):
• Minimum (Min): The lowest percentage of children is in Church-Wellesley, at 15%.
• First Quartile (Q1): The first quartile value is 17%, indicating that 25% of the
neighborhoods have 17% or fewer children.

16
• Median: The median percentage of children across the neighborhoods is 19%, representing the middle value.
• Third Quartile (Q3): The third quartile value is 20%, suggesting that 75% of the
neighborhoods have 20% or fewer children.
• Maximum (Max): The highest percentage of children is found in Mount OliveSilverstone-Jamestown, at 24%.
2. Five-Number Summary for Youth (15-24 years):
• Minimum (Min): The lowest percentage of youth is in Morningside Heights, at 15%.
• First Quartile (Q1): The first quartile value is 16%, indicating that 25% of the
neighborhoods have 16% or fewer youth.
• Median: The median percentage of youth is 17%, indicating that half of the neighborhoods have 17% or fewer youth.
• Third Quartile (Q3): The third quartile value is 18%, suggesting that 75% of the
neighborhoods have 18% or fewer youth.
• Maximum (Max): The highest percentage of youth is found in West HumberClairville, at 28%.

Measures of Central Tendency and Dispersion
The mean percentage for both children (0-14) and youth (15-24) can be calculated as follows:
Mean for Children = 18.2%
Mean for Youth = 17.6%
The standard deviation for both groups provides insight into the dispersion of percentages
across neighborhoods.

17

Distribution Analysis
• There is a relatively even distribution of children across the neighborhoods, with most
percentages clustered around the median (19%).
• The youth distribution shows more variability, with a wider range from 15% to 28%,
suggesting certain neighborhoods have a notably higher youth concentration.
• West Humber-Clairville exhibits the highest combined concentration of children and
youth, indicating a particularly youthful demographic.
• Neighborhoods like Church-Wellesley, Morningside Heights, and Bay-Cloverhill have
lower percentages of children, suggesting a different demographic structure, potentially
with more young professionals or older residents.

Conclusion
The visualization highlights significant differences in the concentration of young populations
across Toronto neighborhoods. The data can inform urban planning, educational resource
allocation, and community services to cater to the needs of younger residents. Neighborhoods
with higher youth percentages may require additional recreational facilities, educational
support, and youth programs.

18

Figure 2: Neighborhoods with most seniors in Toronto

Exploratory Data Analysis of Neighborhoods with Most
Seniors in Toronto
The data visualization presents the percentage of seniors (65+ years) in the neighborhoods
of Toronto with the highest concentration of elderly residents. The neighborhoods included
in this analysis are Banbury-Don Mills, Agincourt North, Annex, Tam O’Shanter-Sullivan,
Milliken, and Steeles. The values represent the percentage of the population aged 65 or older
in each neighborhood.

Data Description
The chart lists the following neighborhoods along with the corresponding percentage of
seniors:
• Banbury-Don Mills: 30.4%
• Agincourt North: 28.7%
• Annex: 28.7%

19
• Tam O’Shanter-Sullivan: 27.9%
• Milliken: 27.8%
• Steeles: 27.8%

Exploratory Data Analysis
1. Five-Number Summary for the Percentage of Seniors:
• Minimum (Min): The lowest percentage of seniors is 27.8%, found in Milliken and
Steeles.
• First Quartile (Q1): The first quartile value is 27.8%, indicating that 25% of the
neighborhoods have 27.8% or fewer seniors.
• Median: The median percentage of seniors is 28.3%, which is the midpoint of the
dataset.
• Third Quartile (Q3): The third quartile value is 28.7%, suggesting that 75% of the
neighborhoods have 28.7% or fewer seniors.
• Maximum (Max): The highest percentage of seniors is 30.4%, found in BanburyDon Mills.
2. Measures of Central Tendency:
• Mean: The mean percentage of seniors across the neighborhoods can be calculated
as:
Mean = 28.72%
• Standard Deviation: The standard deviation measures the dispersion of the percentages:
Standard Deviation = 0.87

20

Distribution Analysis
• The distribution of senior percentages is relatively narrow, with all values falling within
a 2.6% range (27.8% to 30.4%), indicating that these neighborhoods have a consistently
high concentration of seniors.
• Banbury-Don Mills stands out with the highest proportion of seniors (30.4%), suggesting that it may have more amenities and services tailored for the elderly or could be
more attractive for senior living.
• The median and mean values are very close, suggesting a symmetric distribution of
the data without significant skewness.
• The low standard deviation (0.87) reflects a small variation in the percentage of seniors
across these neighborhoods, indicating a consistent senior population density among
the listed areas.

Conclusion
The visualization highlights Toronto neighborhoods with significant senior populations. The
relatively close range of percentages and low variability suggest these areas have a similar
demographic profile in terms of elderly residents. This information is valuable for urban
planning, healthcare resource allocation, and the development of age-appropriate services.

21

Figure 3: Education by Region

Exploratory Data Analysis of Education by Region
The data visualization displays the educational attainment across six regions in terms of
five categories: Graduate degree, High School, No Certificate, Post-Secondary Certificate,
and Bachelors Degree. The regions included are Toronto, Halton, York, Peel, Hamilton, and
Durham. The percentages represent the proportion of the population within each region
that has attained the respective education levels.

Data Description
The chart provides the following educational categories and their corresponding percentages
across the regions:
• Graduate Degree: Highest percentage in Halton (23.1%), lowest in Hamilton (10.7%).
• High School: Highest percentage in Hamilton (24.7%), lowest in Halton (18.3%).
• No Certificate: Highest percentage in Hamilton (10.4%), lowest in Halton (4.1%).
• Post-Secondary Certificate: Highest percentage in Durham (25.5%), lowest in Halton (19.9%).

22
• Bachelors Degree: Highest percentage in Hamilton (34.0%), lowest in York (26.5%).

Exploratory Data Analysis
1. Five-Number Summary for Each Educational Category:
• Graduate Degree:
– Min: 10.7% (Hamilton)
– Q1: 15.4%
– Median: 18.3%
– Q3: 19.9%
– Max: 23.1% (Halton)
• High School:
– Min: 15.8% (Halton)
– Q1: 19.0%
– Median: 19.9%
– Q3: 24.7%
– Max: 24.7% (Hamilton)
• No Certificate:
– Min: 4.1% (Halton)
– Q1: 7.1%
– Median: 8.6%
– Q3: 9.4%
– Max: 10.4% (Hamilton)
• Post-Secondary Certificate:
– Min: 19.9% (Halton)

23
– Q1: 22.4%
– Median: 24.7%
– Q3: 26.5%
– Max: 27.6% (York)
• Bachelors Degree:
– Min: 26.5% (York)
– Q1: 27.8%
– Median: 30.7%
– Q3: 32.2%
– Max: 34.0% (Hamilton)
2. Measures of Central Tendency and Dispersion:
• Mean:
– Graduate Degree: 17.9%
– High School: 20.5%
– No Certificate: 7.8%
– Post-Secondary Certificate: 24.4%
– Bachelors Degree: 30.3%
• Standard Deviation:
– Graduate Degree: 4.2
– High School: 3.3
– No Certificate: 2.2
– Post-Secondary Certificate: 2.6
– Bachelors Degree: 2.6

24

Distribution Analysis
• Graduate degree attainment is highest in Halton, with Hamilton having significantly
lower levels.
• High School completion rates are fairly consistent, with the highest concentration in
Hamilton.
• No Certificate rates are lowest in Halton, suggesting a higher level of education attainment.
• Post-Secondary Certificate rates vary across regions, with York showing the highest
levels.
• Bachelors Degree attainment shows the highest variability, indicating significant differences in educational attainment patterns among regions.

Conclusion
The visualization highlights the distribution of educational attainment across various regions,
showing significant differences in graduate and bachelor degree levels. These insights can
inform policy-making regarding education and workforce development.

Figure 4: Age of Immigrant Population

25

Exploratory Data Analysis of Age of Immigrant Population in 2016 and 2021
The data visualization presents the age distribution of the immigrant population in Toronto,
the Rest of the Greater Toronto Area (GTA), and Canada for the years 2016 and 2021. The
categories shown are: Over 25 in 2021, Under 25 in 2021, Over 25 in 2016, and Under 25 in
2016. The values represent the percentage of the immigrant population falling into each age
group for the respective years.

Data Description
The chart includes the following data:
• Toronto:
– Over 25 in 2021: 91%
– Under 25 in 2021: 9%
– Over 25 in 2016: 55%
– Under 25 in 2016: 45%
• Rest of GTA:
– Over 25 in 2021: 90%
– Under 25 in 2021: 10%
– Over 25 in 2016: 51%
– Under 25 in 2016: 49%
• Canada:
– Over 25 in 2021: 88%
– Under 25 in 2021: 12%
– Over 25 in 2016: 52%
– Under 25 in 2016: 48%

26

Exploratory Data Analysis
1. Five-Number Summary for Each Age Category:
• Over 25 in 2021:
– Min: 88% (Canada)
– Q1: 89%
– Median: 90%
– Q3: 90.5%
– Max: 91% (Toronto)
• Under 25 in 2021:
– Min: 9% (Toronto)
– Q1: 9.5%
– Median: 10%
– Q3: 11%
– Max: 12% (Canada)
• Over 25 in 2016:
– Min: 51% (Rest of GTA)
– Q1: 53%
– Median: 55%
– Q3: 53.5%
– Max: 55% (Toronto)
• Under 25 in 2016:
– Min: 45% (Toronto)
– Q1: 46.5%

27
– Median: 48%
– Q3: 48.5%
– Max: 49% (Rest of GTA)
2. Measures of Central Tendency and Dispersion:
• Mean:
– Over 25 in 2021: 89.67%
– Under 25 in 2021: 10.33%
– Over 25 in 2016: 52.67%
– Under 25 in 2016: 47.33%
• Standard Deviation:
– Over 25 in 2021: 1.53
– Under 25 in 2021: 1.53
– Over 25 in 2016: 2.08
– Under 25 in 2016: 2.08

Distribution Analysis
• The proportion of immigrants over 25 has increased substantially from 2016 to 2021
across all regions, with Toronto showing the highest increase.
• The percentage of immigrants under 25 has decreased over the same period, reflecting
an aging immigrant population or changes in immigration patterns.
• The distribution for the age group Over 25 in 2021 is relatively narrow, indicating
consistency across regions.
• The standard deviation values suggest minimal variability in the proportions for 2021,
while 2016 shows slightly more variation.

28

Conclusion
The data indicates a shift in the age structure of the immigrant population from 2016 to
2021, with an increase in the proportion of individuals over 25 years old. This trend may
have implications for social services, labor market integration, and policy planning.

Figure 5: General Make up of the immigrant population

Exploratory Data Analysis of Generational Make-Up of
Immigrant Populations
The data visualization presents the generational composition of immigrant populations across
different regions: Toronto, the Rest of the Greater Toronto and Hamilton Area (GTHA),
Ontario, and Canada. The categories shown are First Generation, Second Generation, and
Third Generation or More, with percentages indicating the proportion of the population in
each generational group within the specified regions.

29

Data Description
The chart includes the following data:
• Toronto:
– First Generation: 53%
– Second Generation: 27%
– Third Generation or More: 20%
• Rest of GTHA:
– First Generation: 45%
– Second Generation: 28%
– Third Generation or More: 27%
• Ontario:
– First Generation: 34%
– Second Generation: 24%
– Third Generation or More: 44%
• Canada:
– First Generation: 26%
– Second Generation: 18%
– Third Generation or More: 56%

Exploratory Data Analysis
1. Five-Number Summary for Each Generational Category:
• First Generation:
– Min: 26% (Canada)

30
– Q1: 30%
– Median: 39.5%
– Q3: 49%
– Max: 53% (Toronto)
• Second Generation:
– Min: 18% (Canada)
– Q1: 22.5%
– Median: 26%
– Q3: 27.5%
– Max: 28% (Rest of GTHA)
• Third Generation or More:
– Min: 20% (Toronto)
– Q1: 23.5%
– Median: 27%
– Q3: 44%
– Max: 56% (Canada)
2. Measures of Central Tendency and Dispersion:
• Mean:
– First Generation: 39.5%
– Second Generation: 24.25%
– Third Generation or More: 36.75%
• Standard Deviation:
– First Generation: 11.1
– Second Generation: 4.5
– Third Generation or More: 15.6

31

Distribution Analysis
• The proportion of First Generation immigrants is highest in Toronto (53%) and lowest
in Canada as a whole (26%), indicating a higher concentration of recent immigrants in
Toronto.
• Second Generation percentages show less variability across regions, with a narrow range
from 18% to 28%.
• The Third Generation or More group is most prominent in Canada (56%), highlighting
a longer history of immigration for many families outside major metropolitan areas.
• The standard deviation indicates that the Third Generation or More group has the
highest variability, reflecting significant differences across regions.

Conclusion
The visualization reveals different generational compositions of immigrant populations across
regions, with Toronto and the Rest of GTHA having higher percentages of First Generation
immigrants, while Canada as a whole has a larger proportion of Third Generation or More
immigrants. These patterns can influence cultural diversity, social policies, and immigration
strategies.

Figure 6: Projected Racialized population by 2041

32

Exploratory Data Analysis of Population Estimates and
Projections for Racialized populations in Canadian Cities
The data provided shows the estimated racialized population for Canadian cities in 2016 and
the projected population for the same cities in the future. The cities include major urban
centers across Canada, with the population figures given in thousands.

Data Description
The table includes the following columns:
• City: The name of the city.
• Estimated 2016: The estimated population in 2016 (in thousands).
• Projected: The projected future population (in thousands).
The data covers a range of cities, from large metropolitan areas like Toronto and Vancouver to smaller cities such as Belleville and Quinte.

Exploratory Data Analysis
1. Five-Number Summary for Estimated 2016 and Projected Populations:
• Estimated 2016:
– Min: 7 (Belleville)
– Q1: 13 (Lethbridge, Barrie)
– Median: 18 (Hamilton, Oshawa)
– Q3: 29 (Winnipeg, Ottawa-Gatineau Ontario part)
– Max: 51 (Toronto)
• Projected:
– Min: 10 (Quinte, St. John’s)

33
– Q1: 20 (Victoria, Saskatoon)
– Median: 30 (London, Ottawa-Gatineau Quebec part)
– Q3: 50 (Edmonton, Ottawa-Gatineau Ontario part)
– Max: 75 (Toronto)
2. Measures of Central Tendency and Dispersion:
• Mean:
– Estimated 2016: 21.9
– Projected: 33.2
• Standard Deviation:
– Estimated 2016: 10.7
– Projected: 16.5

Distribution Analysis
• The estimated population in 2016 shows a wider range among the smaller cities, with
a maximum value of 51 (Toronto) and a minimum value of 7 (Belleville).
• The projected values show significant growth in larger cities such as Toronto, Vancouver, and Calgary, indicating ongoing urbanization trends in these metropolitan areas.
• The median values suggest that half of the cities had an estimated 2016 population
below 18, while projections show a higher median of 30, indicating overall population
growth across the cities.
• The standard deviation indicates a higher variability in the projected values compared
to the 2016 estimates, suggesting increasing disparities in population growth across
different cities.

34

Conclusion
The analysis shows a trend of population growth in major Canadian cities, with larger cities
like Toronto and Vancouver projected to continue leading in population size. Smaller cities
also show growth, but at a slower pace compared to larger urban centers.

Figure 7: Projected Percentage of Racialized Population

Exploratory Data Analysis of Projected Percentage of
Racialized Populations in the GTA in 2041
The data visualization presents the projected percentage of various racialized groups in the
Greater Toronto Area (GTA) for the year 2041, compared to their percentage in 2016. The
racialized groups include South Asian, Chinese, Filipino, Black, and other groups. The
percentages represent the proportion of the total population made up by each group in the
respective years.

Data Description
The chart includes the following racialized groups and their percentages of the population
in 2016 and projected percentages for 2041:

35
• South Asian: 2.6% (2016), 6.0% (2041)
• Chinese: 1.8% (2016), 3.5% (2041)
• Filipino: 1.4% (2016), 2.5% (2041)
• Black: 1.2% (2016), 3.0% (2041)
• Other racialized groups: 1.2% (2016), 2.0% (2041)
• Arab: 1.0% (2016), 2.0% (2041)
• Latin American: 0.8% (2016), 2.0% (2041)
• Southeast Asian: 0.6% (2016), 1.0% (2041)
• West Asian: 0.6% (2016), 1.5% (2041)
• Korean: 0.4% (2016), 0.7% (2041)
• Japanese: 0.3% (2016), 0.4% (2041)

Exploratory Data Analysis
1. Five-Number Summary for 2016 and 2041 Percentages:
• 2016 Percentages:
– Min: 0.3% (Japanese)
– Q1: 0.6% (Southeast Asian, West Asian)
– Median: 1.0% (Arab)
– Q3: 1.4% (Filipino)
– Max: 2.6% (South Asian)
• 2041 Percentages:
– Min: 0.4% (Japanese)

36
– Q1: 1.0% (Southeast Asian)
– Median: 2.0% (Latin American, Arab)
– Q3: 2.5% (Filipino)
– Max: 6.0% (South Asian)
2. Measures of Central Tendency and Dispersion:
• Mean:
– 2016: 1.0%
– 2041: 2.3%
• Standard Deviation:
– 2016: 0.7
– 2041: 1.4

Distribution Analysis
• The data indicates a significant projected increase in the percentages of all racialized
groups by 2041, with South Asian, Chinese, and Black populations expected to see the
largest growth.
• The range of percentages widens from 2016 to 2041, indicating a more diverse racial
composition projected for the GTA.
• The median percentages for 2041 suggest a general upward shift in the representation
of racialized groups, particularly those previously underrepresented.
• The increase in standard deviation from 0.7 to 1.4 reflects a greater variability in the
projected percentages, highlighting larger differences in population growth rates among
the groups.

37

Conclusion
The analysis suggests a trend towards increased diversity in the GTA by 2041, with notable
growth in the representation of South Asian, Chinese, and Black populations. This demographic shift may have implications for social, economic, and cultural policies within the
region.
Visible Minority Group Toronto Percentage
South Asian
14
Chinese
10.7
Black
9.6
Filipino
6.2
Latin American
3.3
West Asian
2.5
Southeast Asian
2
Korean
1.5
Arab
1.5
Japanese
0.3
Other visible minority
1.5
Multiple visible minority
2.3

Rest of GTA Percentage Canada Percentage
19.7
7.1
9.1
4.7
6.4
3.5
3
2.9
1.8
1.6
2.3
1.1
1.3
1
0.8
0.8
2.4
1
0.2
0.3
0.5
0.5
0.9
0.9

Table 2: Visible Minority Group Percentages in Toronto, Rest of GTA, and Canada

Exploratory Data Analysis of Visible Minority Group
Percentages in Toronto, Rest of GTA, and Canada
The data presented in Table 2 shows the percentage distribution of various visible minority
groups in Toronto, the Rest of the Greater Toronto Area (GTA), and Canada. The table
provides an overview of the representation of these groups across different regions.

Data Description
The table includes the following columns:
• Visible Minority Group: The specific minority group being measured.
• Toronto Percentage: The percentage of the group in the Toronto population.

38
• Rest of GTA Percentage: The percentage of the group in the Rest of GTA population.
• Canada Percentage: The percentage of the group in the Canadian population.
The visible minority groups included are South Asian, Chinese, Black, Filipino, Latin
American, West Asian, Southeast Asian, Korean, Arab, Japanese, Other visible minority,
and Multiple visible minority.

Exploratory Data Analysis
1. Five-Number Summary for Each Region:
• Toronto Percentage:
– Min: 0.3% (Japanese)
– Q1: 1.5% (Korean, Arab, Other visible minority)
– Median: 3.3% (Latin American)
– Q3: 9.6% (Black)
– Max: 14% (South Asian)
• Rest of GTA Percentage:
– Min: 0.5% (Other visible minority)
– Q1: 1.3% (Southeast Asian)
– Median: 2.4% (Arab)
– Q3: 6.4% (Black)
– Max: 19.7% (South Asian)
• Canada Percentage:
– Min: 0.3% (Japanese)
– Q1: 0.8% (Korean)

39
– Median: 1.6% (Latin American)
– Q3: 3.5% (Black)
– Max: 7.1% (South Asian)
2. Measures of Central Tendency and Dispersion:
• Mean:
– Toronto: 4.6%
– Rest of GTA: 4.2%
– Canada: 2.3%
• Standard Deviation:
– Toronto: 4.0
– Rest of GTA: 5.3
– Canada: 2.2

Distribution Analysis
• The data shows that South Asians have the highest representation across all regions,
with Toronto showing 14%, the Rest of GTA 19.7%, and Canada 7.1%.
• Japanese populations have the lowest representation in all regions, consistently showing
the minimum value.
• The median values indicate higher diversity in Toronto compared to the national level,
as more minority groups exceed the national median.
• The standard deviation is highest in the Rest of GTA, indicating more variability in
the percentage distribution across different minority groups compared to Toronto and
Canada.

40

Conclusion
The analysis highlights the distribution of visible minority groups across different regions,
showing significant variation in their representation. The data indicates a more diverse
population in Toronto and the Rest of GTA compared to the national average, suggesting
regional differences in demographic composition.
Age Total Population Number Total Population Percent Men Number Men Percent Women Number Women Percent
0-4
123550
4.4
63380
4.7
60170
4.2
5-9
129040
4.6
66350
4.9
62690
4.3
10-14
131710
4.7
67665
5.0
64040
4.5
15-19
134810
4.8
69135
5.1
65675
4.5
20-24
185650
6.6
93940
6.9
91915
6.4
25-29
243955
8.7
121370
9.0
122585
8.5
30-34
246785
8.8
122845
8.9
123935
8.6
35-39
213810
7.7
105070
7.8
108740
7.5
40-44
185820
6.6
88905
6.6
96910
6.6
45-49
175875
6.3
82600
6.3
93275
6.7
50-54
184060
6.6
87130
6.5
96925
6.7
55-59
191380
6.8
92710
6.9
98665
6.7
60-64
170935
6.1
81960
6.1
88970
6.2
65-69
141550
5.1
65525
4.9
76025
5.4
70-74
118910
4.3
53985
3.9
64930
4.3
75-79
81880
2.9
36035
2.7
45850
3.2
80-84
62790
2.2
26000
2.2
36785
2.5
85-90
42430
1.5
16995
1.3
25435
1.8
90-94
22155
0.8
7545
0.6
14610
1.0
95-99
6400
0.2
195
0.1
4675
0.1
100+
875
0.0
0
0.0
680
0.0

Table 3: Age and Population Breakdown

Exploratory Data Analysis of Age and Population Breakdown
Table 3 provides a detailed breakdown of the population across different age groups in the
Toronto GTA, along with the number and percentage of men and women in each group. The
table includes the total population count and percentage for each age range, as well as the
corresponding breakdown for men and women.

Data Description
The table includes the following columns:
• Age: The age range of the population.

41
• Total Population Number: The total number of people in the given age group.
• Total Population Percent: The percentage of the total population represented by
the age group.
• Men Number: The number of men in the given age group.
• Men Percent: The percentage of men within the total male population.
• Women Number: The number of women in the given age group.
• Women Percent: The percentage of women within the total female population.

Exploratory Data Analysis
1.

Five-Number Summary for Total Population Percent, Men Percent, and

Women Percent:
• Total Population Percent:
– Min: 0.1% (100+)
– Q1: 1.5% (85-89)
– Median: 4.6% (5-9)
– Q3: 6.7% (45-49)
– Max: 8.1% (25-29)
• Men Percent:
– Min: 0.1% (100+)
– Q1: 1.4% (80-84)
– Median: 4.7% (10-14)
– Q3: 6.5% (45-49)
– Max: 8.4% (25-29)

42
• Women Percent:
– Min: 0.1% (100+)
– Q1: 1.7% (85-89)
– Median: 4.2% (0-4)
– Q3: 6.7% (50-54)
– Max: 7.6% (30-34)
2. Measures of Central Tendency and Dispersion:
• Mean:
– Total Population Percent: 4.3%
– Men Percent: 4.1%
– Women Percent: 4.4%
• Standard Deviation:
– Total Population Percent: 2.0
– Men Percent: 2.1
– Women Percent: 1.8

Distribution Analysis
• The age group with the highest representation in the total population is 25-29, with
8.1%, followed by 30-34 at 7.8%. This suggests a relatively younger demographic.
• The percentages for men and women are generally close across most age groups, indicating balanced gender distribution. However, there is a higher representation of
women in older age groups (75+), likely due to higher life expectancy among women.
• The lower variability in the Women’s Percent compared to Men Percent suggests a
more uniform distribution across different age groups for women.

43

Conclusion
The data reveals a relatively young population with a significant concentration in the 25-34
age range. The distribution becomes more uniform as age increases, with a higher proportion
of women in the older age groups. These demographic insights are valuable for policy-making,
healthcare planning, and social services.
Age
Percent Change 2006-2011 Percent Change 2011-2016 Percent Change 2016-2021
0-4
4.10%
-3.20%
-9.20%
5 to 9
-4.10%
5.40%
-4.40%
10 to 14
-6.20%
-3.90%
3.60%
15-19
2.60%
-3.00%
-7.40%
20-24
6.40%
6.10%
-4.70%
25-29
11.40%
10.00%
4.70%
30-34
2.80%
11.60%
9.90%
35-39
-6.20%
3.10%
8.90%
40-44
-7.10%
-7.60%
1.90%
45-49
7.00%
-8.00%
-7.90%
50-54
13.60%
5.80%
-9.10%
55-59
9.70%
12.50%
4.70%
60-64
28.80%
9.20%
11.10%
65-69
9.20%
27.40%
8.40%
70-74
1.20%
8.60%
27.00%
75-79
0.90%
2.60%
7.50%
80-84
5.60%
1.70%
3.60%
85-90
31.50%
10.50%
4.00%
90-94
20.30%
41.80%
12.60%
95-99
12.20%
30.90%
34.70%
100+
12.60%
43.90%
13.60%

Table 4: Age and Percent Changes (2006-2021)

Exploratory Data Analysis of Age and Percent Changes
(2006-2021) in the Toronto GTA
Table 4 provides the percentage changes in the population across different age groups in the
Greater Toronto Area (GTA) over three time periods: 2006-2011, 2011-2016, and 2016-2021.
These values indicate the growth or decline in the population for each age group during these
periods.

44

Data Description
The table includes the following columns:
• Age: The age range of the population.
• Percent Change 2006-2011: The percentage change in the population for the age
group from 2006 to 2011.
• Percent Change 2011-2016: The percentage change in the population for the age
group from 2011 to 2016.
• Percent Change 2016-2021: The percentage change in the population for the age
group from 2016 to 2021.

Exploratory Data Analysis
1. Five-Number Summary for Each Time Period:
• Percent Change 2006-2011:
– Min: -7.10% (40-44)
– Q1: 0.90% (75-79)
– Median: 4.10% (0-4)
– Q3: 12.20% (95-99)
– Max: 31.50% (85-89)
• Percent Change 2011-2016:
– Min: -8.60% (45-49)
– Q1: -3.30% (15-19)
– Median: 5.80% (50-54)
– Q3: 27.40% (65-69)
– Max: 41.80% (90-94)

45
• Percent Change 2016-2021:
– Min: -9.20% (0-4)
– Q1: -4.70% (25-29)
– Median: 3.60% (10-14)
– Q3: 12.60% (80-84)
– Max: 34.70% (95-99)
2. Measures of Central Tendency and Dispersion:
• Mean:
– Percent Change 2006-2011: 5.4%
– Percent Change 2011-2016: 7.5%
– Percent Change 2016-2021: 4.6%
• Standard Deviation:
– Percent Change 2006-2011: 10.2
– Percent Change 2011-2016: 15.6
– Percent Change 2016-2021: 12.4

Distribution Analysis
• The percentage change from 2006-2011 shows relatively moderate growth across most
age groups, with the highest growth seen in the 85-89 age group.
• The 2011-2016 period has greater variability, including some substantial negative changes
(e.g., -8.60% for the 45-49 age group) and significant growth in older age groups, indicating an aging population.
• The 2016-2021 period shows a mix of growth and decline across age groups, with the
youngest age group (0-4) experiencing the largest decline, while the oldest age groups
continue to see substantial increases.

46
• The higher standard deviation for 2011-2016 indicates more variability in the percentage changes compared to the other two periods, suggesting more dynamic demographic
shifts during that time.

Conclusion
The analysis reveals demographic trends in the GTA characterized by an aging population,
with consistent growth in older age groups and declines in younger age groups in recent
years. These trends may impact policy areas such as healthcare, education, and social
services planning.
Age Group
Estimated 2016 (%) Projected 2041 (%)
0 to 14 years
25
40
15 to 64 years
22
35
65 years and older
20
30
All ages
22
40
Table 5: Racialized Population Estimates and Projections by Age Group (2016 vs. 2041)

Exploratory Data Analysis of Racialized Population Estimates and Projections by Age Group (2016 vs. 2041)
Table 5 presents the percentage estimates of racialized populations across different age groups
in 2016, along with the projected percentages for 2041. The data is segmented by three age
groups: 0 to 14 years, 15 to 64 years, and 65 years and older. An additional category for the
total racialized population across all age groups is also provided.

Data Description
The table includes the following columns:
• Age Group: The age range of the population.
• Estimated 2016 (%): The estimated percentage of the racialized population in 2016
for each age group.

47
• Projected 2041 (%): The projected percentage of the racialized population in 2041
for each age group.

Exploratory Data Analysis
1. Five-Number Summary for 2016 and 2041 Percentages:
• Estimated 2016 (%):
– Min: 20% (65 years and older)
– Q1: 21.5% (All ages)
– Median: 22% (15 to 64 years)
– Q3: 23.5% (0 to 14 years)
– Max: 25% (0 to 14 years)
• Projected 2041 (%):
– Min: 30% (65 years and older)
– Q1: 32.5% (15 to 64 years)
– Median: 35% (15 to 64 years)
– Q3: 37.5% (0 to 14 years)
– Max: 40% (0 to 14 years, All ages)
2. Measures of Central Tendency and Dispersion:
• Mean:
– Estimated 2016: 22.3%
– Projected 2041: 35.0%
• Standard Deviation:
– Estimated 2016: 1.9
– Projected 2041: 4.3

48

Distribution Analysis
• The data shows a significant projected increase in the percentage of racialized populations across all age groups from 2016 to 2041.
• The highest growth is expected in the 0 to 14 years age group, with a 15% increase
from 25% in 2016 to 40% in 2041, indicating a trend toward a more diverse younger
population.
• The lower variability in the 2016 estimates compared to the 2041 projections suggests
that the diversity of the population is expected to increase across all age groups.
• The higher standard deviation in the projected 2041 values reflects greater disparity
in the distribution of racialized populations across different age groups in the future.

Conclusion
The analysis indicates a growing racialized population in the GTA, with the most significant
changes anticipated in younger age groups by 2041. These demographic shifts may influence
various aspects of social planning, including education, healthcare, and cultural services.
Visible Minority Group Montreal (%) Toronto (%)
South Asian
5
14
Black
30
12
Chinese
18
11
Filipino
7
7
Arab
3
8
Latin American
3
2
West Asian
2
3
Southeast Asian
2
1
Korean
1
0
Japanese
1
0
Other racial minority
1
1

Vancouver (%) Canada (%)
12
12
2
7
20
11
6
6
5
4
3
3
2
2
3
3
2
1
1
1
1
2

Table 6: Visible Minority Groups by Percentage in Different Canadian Cities

49

Exploratory Data Analysis of Visible Minority Groups
by Percentage in Different Canadian Cities
Table 6 presents the percentages of various visible minority groups in four Canadian cities:
Montreal, Toronto, Vancouver, and the overall population of Canada. The visible minority
groups included in the table are South Asian, Black, Chinese, Filipino, Arab, Latin American,
West Asian, Southeast Asian, Korean, Japanese, and Other racial minority.

Data Description
The table contains the following columns:
• Visible Minority Group: The specific minority group being measured.
• Montreal (%): The percentage of each minority group in the population of Montreal.
• Toronto (%): The percentage of each minority group in the population of Toronto.
• Vancouver (%): The percentage of each minority group in the population of Vancouver.
• Canada (%): The percentage of each minority group in the overall population of
Canada.

Exploratory Data Analysis
1. Five-Number Summary for Each City:
• Montreal (%):
– Min: 1% (Japanese, Other racial minority, Korean)
– Q1: 2% (Latin American, Southeast Asian, West Asian)
– Median: 3% (Arab)
– Q3: 7% (Filipino)

50
– Max: 30% (Black)
• Toronto (%):
– Min: 0% (Japanese)
– Q1: 3% (Latin American, West Asian)
– Median: 7% (Filipino)
– Q3: 12% (Black)
– Max: 14% (South Asian)
• Vancouver (%):
– Min: 1% (West Asian, Korean, Japanese, Other racial minority)
– Q1: 2% (Black)
– Median: 5% (Filipino)
– Q3: 12% (South Asian)
– Max: 20% (Chinese)
• Canada (%):
– Min: 1% (Japanese, Korean, West Asian)
– Q1: 1.5% (Southeast Asian, Latin American)
– Median: 3% (Arab)
– Q3: 7% (Black)
– Max: 12% (South Asian, Vancouver)
2. Measures of Central Tendency and Dispersion:
• Mean:
– Montreal: 6.1%
– Toronto: 5.6%

51
– Vancouver: 5.7%
– Canada: 3.8%
• Standard Deviation:
– Montreal: 8.3
– Toronto: 4.9
– Vancouver: 6.6
– Canada: 3.3

Distribution Analysis
• The data shows considerable variation in the distribution of visible minority groups
across different cities, with Montreal having a higher concentration of Black populations
(30%) compared to other cities.
• Toronto exhibits a more balanced distribution, with South Asians having the highest
representation (14%) and several other groups falling within the 3%-7% range.
• Vancouver is characterized by a high concentration of Chinese (20%) and South Asian
(12%) populations, reflecting significant Asian representation in the city.
• The lower mean and standard deviation for Canada suggest less variability in minority
group percentages across the country compared to individual cities.

Conclusion
The analysis highlights the differences in the demographic composition of visible minority
groups in various Canadian cities, with certain groups having significantly higher representation in specific urban centers. These findings may inform policies related to multiculturalism,
social integration, and resource allocation.

52

Financial stability
In our analysis of financial stability, we selected target variables that capture the economic
conditions impacting poverty, homelessness, and employment in the Greater Toronto Area.
These variables include:
• Income Levels: This variable is essential for measuring economic stability and assessing the adequacy of wages in relation to the cost of living. It includes categories
such as low-income, middle-income, and high-income households.
• Living Wage vs. Minimum Wage: This variable captures the differences between
living wages (wages needed to meet basic living standards) and minimum wages, helping to evaluate wage adequacy and predict poverty risk.
• Employment Stability: This includes data on job security, full-time versus parttime work, and unemployment rates. It helps in identifying populations vulnerable to
income instability and economic insecurity.
• Housing Costs: Variables such as rent, mortgage payments, and housing affordability
are used to assess financial burdens related to housing, which can contribute to poverty
and homelessness.
These target variables provide a comprehensive view of financial stability factors in the
Greater Toronto Area, offering insights into the economic challenges faced by vulnerable
populations. By analyzing these variables, we can develop predictive models to identify
individuals and households at risk of financial instability and design effective interventions.

53

Figure 8: Gini Coefficient in the Toronto CMA Regions

Gini Coefficient and Exploratory Data Analysis of the
Toronto CMA Regions
Understanding the Gini Coefficient
The Gini Coefficient is a measure of inequality in a distribution, commonly used to assess
income or wealth inequality. It ranges from 0 to 1, where 0 represents perfect equality
(everyone has the same income), and 1 represents perfect inequality (one person has all the
income). In this context, higher Gini values indicate higher levels of income inequality within
a region.

Data Description
The data visualization shows the Gini Coefficient trends from 1970 to 2010 across various
regions in the Toronto Census Metropolitan Area (CMA), including Toronto City, Durham,
Halton, Peel, York, and the entire Toronto CMA. The values for each region are plotted over
time, illustrating changes in income inequality.

54

Exploratory Data Analysis
1. Five-Number Summary for Each Region (2010 Values):
• Toronto City:
– Min: 0.130 (1970)
– Q1: 0.140 (1980)
– Median: 0.160 (1990)
– Q3: 0.200 (2000)
– Max: 0.310 (2010)
• Durham:
– Min: 0.100 (1970)
– Q1: 0.120 (1980)
– Median: 0.130 (1990)
– Q3: 0.140 (2000)
– Max: 0.140 (2010)
• Halton:
– Min: 0.110 (1970)
– Q1: 0.130 (1980)
– Median: 0.150 (1990)
– Q3: 0.180 (2000)
– Max: 0.210 (2010)
• Peel:
– Min: 0.110 (1970)
– Q1: 0.130 (1980)

55
– Median: 0.140 (1990)
– Q3: 0.160 (2000)
– Max: 0.140 (2010)
• York:
– Min: 0.100 (1970)
– Q1: 0.120 (1980)
– Median: 0.130 (1990)
– Q3: 0.180 (2000)
– Max: 0.180 (2010)
• Toronto CMA:
– Min: 0.100 (1970)
– Q1: 0.120 (1980)
– Median: 0.140 (1990)
– Q3: 0.180 (2000)
– Max: 0.200 (2010)
2. Measures of Central Tendency and Dispersion:
• Mean (2010 Values):
– Toronto City: 0.190
– Durham: 0.130
– Halton: 0.160
– Peel: 0.140
– York: 0.140
– Toronto CMA: 0.160

56
• Standard Deviation (2010 Values):
– Toronto City: 0.070
– Durham: 0.015
– Halton: 0.040
– Peel: 0.015
– York: 0.030
– Toronto CMA: 0.040

Distribution Analysis
• The Gini Coefficient for Toronto City shows a consistent increase over time, indicating
growing income inequality. The highest value of 0.310 in 2010 suggests significant
inequality.
• Durham and Peel exhibit lower Gini values, with minimal changes over the years,
suggesting relatively stable levels of income distribution.
• Halton and York show moderate increases in their Gini values, reflecting rising inequality, although at a slower rate compared to Toronto City.
• The overall Toronto CMA follows a trend of increasing inequality, with Gini values
rising from 0.100 in 1970 to 0.200 in 2010.
• The variability in Gini values across regions is highest in Toronto City, as reflected by
the larger standard deviation.

Conclusion
The analysis demonstrates increasing income inequality in the Toronto CMA, particularly in
Toronto City, where the Gini Coefficient has risen significantly over the decades. The trends
suggest the need for targeted policies to address rising inequality and its associated social
implications.

57

Figure 9: LIMAT by Age and Council in GTA

Exploratory Data Analysis of Low-Income Measure, After Tax (LIMAT) by Age and Council in GTA
Understanding LIMAT
The Low-Income Measure, After Tax (LIMAT) is a widely used metric to assess poverty
levels. It defines individuals or households as low-income if their after-tax income is less
than half of the median after-tax income for all households. It provides a relative measure
of income inequality by identifying individuals with incomes significantly below the typical
standard of living.

Data Description
The visualization shows the LIMAT population distribution across age groups in different
regions of the Greater Toronto Area (GTA), specifically Hamilton, Toronto, Peel, Durham,
York, and Halton. The age groups are broken down into the following categories:
• Under 6 years of Age
• 6 to 18 years

58
• 18 to 24 years
• 25 to 54 years
• 55 to 64 years
• 65 years and above

Exploratory Data Analysis
1. Five-Number Summary for Each Region (Percentage Values by Age Group):
• Hamilton:
– Min: 11% (55 to 64 years)
– Q1: 13% (65 years and above)
– Median: 15% (18 to 24 years)
– Q3: 16% (25 to 54 years)
– Max: 17% (Under 6 years of age)
• Toronto:
– Min: 11% (55 to 64 years)
– Q1: 13% (65 years and above)
– Median: 16% (25 to 54 years)
– Q3: 17% (Under 6 years of age)
– Max: 18% (6 to 18 years)
• Peel:
– Min: 10% (55 to 64 years)
– Q1: 13% (65 years and above)
– Median: 14% (Under 6 years of age)

59
– Q3: 14% (25 to 54 years)
– Max: 16% (6 to 18 years)
• Durham:
– Min: 8% (55 to 64 years)
– Q1: 9% (65 years and above)
– Median: 10% (18 to 24 years)
– Q3: 13% (Under 6 years of age)
– Max: 14% (25 to 54 years)
• York:
– Min: 8% (55 to 64 years)
– Q1: 9% (65 years and above)
– Median: 10% (18 to 24 years)
– Q3: 13% (Under 6 years of age)
– Max: 14% (25 to 54 years)
• Halton:
– Min: 7% (55 to 64 years)
– Q1: 8% (6 to 18 years)
– Median: 9% (25 to 54 years)
– Q3: 10% (Under 6 years of age)
– Max: 11% (65 years and above)
2. Measures of Central Tendency and Dispersion:
• Mean:
– Hamilton: 14.5%

60
– Toronto: 14.7%
– Peel: 13.5%
– Durham: 10.7%
– York: 10.7%
– Halton: 9.0%
• Standard Deviation:
– Hamilton: 2.1
– Toronto: 2.2
– Peel: 2.0
– Durham: 2.1
– York: 2.1
– Halton: 1.5

Distribution Analysis
• The distribution across age groups shows a higher concentration of LIMAT populations among younger individuals (under 6 years and 6 to 18 years) in most regions,
particularly in Toronto and Hamilton.
• In regions like Halton, the percentage distribution is more balanced, with relatively
lower values across all age groups compared to other regions.
• The standard deviation values suggest more variability in LIMAT populations in Toronto,
Hamilton, and Peel, while Halton shows the lowest variability, indicating a more uniform distribution of LIMAT populations.

Conclusion
The data reflects the age-based distribution of the LIMAT population across the GTA,
indicating higher levels of income inequality affecting younger age groups in certain regions.

61
These findings may inform policy decisions aimed at addressing poverty and supporting
vulnerable populations.

Figure 10: Toronto City Income Level

Exploratory Data Analysis of Toronto City Income Levels from 1970 to 2015
Data Description
The data visualization shows the distribution of income levels in Toronto City over the years
1970, 1980, 1990, 2000, 2010, and 2015. The income levels are divided into three categories:
• High or Very High Income
• Middle Income
• Low or Very Low Income
The chart displays the percentage distribution of each income level for the given years,
indicating changes in the economic profile of the city over time.

62

Exploratory Data Analysis
1. Five-Number Summary for Each Income Level Over Time:
• High or Very High Income:
– Min: 10% (1970)
– Q1: 14% (1990)
– Median: 18% (2000)
– Q3: 22% (2010)
– Max: 25% (2015)
• Middle Income:
– Min: 40% (2015)
– Q1: 45% (2010)
– Median: 55% (2000)
– Q3: 60% (1990)
– Max: 65% (1970)
• Low or Very Low Income:
– Min: 20% (1970)
– Q1: 25% (1980)
– Median: 30% (1990)
– Q3: 35% (2000)
– Max: 40% (2015)
2. Measures of Central Tendency and Dispersion:
• Mean:
– High or Very High Income: 17.5%

63
– Middle Income: 53.3%
– Low or Very Low Income: 30.0%
• Standard Deviation:
– High or Very High Income: 5.2
– Middle Income: 9.1
– Low or Very Low Income: 7.4

Distribution Analysis
• The data reveals a declining trend in the percentage of Middle Income households from
1970 to 2015, indicating a shrinking middle class over the years.
• There is a noticeable increase in the percentage of Low or Very Low Income households,
especially from 2000 onwards, suggesting rising income inequality in the city.
• The proportion of High or Very High Income households shows a steady increase over
time, indicating a growing affluent segment in the population.
• The standard deviation for Middle Income is the highest, reflecting significant changes
in the distribution of this income level over the years.

Conclusion
The analysis shows a clear shift in the income distribution of Toronto City, with a decreasing middle-income population and increasing segments of both high-income and low-income
households. This trend suggests a polarization in the city’s economic profile, with implications for social equity and policy interventions.

64

Figure 11: York Income Levels

Exploratory Data Analysis of York Income Levels from
1970 to 2015
Data Description
The data visualization presents the income level distribution in York from 1970 to 2015,
categorized into three income groups:
• High or Very High Income
• Middle Income
• Low or Very Low Income
The chart depicts the percentage share of households in each income group over the given
years, providing insights into how income distribution has shifted in the region.

Exploratory Data Analysis
1. Five-Number Summary for Each Income Level Over Time:
• High or Very High Income:

65
– Min: 2% (1970)
– Q1: 5% (1980)
– Median: 8% (1990)
– Q3: 12% (2010)
– Max: 14% (2015)
• Middle Income:
– Min: 15% (2015)
– Q1: 20% (2010)
– Median: 25% (2000)
– Q3: 30% (1990)
– Max: 80% (1970)
• Low or Very Low Income:
– Min: 5% (1970)
– Q1: 10% (1980)
– Median: 15% (1990)
– Q3: 20% (2000)
– Max: 25% (2015)
2. Measures of Central Tendency and Dispersion:
• Mean:
– High or Very High Income: 8.5%
– Middle Income: 34.2%
– Low or Very Low Income: 15.0%
• Standard Deviation:

66
– High or Very High Income: 4.5
– Middle Income: 22.1
– Low or Very Low Income: 6.7

Distribution Analysis
• The data reveals a dramatic decline in Middle Income households, dropping from 80%
in 1970 to 15% in 2015. This suggests a significant reduction in the proportion of
households considered middle class.
• The proportion of High or Very High Income households has steadily increased over
time, reaching 14% in 2015.
• Low or Very Low Income households have shown a gradual upward trend, indicating
increasing income inequality in the region.
• The high standard deviation for Middle Income highlights significant variability and
changes in this group’s distribution over the decades.

Conclusion
The analysis indicates a major shift in income distribution in York from 1970 to 2015, with a
notable decrease in the middle-income population and an increase in both higher and lower
income groups. This trend suggests increasing economic disparity in the region.

67

Figure 12: Income levels in Peel

Exploratory Data Analysis of Peel Income Levels from
1970 to 2015
Data Description
The visualization illustrates the income level distribution in Peel from 1970 to 2015, divided
into three categories:
• Low or Very Low Income
• Middle Income
• High or Very High Income
The percentages represent the share of households in each income category over the years,
showing shifts in income distribution across the decades.

Exploratory Data Analysis
1. Five-Number Summary for Each Income Level Over Time:
• Low or Very Low Income:

68
– Min: 5% (1970, 1990, 2000, 2015)
– Q1: 5% (2000)
– Median: 5% (2015)
– Q3: 10% (1980)
– Max: 20% (2010)
• Middle Income:
– Min: 44% (2015)
– Q1: 52% (2010)
– Median: 65% (2010)
– Q3: 75% (2000)
– Max: 85% (1970, 1980)
• High or Very High Income:
– Min: 5% (1970, 1980, 1990, 2000, 2010)
– Q1: 5% (1990)
– Median: 5% (2000)
– Q3: 10% (1980)
– Max: 15% (2015)
2. Measures of Central Tendency and Dispersion:
• Mean:
– Low or Very Low Income: 8.3%
– Middle Income: 70.3%
– High or Very High Income: 7.5%
• Standard Deviation:

69
– Low or Very Low Income: 5.8
– Middle Income: 14.3
– High or Very High Income: 3.7

Distribution Analysis
• The data indicates a gradual decline in Middle Income households from 85% in 1970
to 44% in 2015, suggesting a shrinking middle class over the years.
• The percentage of Low or Very Low Income households has increased notably, especially
in 2010, where it reached 20%, indicating a rise in economic inequality.
• High or Very High Income levels remain relatively stable, maintaining around 5% from
1970 to 2000 before increasing to 15% in 2015.
• The high standard deviation for Middle Income reflects substantial variability over the
years, while Low or Very Low Income has also shown significant changes.

Conclusion
The analysis reveals a shifting income distribution in Peel, characterized by a shrinking
middle-income population and growing segments of both low-income and high-income households. These trends suggest increasing economic polarization in the region.

70

Figure 13: Government Transfer by Region

Exploratory Data Analysis of Government Transfer as
Percent of Budget by Region
Data Description
The visualization illustrates the percentage of government transfer as a portion of the overall
budget for various regions, including Hamilton, Peel, Canada (as a whole), Ontario, Durham,
Toronto, York, and Halton. The government transfer represents financial assistance from the
government, typically in the form of grants, subsidies, or other forms of funding. The data
indicates the reliance of different regions on government support as part of their budgetary
allocations.

Exploratory Data Analysis
1. Five-Number Summary for Government Transfer as Percent of Budget:
• Minimum: 11.30% (Halton)
• First Quartile (Q1): 15.50% (Toronto, York)
• Median: 16.80% (Durham)

71
• Third Quartile (Q3): 17.80% (Canada)
• Maximum: 18.70% (Hamilton)
2. Measures of Central Tendency and Dispersion:
• Mean: 16.24%
• Standard Deviation: 2.31

Distribution Analysis
• The data reveals that Hamilton has the highest percentage of government transfer as
a part of its budget at 18.70%, indicating a relatively higher reliance on government
funding compared to other regions.
• Halton shows the lowest percentage of government transfer, at 11.30%, suggesting less
dependence on government support.
• The median value is 16.80%, with Durham having a government transfer percentage
that closely aligns with this central tendency.
• The standard deviation of 2.31 indicates moderate variability in the distribution of
government transfer percentages across the regions.

Conclusion
The analysis demonstrates variability in the reliance on government transfers across different
regions, with Hamilton and Peel having higher percentages, while regions like Halton have
lower levels of government support as a portion of their budget. These differences may
reflect variations in regional economic conditions, social policies, and the availability of local
revenue sources.

72

Figure 14: Unemployment Rates compared

Exploratory Data Analysis of Unemployment Rate in
Ontario, Rest of Ontario, and Toronto CMA from 2018
to 2023
Data Description
The visualization shows the unemployment rate trends in Ontario as a whole, the Rest of
Ontario (excluding Toronto CMA), and the Toronto CMA from 2018 to 2023. The data
illustrates the fluctuations in unemployment across these regions over the six-year period,
highlighting the impact of events such as the COVID-19 pandemic in 2020, which resulted
in a significant increase in unemployment rates.

Exploratory Data Analysis
1. Five-Number Summary for Each Region:
• Ontario (Overall):
– Min: 5.2% (2019)

73
– Q1: 5.6% (2018)
– Median: 7.2% (2021)
– Q3: 8.7% (2020)
– Max: 9.8% (2020)
• Rest of Ontario (excluding Toronto CMA):
– Min: 4.9% (2023)
– Q1: 5.3% (2018)
– Median: 7.0% (2021)
– Q3: 8.1% (2020)
– Max: 9.3% (2020)
• Toronto CMA:
– Min: 5.1% (2023)
– Q1: 5.5% (2018)
– Median: 8.1% (2021)
– Q3: 9.8% (2020)
– Max: 10.0% (2020)
2. Measures of Central Tendency and Dispersion:
• Mean:
– Ontario (Overall): 7.3%
– Rest of Ontario: 6.7%
– Toronto CMA: 7.7%
• Standard Deviation:
– Ontario (Overall): 1.6
– Rest of Ontario: 1.6
– Toronto CMA: 1.8

74

Distribution Analysis
• The data shows a sharp increase in unemployment across all regions in 2020 due to the
COVID-19 pandemic, with the highest unemployment rate observed in Toronto CMA
(10.0%).
• Following 2020, the unemployment rates decreased gradually, with Rest of Ontario
reaching the lowest rate of 4.9% in 2023.
• The unemployment rate in Toronto CMA remains higher than in the Rest of Ontario
throughout most of the observed period, reflecting potentially higher economic challenges in urban areas during recovery.
• The standard deviation is highest for Toronto CMA, indicating greater variability in
unemployment trends compared to the other regions.

Conclusion
The analysis highlights the substantial impact of the COVID-19 pandemic on unemployment rates in Ontario, with Toronto CMA experiencing the highest levels of unemployment.
While recovery has been observed, the variability in unemployment trends suggests ongoing
challenges, particularly in metropolitan areas.

75

Figure 15: Unemployment Rate in Peel.

Exploratory Data Analysis of Unemployment Rate in
Peel (2020–2023)
Data Description
The visualization presents the unemployment rate trends across different regions in Peel,
including Brampton, Halton, Mississauga, and Toronto CMA as a whole, from the first
quarter of 2020 to the first quarter of 2023. The data shows quarterly unemployment rates
over this period, illustrating how the rates have fluctuated in response to economic conditions,
including the recovery from the COVID-19 pandemic.

Exploratory Data Analysis
1. Five-Number Summary for Each Region:
• Brampton:

76
– Min: 3.8% (Q1 2023)
– Q1: 5.1% (Q3 2022)
– Median: 6.4% (Q2 2022)
– Q3: 7.1% (Q4 2020)
– Max: 8.3% (Q2 2021)
• Halton:
– Min: 3.9% (Q1 2023)
– Q1: 5.5% (Q4 2022)
– Median: 6.3% (Q4 2021)
– Q3: 7.2% (Q2 2021)
– Max: 8.7% (Q3 2020)
• Mississauga:
– Min: 4.3% (Q1 2023)
– Q1: 5.7% (Q4 2022)
– Median: 6.6% (Q4 2021)
– Q3: 7.5% (Q2 2021)
– Max: 7.6% (Q2 2021)
• Toronto CMA:
– Min: 5.1% (Q4 2022)
– Q1: 5.5% (Q1 2023)
– Median: 6.0% (Q2 2022)
– Q3: 6.6% (Q2 2021)
– Max: 7.3% (Q3 2020)
2. Measures of Central Tendency and Dispersion:

77
• Mean:
– Brampton: 6.0%
– Halton: 6.4%
– Mississauga: 6.5%
– Toronto CMA: 6.1%
• Standard Deviation:
– Brampton: 1.4
– Halton: 1.6
– Mississauga: 1.1
– Toronto CMA: 0.8

Distribution Analysis
• The data shows a general decline in unemployment rates across all regions from mid2020 to early 2023, reflecting economic recovery post-pandemic.
• Halton exhibited the most variability, with a peak unemployment rate of 8.7% in Q3
2020 and a low of 3.9% in Q1 2023.
• The lowest standard deviation for Toronto CMA indicates that the unemployment rate
was relatively stable in comparison to other regions.
• There is a trend of convergence in unemployment rates across regions in recent quarters,
with all rates approaching 4%–5% by Q1 2023.

Conclusion
The analysis highlights the initial economic shock in 2020 followed by a steady decline in
unemployment rates in Peel’s regions. The variability across regions reflects different local
economic conditions and recovery patterns.

78

Figure 16: Unemployment Rate in York

Exploratory Data Analysis of Unemployment Rate in
York (2021)
Data Description
The visualization displays the monthly unemployment rate trends for York Region, Toronto
CMA, and Ontario as a whole throughout 2021. It shows how unemployment rates fluctuated
across these regions over the course of the year, with higher rates at the beginning due to
ongoing economic challenges and gradual decreases as the year progressed.

Exploratory Data Analysis
1. Five-Number Summary for Each Region:
• York Region:
– Min: 5.9% (December)
– Q1: 6.7% (July)
– Median: 7.3% (April)

79
– Q3: 8.5% (February)
– Max: 12.0% (January)
• Toronto CMA:
– Min: 6.2% (December)
– Q1: 6.9% (August)
– Median: 7.5% (May)
– Q3: 8.2% (March)
– Max: 13.1% (January)
• Ontario (Overall):
– Min: 6.0% (December)
– Q1: 6.5% (August)
– Median: 7.2% (April)
– Q3: 8.0% (February)
– Max: 15.6% (January)
2. Measures of Central Tendency and Dispersion:
• Mean:
– York Region: 7.5%
– Toronto CMA: 8.1%
– Ontario (Overall): 8.3%
• Standard Deviation:
– York Region: 1.7
– Toronto CMA: 2.0
– Ontario (Overall): 3.0

80

Distribution Analysis
• The data shows a sharp decrease in unemployment rates across all regions from January
to December, reflecting economic recovery in 2021.
• Ontario had the highest variability in unemployment rates, as indicated by the larger
standard deviation, reaching a peak of 15.6% in January before decreasing to 6.0% in
December.
• Toronto CMA exhibited higher unemployment rates than York Region throughout most
of the year, indicating potentially greater economic challenges in the metropolitan area.
• The convergence of unemployment rates by the end of the year (December) suggests
stabilization across the regions.

Conclusion
The analysis highlights a significant decrease in unemployment rates in York, Toronto CMA,
and Ontario during 2021, with Ontario experiencing the most significant reduction. The
variability in unemployment trends reflects different recovery patterns across regions, with
Toronto CMA and Ontario showing higher rates of unemployment than York Region.

81

Figure 17: Working Poor in the Toronto CMA

Exploratory Data Analysis of Working Poor by Region
in the Toronto CMA
Data Description
The visualization shows the number of working poor across various regions within the Toronto
Census Metropolitan Area (CMA), including Halton, Peel, Scarborough, Toronto City, and
York. The term ”working poor” refers to individuals who are employed but earn incomes
that fall below the poverty line, highlighting economic disparity despite employment.

Exploratory Data Analysis
1. Five-Number Summary for Working Poor by Region:
• Minimum: 32.5k (Scarborough)
• First Quartile (Q1): 34.3k (Halton)
• Median: 80.6k (Peel)

82
• Third Quartile (Q3): 81.4k (York)
• Maximum: 104k (Toronto City)
2. Measures of Central Tendency and Dispersion:
• Mean: 66.5k
• Standard Deviation: 30.6k

Distribution Analysis
• The number of working poor is highest in Toronto City, with 104k individuals, indicating a higher concentration of economically disadvantaged workers despite employment.
• Scarborough has the lowest number of working poor at 32.5k, suggesting relatively
lower levels of economic hardship in comparison to other regions within the Toronto
CMA.
• The median value is 80.6k, reflecting the distribution’s central tendency, with Peel and
York having figures close to this median.
• The standard deviation of 30.6k indicates considerable variability in the number of
working poor across different regions.
• There is a substantial gap between the highest and lowest values, pointing to regional
economic disparities within the Toronto CMA.

Conclusion
The analysis highlights significant differences in the distribution of the working poor across
regions in the Toronto CMA, with Toronto City having the largest concentration and Scarborough the smallest. The high standard deviation further indicates substantial variation,
suggesting uneven economic conditions across these regions.

83
Region
Toronto
Peel Region
Durham
Halton
York

Living Wage 2020 Living Wage 2021 Minimum Wage 2020 Minimum Wage 2021
22.08
23.15
14.35
15
19.80
23.15
14.35
15
17.80
19.05
14.35
15
20.75
23.15
14.35
15
25.00
25.05
14.35
15

Table 7: Comparison of Living and Minimum Wages across Different Regions

Exploratory Data Analysis of Living and Minimum Wages
across Different Regions
Data Description
The table provides a comparison of living wages and minimum wages across different regions
(Toronto, Peel Region, Durham, Halton, and York) for the years 2020 and 2021. The living
wage is defined as the hourly wage required for workers to meet basic living expenses, while
the minimum wage is the legally mandated lowest hourly wage that employers must pay.
This comparison highlights the gap between living wages and minimum wages in each region
over time.

Exploratory Data Analysis
1. Five-Number Summary for Living Wage (2020 and 2021):
• Living Wage 2020:
– Min: 17.80 (Durham)
– Q1: 19.80 (Peel Region)
– Median: 20.75 (Halton)
– Q3: 22.08 (Toronto)
– Max: 25.00 (York)
• Living Wage 2021:

84
– Min: 19.05 (Durham)
– Q1: 23.15 (Peel Region, Halton, Toronto)
– Median: 23.15 (Peel Region, Halton, Toronto)
– Q3: 23.15 (Peel Region, Halton, Toronto)
– Max: 25.05 (York)
2. Five-Number Summary for Minimum Wage (2020 and 2021):
• Minimum Wage 2020:
– Min: 14.35 (all regions)
– Q1: 14.35 (all regions)
– Median: 14.35 (all regions)
– Q3: 14.35 (all regions)
– Max: 14.35 (all regions)
• Minimum Wage 2021:
– Min: 15.00 (all regions)
– Q1: 15.00 (all regions)
– Median: 15.00 (all regions)
– Q3: 15.00 (all regions)
– Max: 15.00 (all regions)
3. Measures of Central Tendency and Dispersion:
• Mean:
– Living Wage 2020: 21.49
– Living Wage 2021: 22.91
– Minimum Wage 2020: 14.35

85
– Minimum Wage 2021: 15.00
• Standard Deviation:
– Living Wage 2020: 2.56
– Living Wage 2021: 2.26
– Minimum Wage 2020: 0.00
– Minimum Wage 2021: 0.00

Distribution Analysis
• The living wage shows variability across regions, with York consistently having the
highest living wage, indicating a higher cost of living in this region.
• The minimum wage is uniform across all regions for both years, indicating no regional
differentiation in the legislated minimum wage.
• The living wage increased in all regions from 2020 to 2021, with the most significant
change in Durham, reflecting an increase in living expenses.
• The standard deviation for the living wage decreased from 2020 to 2021, suggesting a
slight convergence in living wage requirements across regions.

Conclusion
The analysis highlights a significant gap between living wages and minimum wages, indicating
that the minimum wage is not sufficient to meet the basic living expenses in any of the regions.
The increase in the living wage from 2020 to 2021 reflects rising costs of living, particularly
in regions like Durham and York.
Category
Total
0 to 17 years
0 to 5 years
18 to 64 years
65 years and over

Population In low income (LIM-AT) Prevalence of low income (%)
2,761,285
363,955
13.2
461,810
67,725
14.7
148,485
22,175
14.9
1,842,580
218,825
11.9
456,895
77,410
16.9

Table 8: Population and Low Income Prevalence Based on LIM-AT

86

Exploratory Data Analysis of Population and Low Income Prevalence Based on LIM-AT
Data Description
The table provides information on the population distribution and the prevalence of low
income based on the Low-Income Measure After Tax (LIM-AT) for different age categories.
The LIM-AT is a widely used indicator of low income, representing the proportion of individuals whose after-tax income falls below half of the median income of the population. The
data includes total population, the number of individuals in low income, and the prevalence
of low income as a percentage for various age groups.

Exploratory Data Analysis
1. Five-Number Summary for Prevalence of Low Income (%):
• Minimum: 11.9% (18 to 64 years)
• First Quartile (Q1): 13.2% (Total)
• Median: 14.7% (0 to 17 years)
• Third Quartile (Q3): 14.9% (0 to 5 years)
• Maximum: 16.9% (65 years and over)
2. Measures of Central Tendency and Dispersion:
• Mean: 14.32%
• Standard Deviation: 1.89%

Distribution Analysis
• The prevalence of low income is highest among individuals aged 65 years and over
(16.9%), indicating that seniors face higher levels of economic vulnerability.

87
• The lowest prevalence is observed in the 18 to 64 years age group (11.9%), suggesting
that the working-age population is relatively less affected by low income.
• There is a slight increase in the prevalence of low income for children (0 to 5 years)
compared to the overall population, with a value of 14.9%.
• The standard deviation of 1.89% indicates moderate variability in low income prevalence across different age groups.
• The median value of 14.7% for the 0 to 17 years age group shows that children have a
higher than average likelihood of experiencing low income.

Conclusion
The analysis highlights that seniors (65 years and over) are the most affected by low income,
with the highest prevalence among all age groups. Children also face higher low income
prevalence than the overall population, pointing to potential economic challenges for families
with young children. The working-age group (18 to 64 years) experiences the lowest levels
of low income, suggesting a relative economic advantage.
CMA
Windsor, ON
St. Catharines - Niagara, ON
Calgary, AB
Toronto, ON
Greater Sudbury, ON
Saint John, NB
Brantford, ON
Kelowna, BC
Saguenay, QC
Ottawa-Gatineau, QC
Sherbrooke, QC
Trois-Rivières, QC
Lethbridge, AB
Québec, QC
Victoria, BC

Unemployment Rate
10.6
10.5
9.6
9.3
8.7
8.7
5.7
5.7
5.5
5.5
5.2
5.0
4.2
4.2
4.2

Table 9: Unemployment Rates by CMA

88

Exploratory Data Analysis of Unemployment Rates by
CMA
Data Description
The table provides the unemployment rates for various Census Metropolitan Areas (CMAs)
across Canada. The unemployment rate represents the percentage of the labor force that
is without work but actively seeking employment. This data allows for the comparison of
economic conditions across different regions.

Exploratory Data Analysis
1. Five-Number Summary for Unemployment Rates:
• Minimum: 4.2% (Lethbridge, QC; Québec, QC; Victoria, BC)
• First Quartile (Q1): 5.2% (Sherbrooke, QC)
• Median: 5.7% (Brantford, ON; Kelowna, BC)
• Third Quartile (Q3): 8.7% (Greater Sudbury, ON; Saint John, NB)
• Maximum: 10.6% (Windsor, ON)
2. Measures of Central Tendency and Dispersion:
• Mean: 6.56%
• Standard Deviation: 2.17%

Distribution Analysis
• The unemployment rates vary significantly across the CMAs, with the highest rate
recorded in Windsor, ON (10.6%), and the lowest rates observed in Lethbridge, QC;
Québec, QC; and Victoria, BC (4.2%).

89
• The first quartile value of 5.2% suggests that a quarter of the CMAs have relatively
low unemployment rates below this threshold.
• The median value of 5.7% indicates that half of the regions have unemployment rates
above this level, while the other half fall below it.
• The third quartile value of 8.7% highlights that 25% of the regions have unemployment
rates higher than this, indicating higher levels of economic distress in certain areas.
• The standard deviation of 2.17% shows a moderate degree of variability in unemployment rates across the different CMAs.

Conclusion
The analysis shows considerable disparities in unemployment rates across the CMAs, reflecting varying economic conditions. While some regions like Windsor and St. Catharines Niagara exhibit higher levels of unemployment, others such as Victoria, Québec, and Lethbridge demonstrate lower rates, indicating a more favorable economic situation.

90

Housing stability
In our analysis of housing stability, we focused on target variables that capture factors
influencing housing security, affordability, and homelessness in the Greater Toronto Area.
These variables include:
• Housing Affordability: This variable measures the percentage of income spent on
housing costs (e.g., rent or mortgage payments). It is a key indicator for identifying
households at risk of housing instability and potential homelessness.
• Eviction Rates: Data on eviction occurrences, notices, and legal disputes related to
housing provide insights into trends that may indicate rising risks of displacement and
housing insecurity.
• Homelessness Rates: This variable captures the number of individuals experiencing
homelessness, including sheltered and unsheltered populations. It is used to monitor
changes in housing stability and the effectiveness of interventions.
These target variables collectively provide a detailed understanding of housing stability in
the Greater Toronto Area. By analyzing these variables, predictive models can be developed
to identify high-risk groups, forecast future trends in housing insecurity, and inform policy
recommendations aimed at improving housing stability.

Figure 18: Core Housing Need in Toronto CMA

91

Exploratory Data Analysis of Population Living in Core
Housing Need in the Toronto CMA
Data Description
The visualization presents the distribution of households in the Toronto Census Metropolitan Area (CMA) experiencing core housing need, categorized by income levels. The income
groups include Very Low Income (¡= $425), Low Income ($426 - $1,063), Moderate Income
($1,064 - $1,700), Median Income ($1,701 - $2,550), and High Income (¿= $2,551). Core
housing need is defined as households whose housing is inadequate, unaffordable, or unsuitable, and who cannot afford alternative suitable housing.

Exploratory Data Analysis
1. Five-Number Summary for Percentage of Households in Core Housing Need:
• Minimum: 5% (High Income)
• First Quartile (Q1): 10% (Median Income)
• Median: 20% (Very Low Income)
• Third Quartile (Q3): 30% (Moderate Income)
• Maximum: 65% (Low Income)
2. Measures of Central Tendency and Dispersion:
• Mean: 26%
• Standard Deviation: 21.13%

Distribution Analysis
• The proportion of households experiencing core housing need is highest among those
in the Low Income group, with 65% of such households facing housing challenges. This
indicates a significant disparity in housing accessibility for lower-income households.

92
• The proportion is lowest among the High Income group at 5%, demonstrating that
higher income levels are associated with lower instances of core housing need.
• The median value of 20% corresponds to the Very Low Income group, suggesting that
about half of the groups have more than 20% of households in core housing need.
• The standard deviation of 21.13% indicates a high degree of variability in the proportion of households in core housing need across different income groups.
• The skewness of the data towards higher percentages for lower income groups suggests
that core housing need disproportionately affects those with lower incomes.

Conclusion
The analysis reveals a stark contrast in core housing need across income levels, with lowerincome households being far more likely to experience housing challenges. This suggests that
income is a critical determinant of housing adequacy and affordability, and policy interventions may be needed to address housing accessibility for low-income groups.

Figure 19: Housing situation of Evicted Persons in Toronto CMA

93

Exploratory Data Analysis of Housing Situation of Evicted
Persons in the Toronto CMA
Data Description
The visualization provides information on the housing situation of individuals who have experienced eviction in the Toronto Census Metropolitan Area (CMA). The categories included
are:
• Experienced homelessness
• Living in social and affordable housing
• Renters
• Not living in social and affordable housing
• Never experienced homelessness
• Homeowners
The data reflects the percentage distribution of individuals falling into each housing situation
category.

Exploratory Data Analysis
1. Five-Number Summary for the Percentage Distribution:
• Minimum: 5.19% (Homeowners)
• First Quartile (Q1): 7.79% (Never experienced homelessness)
• Median: 12.99% (Not living in social and affordable housing)
• Third Quartile (Q3): 19.48% (Living in social and affordable housing)
• Maximum: 38.96% (Experienced homelessness)

94
2. Measures of Central Tendency and Dispersion:
• Mean: 16.67%
• Standard Deviation: 10.78%

Distribution Analysis
• The category with the highest proportion of individuals is ”Experienced homelessness,”
accounting for 38.96%, indicating a significant issue of homelessness among evicted
individuals.
• The smallest group is ”Homeowners,” at 5.19%, suggesting that few evicted persons
own their homes.
• The median percentage of 12.99% indicates that half of the categories have more than
12.99% representation, while the other half fall below this value.
• The first quartile (7.79%) and third quartile (19.48%) indicate a moderate spread of
the middle 50% of the data.
• The standard deviation of 10.78% reflects a considerable variability in the distribution
of housing situations among evicted individuals.

Conclusion
The data highlights that a significant portion of evicted individuals in the Toronto CMA have
experienced homelessness, pointing to the critical need for targeted interventions in housing
support services. Meanwhile, the relatively low percentages in categories like ”Homeowners”
suggest that eviction affects renters and those in temporary or subsidized housing disproportionately.

95

Figure 20: Eviction Applications by Year in Toronto CMA

Exploratory Data Analysis of Eviction Applications by
Year in Toronto CMA
Data Description
The visualization depicts the number of eviction applications in the Toronto Census Metropolitan Area (CMA) from 2010 to 2018. The trend shows fluctuations in the annual number
of eviction applications, with peaks and troughs throughout the period. The values on the
y-axis represent the number of eviction applications, while the x-axis indicates the years.

Exploratory Data Analysis
1. Five-Number Summary for the Number of Eviction Applications:
• Minimum: 23,000 (2018)
• First Quartile (Q1): 24,000 (2015)
• Median: 25,000 (2016)
• Third Quartile (Q3): 26,800 (2011)

96
• Maximum: 28,000 (2013)
2. Measures of Central Tendency and Dispersion:
• Mean: 25,475
• Standard Deviation: 1,748

Distribution Analysis
• The number of eviction applications shows an upward trend from 2010, peaking at
28,000 in 2013. This indicates an increase in housing instability during the early
2010s.
• After 2013, there is a noticeable decline, reaching 24,000 in 2015. The number of
applications rises again to 25,000 in 2016 before gradually decreasing to the lowest
level of 23,000 in 2018.
• The median number of eviction applications is 25,000, with 50% of the data points
above and below this value.
• The interquartile range (IQR), calculated as Q3 - Q1, is 2,800, suggesting moderate
variability in the middle 50% of the data.
• The standard deviation of 1,748 indicates some fluctuation in the number of eviction
applications over the years, with a more pronounced peak in 2013.

Conclusion
The analysis highlights a peak in eviction applications around 2013, followed by a downward
trend, suggesting a reduction in eviction rates in the latter half of the decade. The data
indicates housing policies or economic conditions that may have influenced these trends.

97

Figure 21: Evictions by Demographic Groups

Exploratory Data Analysis of Eviction Percentage by
Demographic Group in Toronto CMA
Data Description
The visualization displays the distribution of evicted individuals by demographic group
within the Toronto Census Metropolitan Area (CMA). The demographic groups included
are Métis, Indigenous, First Nations (on reserve), Black, Filipino, Non-Indigenous, individuals not part of a visible minority, South Asian, Chinese, and Arab.

Exploratory Data Analysis
1. Five-Number Summary for the Percentage of Evicted Individuals:
• Minimum: 2.74% (Arab)
• First Quartile (Q1): 6.85% (Non-Indigenous)
• Median: 9.59% (Multiple groups: Filipino, Not a visible minority, South Asian)

98
• Third Quartile (Q3): 13.7% (Chinese)
• Maximum: 19.18% (Métis)
2. Measures of Central Tendency and Dispersion:
• Mean: 10.8%
• Standard Deviation: 4.88%

Distribution Analysis
• The largest group of evicted individuals are the Métis, accounting for 19.18% of the
total evictions, followed closely by Indigenous individuals at 17.81%.
• The smallest group in terms of eviction percentage is the Arab demographic, which
accounts for only 2.74% of the evicted population.
• There is a significant concentration of groups around the median value of 9.59%, suggesting a clustering of multiple demographic groups at this level.
• The interquartile range (IQR), calculated as Q3 - Q1, is 6.85%, indicating moderate
variability in the eviction percentages across different demographic groups.
• The standard deviation of 4.88% reflects some degree of dispersion from the mean
eviction rate, showing that certain groups face disproportionate eviction risks.

Conclusion
The analysis reveals significant variation in eviction percentages among different demographic
groups. While some groups, such as Métis and Indigenous individuals, face higher eviction
rates, others like Arabs and Chinese face comparatively lower eviction risks. The data
indicates that eviction may disproportionately affect certain ethnic groups, necessitating
targeted policy interventions to address housing instability.

99

Figure 22: The Racialized identity of the homeless in Toronto CMA

Exploratory Data Analysis of Homelessness by Racialized Group in Toronto CMA
Data Description
The visualization provides the percentage distribution of homelessness among various racialized groups within the Toronto Census Metropolitan Area (CMA). The racialized groups
included in the data are Black-African, Black-Afro-Caribbean or Afro-Latinx, First Nations
(with or without status), Métis or Inuit, Black-Canadian/American, South Asian or IndoCaribbean, Latin American, South East Asian, Arab, East Asian, West Asian, and Other
(Black-Africa-European).

Exploratory Data Analysis
1. Five-Number Summary for the Percentage of Homeless Individuals:
• Minimum: 0% (Other: Black-Africa-European)
• First Quartile (Q1): 2% (East Asian, West Asian, Arab)
• Median: 4% (Latin American)
• Third Quartile (Q3): 7% (Black-Canadian/American)

100
• Maximum: 13% (Black-African)
2. Measures of Central Tendency and Dispersion:
• Mean: 5.1%
• Standard Deviation: 4.06%

Distribution Analysis
• The highest percentage of homeless individuals belongs to the Black-African group,
accounting for 13% of the total homeless population. This is followed by the BlackAfro-Caribbean or Afro-Latinx group at 11% and First Nations at 10%.
• The lowest representation in the homeless population is from the ”Other: Black-AfricaEuropean” category, which accounts for 0%.
• There is a concentration of homelessness rates around the median value of 4%, indicating a central tendency for many racialized groups to be underrepresented in homelessness figures compared to the highest groups.
• The interquartile range (IQR), calculated as Q3 - Q1, is 5%, suggesting moderate
variability in the data.
• The standard deviation of 4.06% reflects a notable level of dispersion from the mean,
highlighting significant variation in the rates of homelessness across different racialized
groups.

Conclusion
The analysis reveals that homelessness is disproportionately high among certain racialized
groups, particularly Black-African, Black-Afro-Caribbean, and First Nations individuals.
There is a need for targeted policies to address homelessness within these communities, considering the substantial differences observed in homelessness rates among racialized groups.

101

Figure 23: Main Reasons behind evictions in Toronto CMA

Exploratory Data Analysis of Primary Reasons for Evictions in Toronto CMA
Data Description
The visualization provides the percentage distribution of the primary reasons for evictions in
the Toronto Census Metropolitan Area (CMA). The reasons for eviction include the sale of
property by the landlord, landlord wanting the unit for own use, conflict with the landlord,
demolition/conversion/major repairs, and being behind on rent payments.

Exploratory Data Analysis
1. Five-Number Summary for the Percentage of Reasons for Eviction:
• Minimum: 8% (Being behind on rent payments)
• First Quartile (Q1): 10% (Demolition, conversion, or major repairs)
• Median: 13% (Conflict with the landlord)
• Third Quartile (Q3): 26% (Landlord wanted unit for own use)
• Maximum: 37% (Sale of property by landlord)

102
2. Measures of Central Tendency and Dispersion:
• Mean: 18.8%
• Standard Deviation: 12.08%

Distribution Analysis
• The highest percentage of evictions is attributed to the sale of property by landlords,
which accounts for 37% of cases, suggesting that property transactions are a significant
driver of tenant displacement.
• The least cited reason for eviction is being behind on rent payments, at 8%, indicating
that financial difficulties in paying rent are not the predominant reason for eviction.
• The interquartile range (IQR), calculated as Q3 - Q1, is 16%, which shows a moderate
spread in the reasons for eviction.
• The standard deviation of 12.08% reflects a noticeable level of variability in the reasons
for eviction, with some reasons being significantly more common than others.

Conclusion
The data highlights that evictions are predominantly driven by landlords’ decisions to sell
or repurpose properties for personal use rather than tenant-related issues like unpaid rent.
Policies aimed at protecting tenants in cases of property sales or conversions could potentially
reduce the high rates of eviction attributed to these factors.

103

Figure 24: Age Distribution of the Homeless

Exploratory Data Analysis of Age Distribution of Homeless Individuals in Toronto CMA
Data Description
The visualization shows the percentage distribution of homeless individuals by age group in
the Toronto Census Metropolitan Area (CMA). The categories analyzed include All Respondents, City-administered shelters, Families, Outdoors, Single adults, and Youth. The age
groups considered are:
• 16 to 24 years
• 25 to 34 years
• 35 to 44 years
• 45 to 54 years
• 55 to 59 years
• 60 years and older

104

Exploratory Data Analysis
1. Five-Number Summary for the Age Group Distribution: The analysis is provided
for each age group across the different categories.
• 16 to 24 years:
– Minimum: 5.43% (Outdoors)
– First Quartile (Q1): 10.10% (Families)
– Median: 12.37% (All Respondents)
– Third Quartile (Q3): 13.27% (City-administered shelters)
– Maximum: 100% (Youth)
• 25 to 34 years:
– Minimum: 18.37% (City-administered shelters)
– First Quartile (Q1): 18.48% (Outdoors)
– Median: 18.56% (All Respondents)
– Third Quartile (Q3): 26.26% (Families)
– Maximum: 26.26% (Families)
• 35 to 44 years:
– Minimum: 21.43% (City-administered shelters)
– First Quartile (Q1): 21.43% (City-administered shelters)
– Median: 21.65% (All Respondents)
– Third Quartile (Q3): 32.61% (Outdoors)
– Maximum: 33.33% (Families)
• 45 to 54 years:
– Minimum: 14.43% (Single adults)

105
– First Quartile (Q1): 17.17% (Families)
– Median: 20.41% (City-administered shelters)
– Third Quartile (Q3): 20.62% (All Respondents)
– Maximum: 23.91% (Outdoors)
• 55 to 59 years:
– Minimum: 6.06% (Families)
– First Quartile (Q1): 7.07% (Families)
– Median: 8.70% (Outdoors)
– Third Quartile (Q3): 11.34% (All Respondents)
– Maximum: 14.43% (Single adults)
• 60 years and older:
– Minimum: 5.06% (Families)
– First Quartile (Q1): 6.06% (Families)
– Median: 10.87% (Outdoors)
– Third Quartile (Q3): 15.46% (All Respondents)
– Maximum: 20.62% (Single adults)
2. Measures of Central Tendency and Dispersion:
• Mean for All Age Groups: 17.85%
• Standard Deviation for All Age Groups: 19.52%

Distribution Analysis
• Youth (16 to 24 years) account for a significant proportion in the ’Youth’ category,
with 100%, reflecting that the Youth classification is solely attributed to individuals
within this age range.

106
• The 25 to 34 years age group is more evenly distributed across the categories, with
percentages ranging from 18.37% to 26.26%.
• Older adults (55 years and above) show lower proportions, indicating that younger and
middle-aged adults make up the larger percentage of the homeless population.
• The wide range in percentages for the age group 16 to 24 years suggests a highly skewed
distribution, whereas other age groups present a more uniform distribution.

Conclusion
The data reveals that homeless individuals are predominantly middle-aged, particularly in
outdoor settings, while younger individuals (16 to 24 years) dominate the Youth category
exclusively. Age-based policies and interventions may need to be tailored to address the
distinct characteristics and needs of each age group.

Figure 25: Subsidized Housing Units in Toronto

107

Exploratory Data Analysis of Subsidized Housing Units
by Quarter
Data Description
The visualizations show the quarterly trends in the number of subsidized and affordable
housing units from Q1 2021 to Q1 2024. The first graph depicts the number of subsidized
housing units, while the second graph represents affordable housing units. Both visualizations exhibit an upward trend over the observed period.

Exploratory Data Analysis
1. Subsidized Housing Units
The five-number summary for the subsidized housing units data across the quarters is:
• Minimum: 82.5K (Q1 2024)
• First Quartile (Q1): 84.7K (Q2 2023 to Q4 2023)
• Median: 85.1K (Q4 2021)
• Third Quartile (Q3): 85.8K (Q3 2022 to Q2 2023)
• Maximum: 86.0K (Q2 2021, Q3 2021, Q1 2024)
2. Affordable Housing Units
The five-number summary for the affordable housing units data across the quarters is:
• Minimum: 6.5K (Q1 2021)
• First Quartile (Q1): 6.9K (Q3 2021)
• Median: 7.4K (Q4 2022)
• Third Quartile (Q3): 8.1K (Q1 2022, Q3 2022)
• Maximum: 9.6K (Q1 2024)

108

Measures of Central Tendency and Dispersion
• Mean of Subsidized Housing Units: 85.2K
• Standard Deviation of Subsidized Housing Units: 1.2K
• Mean of Affordable Housing Units: 7.6K
• Standard Deviation of Affordable Housing Units: 1.1K

Distribution Analysis
• The data for subsidized housing units shows a relatively steady increase with some
periods of stabilization, particularly around 84.7K and 85.8K.
• Affordable housing units exhibit a more significant relative increase over time, with a
sharper rise in the latter quarters, especially between Q4 2023 and Q1 2024.
• There is a greater variability in the number of affordable housing units compared
to subsidized housing units, as seen in the five-number summary and the standard
deviation values.
• The peaks and plateaus in both datasets suggest incremental additions or policy-driven
changes at particular points in time.

Conclusion
The data highlights an overall positive trend in both subsidized and affordable housing units
over the examined period, with a steeper increase in affordable units. This indicates efforts
to address housing affordability, especially towards the later quarters.

109
Category
2018 (% of households) 2021 (% of households) 2022 (% of households)
All households
21.5
19.5
22.0
Owner-occupied
16.2
14.3
16.1
With a mortgage
23.5
20.9
23.6
Without a mortgage
5.9
5.2
5.5
Renter
32.9
30.3
33.0
Living in social and affordable housing
29.4
22.2
25.4
Living in market rental housing
33.4
31.4
34.0

Table 10: Share of households that spend 30% or more of their household income on shelter
costs, Canada, 2018, 2021, and 2022

Exploratory Data Analysis of Household Shelter Costs
in Canada
Data Description
Table 10 shows the percentage of households in Canada that spent 30% or more of their
household income on shelter costs in the years 2018, 2021, and 2022. The data is categorized
by the type of housing tenure, including owner-occupied households (with and without mortgages), renters, and those living in social and affordable housing or market rental housing.

Exploratory Data Analysis
Five Number Summary for Each Category
• All Households:
– Minimum: 19.5% (2021)
– First Quartile (Q1): 21.5% (2018)
– Median: 22.0% (2022)
– Third Quartile (Q3): 22.0% (2022)
– Maximum: 22.0% (2022)
• Owner-occupied:
– Minimum: 14.3% (2021)

110
– First Quartile (Q1): 16.1% (2022)
– Median: 16.2% (2018)
– Third Quartile (Q3): 16.2% (2018)
– Maximum: 16.2% (2018)
• With a Mortgage:
– Minimum: 23.5% (2021)
– First Quartile (Q1): 25.4% (2022)
– Median: 25.5% (2018)
– Third Quartile (Q3): 25.5% (2018)
– Maximum: 25.5% (2018)
• Without a Mortgage:
– Minimum: 5.2% (2021)
– First Quartile (Q1): 5.9% (2018)
– Median: 5.3% (2022)
– Third Quartile (Q3): 5.9% (2018)
– Maximum: 5.9% (2018)
• Renter:
– Minimum: 30.3% (2021)
– First Quartile (Q1): 32.9% (2018)
– Median: 33.0% (2022)
– Third Quartile (Q3): 33.0% (2022)
– Maximum: 33.0% (2022)
• Living in Social and Affordable Housing:

111
– Minimum: 22.2% (2021)
– First Quartile (Q1): 29.4% (2018)
– Median: 29.4% (2018)
– Third Quartile (Q3): 29.4% (2018)
– Maximum: 29.4% (2018)
• Living in Market Rental Housing:
– Minimum: 31.4% (2021)
– First Quartile (Q1): 34.0% (2022)
– Median: 34.0% (2022)
– Third Quartile (Q3): 34.0% (2022)
– Maximum: 34.0% (2022)

Measures of Central Tendency and Dispersion
• Mean for All Households: 21.0%
• Standard Deviation for All Households: 1.3%
• Mean for Owner-occupied: 15.5%
• Standard Deviation for Owner-occupied: 0.9%
• Mean for With a Mortgage: 24.8%
• Standard Deviation for With a Mortgage: 1.0%
• Mean for Without a Mortgage: 5.6%
• Standard Deviation for Without a Mortgage: 0.4%
• Mean for Renter: 32.1%
• Standard Deviation for Renter: 1.3%

112
• Mean for Living in Social and Affordable Housing: 26.7%
• Standard Deviation for Living in Social and Affordable Housing: 3.8%
• Mean for Living in Market Rental Housing: 32.9%
• Standard Deviation for Living in Market Rental Housing: 1.3%

Conclusion
The analysis reveals that renters and those living in market rental housing consistently
have the highest percentage of households spending 30% or more of their income on shelter
costs, with values above 30%. Households without a mortgage exhibit the lowest values,
suggesting that mortgage-free homeownership provides significant financial relief in terms
of housing costs. There is also a noticeable increase in the share of households facing high
shelter costs between 2021 and 2022 across nearly all categories.
Year
1990
1991
1992
1993
1994
1995
1996
1997
1998
1999
2000
2001
2002
2003
2004

Single Semi-Detached Row Apartment
All
7,067
180 1,867
9,609 18,723
9,459
206 3,030
6,119 18,814
9,027
836 2,325
8,582 20,770
8,350
408 3,298
4,684 16,637
10,811
1,409 2,592
3,631 18,443
6,879
896 3,323
5,227 16,325
10,517
1,612 4,056
3,178 18,998
15,240
2,619 3,283
9,753 30,895
12,696
3,232 5,361
4,621 25,910
15,535
4,933 5,773
8,663 34,904
17,119
5,586 6,163
10,114 38,982
22,116
5,041 8,540
13,885 49,582
22,115
5,208 4,194
11,843 43,405
16,366
4,786 5,749
14,315 41,475
13,220
4,703 5,978
12,856 36,757

Table 11: Toronto — Historical Starts by Dwelling Type (1990 to 2004)

113

Exploratory Data Analysis of Historical Housing Starts
by Dwelling Type in Toronto (1990-2004)
Data Description
Table 11 provides the historical data on the number of housing starts by dwelling type in
Toronto from 1990 to 2004. The data includes four dwelling types: Single-family, SemiDetached, Row, and Apartment, along with a total count for each year.

Exploratory Data Analysis
Five Number Summary for Each Dwelling Type (1990-2004)
• Single-family:
– Minimum: 7,067 (1990)
– First Quartile (Q1): 10,214
– Median: 12,760
– Third Quartile (Q3): 15,756
– Maximum: 22,116 (2002)
• Semi-Detached:
– Minimum: 180 (1990)
– First Quartile (Q1): 1,409
– Median: 3,167
– Third Quartile (Q3): 4,850
– Maximum: 5,928 (1999)
• Row Housing:
– Minimum: 408 (1993)
– First Quartile (Q1): 1,867

114
– Median: 3,035
– Third Quartile (Q3): 4,694
– Maximum: 6,529 (1999)
• Apartment:
– Minimum: 2,153 (1995)
– First Quartile (Q1): 5,227
– Median: 7,861
– Third Quartile (Q3): 9,609
– Maximum: 12,856 (2004)
• All Dwelling Types:
– Minimum: 18,443 (1994)
– First Quartile (Q1): 26,225
– Median: 33,867
– Third Quartile (Q3): 38,982
– Maximum: 43,405 (2002)

Measures of Central Tendency and Dispersion
• Mean for Single-family: 13,558
• Standard Deviation for Single-family: 4,201
• Mean for Semi-Detached: 3,204
• Standard Deviation for Semi-Detached: 1,943
• Mean for Row Housing: 3,046
• Standard Deviation for Row Housing: 1,697

115
• Mean for Apartment: 7,122
• Standard Deviation for Apartment: 2,668
• Mean for All Dwelling Types: 31,224
• Standard Deviation for All Dwelling Types: 8,290

Conclusion
The data reveals that Single-family housing starts have the highest variability, with the
widest range and highest standard deviation, indicating significant fluctuations over the
years. In contrast, Semi-Detached and Row housing types exhibit smaller ranges and lower
variability, suggesting more stable development patterns. The trend in Apartment starts
is relatively consistent, although it exhibits some variability, particularly in the later years.
Overall, the total number of starts shows a general increase, peaking around the early 2000s.
Year
2005
2006
2007
2008
2009
2010
2011
2012
2013
2014
2015
2016
2017
2018
2019
2020
2021
2022
2023

Single Semi-Detached Row Apartment
All
15,797
3,375 6,516
15,908 41,596
14,120
2,892 5,177
14,891 37,080
14,769
2,864 5,280
10,380 33,293
11,308
2,853 6,515
12,636 32,412
12,301
1,654 4,365
13,240 29,195
11,247
2,010 4,231
22,257 39,745
13,485
1,985 5,401
29,617 48,488
9,421
1,874 4,103
18,149 33,547
8,830
1,530 3,861
14,808 28,929
10,223
1,106 5,133
25,825 42,287
11,848
1,420 5,838
20,174 38,738
10,172
1,410 6,982
20,174 38,738
6,405
926 4,137
29,639 41,107
4,200
459 3,951
21,683 30,462
5,848
3,037 8,480
23,638 38,587
9,620
786 3,955
30,237 44,598
4,368
430 4,060
38,018 46,876
6,329
514 5,648
32,618 45,109
4,721
328 4,860
37,519 47,428

Table 12: Toronto — Historical Starts by Dwelling Type (2005 to 2023)

116

Exploratory Data Analysis of Historical Starts by Dwelling
Type in Toronto (2005-2023)
Data Description
Table 12 presents the historical housing starts in Toronto by dwelling type for the period
from 2005 to 2023. The dwelling categories included are Single-family, Semi-Detached, Row,
and Apartment, along with the total starts for each year.

Exploratory Data Analysis
Five Number Summary for Each Dwelling Type (2005-2023)
• Single-family:
– Minimum: 4,721 (2023)
– First Quartile (Q1): 6,329
– Median: 10,120
– Third Quartile (Q3): 12,301
– Maximum: 17,469 (2007)
• Semi-Detached:
– Minimum: 328 (2023)
– First Quartile (Q1): 1,420
– Median: 2,011
– Third Quartile (Q3): 2,892
– Maximum: 3,373 (2005)
• Row Housing:
– Minimum: 4,060 (2022)
– First Quartile (Q1): 5,004

117
– Median: 5,516
– Third Quartile (Q3): 6,529
– Maximum: 7,663 (2009)
• Apartment:
– Minimum: 12,368 (2008)
– First Quartile (Q1): 21,709
– Median: 28,636
– Third Quartile (Q3): 32,618
– Maximum: 39,447 (2022)
• All Dwelling Types:
– Minimum: 30,412 (2018)
– First Quartile (Q1): 35,962
– Median: 38,538
– Third Quartile (Q3): 41,166
– Maximum: 47,428 (2023)

Measures of Central Tendency and Dispersion
• Mean for Single-family: 9,542
• Standard Deviation for Single-family: 3,716
• Mean for Semi-Detached: 1,978
• Standard Deviation for Semi-Detached: 1,005
• Mean for Row Housing: 5,524
• Standard Deviation for Row Housing: 885

118
• Mean for Apartment: 26,510
• Standard Deviation for Apartment: 7,656
• Mean for All Dwelling Types: 38,236
• Standard Deviation for All Dwelling Types: 5,475

Conclusion
The analysis reveals that Single-family and Apartment starts exhibit the most variability,
with higher standard deviations, reflecting fluctuations in housing starts over the years.
Semi-Detached and Row housing starts have more stable trends, with smaller ranges and
lower variability. The overall trend for total starts shows an increase, particularly towards
the later years, indicating growth in housing development in Toronto.

119

Community Services
In our analysis of community services, we identified target variables that capture access to,
utilization of, and the impact of various community support services in the Greater Toronto
Area. These variables include:
• Access to Social Services: This variable measures the availability and accessibility
of social services, including food banks, counseling, addiction treatment, and youth
programs. It helps assess service coverage and identify gaps in service delivery.
• Issues impacting NGO Performance: Pressure on NGO support services due to
shortages of staff and recruitment shortfall.
• Funding and Budget of NGOs This variable captures the funds available for the
NGOs and lack thereof.
These target variables provide a comprehensive view of the community services landscape
in the Greater Toronto Area. By analyzing these variables, we can better understand the
role of community services in supporting vulnerable populations, predict future service needs,
and inform strategies for enhancing service delivery and social support.

Figure 26: Ontario NGO’s by operating budget

120

Exploratory Data Analysis of Ontario NGOs by Operating Budget (2024)
Data Description
The visualization presents the distribution of Ontario NGOs in 2024 based on their operating
budget. The operating budget categories range from ”0 to $99,999” to ”$10,000,000 and
more,” including a category for organizations that chose not to disclose their budget.

Exploratory Data Analysis
Five Number Summary
The following five-number summary describes the distribution of percentages of Ontario
NGOs across different budget categories:
• Minimum: 0.03 (Do not wish to answer)
• First Quartile (Q1): 0.05 ($250,000 to $499,999)
• Median: 0.07 ($100,000 to $249,999)
• Third Quartile (Q3): 0.14 ($0 to $99,999)
• Maximum: 0.18 ($1,000,000 to $2,999,999)

Measures of Central Tendency and Dispersion
• Mean Percentage: 0.10
• Standard Deviation: 0.06

Conclusion
The analysis indicates that the majority of Ontario NGOs fall into lower to mid-range operating budgets, with the highest proportion in the ”$1,000,000 to $2,999,999” category. There

121
is a noticeable number of organizations with budgets below $100,000, suggesting a significant
presence of smaller NGOs. The spread of the data, as indicated by the standard deviation,
shows moderate variability in operating budgets across the NGOs.

Figure 27: Demand for Services by NGO’s

Exploratory Data Analysis of Demand for Services by
NGOs in Ontario
Data Description
The visualization illustrates the demand for services by NGOs in Ontario, classified into
three categories: ”Increased demand for programs and services,” ”No increased demand for
programs and services,” and ”Not sure.” The data presents the proportion of NGOs reporting
each level of demand.

Exploratory Data Analysis
Five Number Summary
The five-number summary provides insights into the distribution of demand levels reported
by NGOs:
• Minimum: 0.06 (Not sure)

122
• First Quartile (Q1): 0.08 (Not sure)
• Median: 0.16 (No increased demand for programs and services)
• Third Quartile (Q3): 0.76 (Increased demand for programs and services)
• Maximum: 0.83 (Increased demand for programs and services)

Measures of Central Tendency and Dispersion
• Mean Percentage: 0.33
• Standard Deviation: 0.35

Conclusion
The analysis indicates that the majority of NGOs in Ontario reported an increased demand
for their programs and services, with proportions reaching up to 83%. A smaller portion of
NGOs (16%) reported no increased demand, while an even smaller group (6% to 8%) were
unsure about the changes in demand. The high standard deviation reflects the variability in
service demand across NGOs.

Figure 28: Forecast of NGO’s in Ontario

123

Exploratory Data Analysis of NGO Sustainability Forecast in Ontario (2023 vs. 2024)
Data Description
The visualization provides a comparative analysis of the sustainability forecasts of NGOs
in Ontario for the years 2023 and 2024. It categorizes the expected duration that NGOs
anticipate they can sustain their operations, ranging from 1 to 3 months to more than 12
months. Additionally, some NGOs expressed uncertainty regarding their sustainability.

Exploratory Data Analysis
Five Number Summary for 2023
The five-number summary for the 2023 data is:
• Minimum: 0.08 (Able to sustain organization for 1 to 3 months)
• First Quartile (Q1): 0.11 (Able to sustain organization for 4 to 6 months)
• Median: 0.16 (Able to sustain organization for 7 to 12 months)
• Third Quartile (Q3): 0.57 (Able to sustain organization for more than 12 months)
• Maximum: 0.57 (Able to sustain organization for more than 12 months)
Five Number Summary for 2024
The five-number summary for the 2024 data is:
• Minimum: 0.09 (Able to sustain organization for 1 to 3 months)
• First Quartile (Q1): 0.10 (Not sure)
• Median: 0.13 (Able to sustain organization for 4 to 6 months)
• Third Quartile (Q3): 0.54 (Able to sustain organization for more than 12 months)
• Maximum: 0.54 (Able to sustain organization for more than 12 months)

124

Measures of Central Tendency and Dispersion
• Mean Percentage for 2023: 0.22
• Mean Percentage for 2024: 0.21
• Standard Deviation for 2023: 0.20
• Standard Deviation for 2024: 0.17

Conclusion
The analysis reveals that a substantial proportion of NGOs in Ontario are confident in their
sustainability for more than 12 months, with both years showing over 50% of NGOs in
this category. However, there is a slight decrease from 57% in 2023 to 54% in 2024. The
uncertainty among NGOs also dropped from 18% in 2023 to 10% in 2024. The calculated
standard deviations indicate a similar spread in sustainability expectations for both years,
suggesting consistent responses across categories.

Figure 29: Impact of staff shortage on NGO’s

125

Exploratory Data Analysis of Shortage Impact on NGOs
in Ontario (2022-2024)
Data Description
The visualization illustrates the impacts of shortages on NGOs in Ontario from 2022 to
2024. It highlights three main effects: increased waitlists, programs being discontinued, and
programs being scaled back. The trends over the three years are displayed, showing how
these impacts have changed over time.We must bear in mind that the data are in percentage.

Exploratory Data Analysis
Five Number Summary for Increased Waitlists
• Minimum: 10 (2022)
• First Quartile (Q1): 12 (2024)
• Median: 20 (2023)
• Third Quartile (Q3): 40 (2024)
• Maximum: 40 (2024)
Five Number Summary for Programs Discontinued
• Minimum: 8 (2023)
• First Quartile (Q1): 10 (2022)
• Median: 12 (2024)
• Third Quartile (Q3): 30 (2023)
• Maximum: 30 (2023)

126
Five Number Summary for Programs Scaled Back
• Minimum: 40 (2023)
• First Quartile (Q1): 40 (2022)
• Median: 50 (2022)
• Third Quartile (Q3): 50 (2022)
• Maximum: 60 (2024)

Measures of Central Tendency and Dispersion
• Mean Percentage for Increased Waitlists: 20.67
• Mean Percentage for Programs Discontinued: 16.67
• Mean Percentage for Programs Scaled Back: 50.00
• Standard Deviation for Increased Waitlists: 15.28
• Standard Deviation for Programs Discontinued: 9.81
• Standard Deviation for Programs Scaled Back: 8.16

Conclusion
The data indicates that the impact on NGOs in Ontario has intensified from 2022 to 2024.
The most significant change was observed in the category of ”Programs Scaled Back,” which
increased from 40% in 2023 to 60% in 2024. Similarly, ”Increased Waitlists” showed a
rise from 20% in 2023 to 40% in 2024, indicating an increasing strain on services. The
standard deviation values suggest that while the spread of data is relatively moderate across
all categories, there is a higher variability in the increase of waitlists.

127

Figure 30: Types of Skill Shortages in NGO’s in Ontario 2024

Exploratory Data Analysis of Skill Shortages in Ontario
NGOs in 2024
Data Description
The visualization presents data on various types of skill shortages reported by NGOs in
Ontario for the year 2024. The chart lists the areas where NGOs are experiencing a shortage
of skills, with the corresponding proportion of organizations affected. The categories cover
a range of skills, from fundraising and IT/Tech to social workers and educators.

Exploratory Data Analysis
Five Number Summary for Skill Shortages
The five-number summary provides insight into the distribution of skill shortages across
different categories:
• Minimum: 0.02 (Healthcare, nursing, PSW; Social workers and educators)
• First Quartile (Q1): 0.16 (Senior management; Program design and delivery)

128
• Median: 0.22 (Volunteer Management/Coordination)
• Third Quartile (Q3): 0.27 (Communications; Data; Human Resources)
• Maximum: 0.42 (Fundraising)

Measures of Central Tendency and Dispersion
• Mean Proportion of Skill Shortages: 0.22
• Standard Deviation: 0.10

Conclusion
The data highlights significant skill shortages across a variety of areas within Ontario NGOs,
with the most prominent shortage reported in fundraising (0.42). IT/Tech skills (0.34) also
represent a substantial gap, while areas such as social work and healthcare show the lowest
reported shortages (0.02). The five-number summary and measures of central tendency
indicate that most skill shortages fall between 0.16 and 0.27, suggesting a moderate level of
demand across various competencies.
Factors
Skills shortage
Staff burnout and stress
Uncompetitive compensation packages
Wage disparity for similar/same jobs across sectors
Lack of funding
Lack of candidates in your region
Short-term precarious contracts
Lack of paid learning/advancement opportunities
Unhealthy work culture
Wage restraint legislation (e.g. Bill 124)
Winding down of COVID-19 federal and provincial supports
Staff pushback to return to in-person work
Lack of affordable accessible child care services for staff
Other

2023 Under 500K Annual Budget Between 500K and 3M
52%
33%
48%
51%
29%
49%
49%
40%
53%
47%
29%
53%
45%
58%
46%
42%
29%
39%
39%
47%
43%
20%
18%
17%
19%
24%
22%
14%
2%
10%
14%
16%
12%
13%
3%
9%
8%
3%
9%
6%
11%
5%

More than 3M
68%
67%
48%
54%
29%
50%
38%
22%
22%
28%
14%
25%
12%
4%

Table 13: Recruitment Retention Factors in NGO’s in Ontario in 2023

129

Exploratory Data Analysis of Recruitment Retention
Factors in Ontario NGOs (2023)
Data Description
Table 13 presents data on various recruitment and retention factors affecting NGOs in Ontario during 2023, segmented by the size of the organization’s annual budget. The factors
include skills shortage, burnout, uncompetitive compensation, funding issues, and several
others. The table reports the percentage of NGOs facing each issue across different budget
categories: Under 500K, Between500K and 3M, andM orethan3M.

Exploratory Data Analysis
Five Number Summary for Each Recruitment Factor (2023)
The five-number summary gives insight into the spread of each recruitment retention factor
across the different budget categories. Here are the summaries for some key factors:
• Skills Shortage
– Minimum: 47%
– First Quartile (Q1): 49%
– Median: 52%
– Third Quartile (Q3): 67%
– Maximum: 67%
• Staff Burnout and Stress
– Minimum: 50%
– First Quartile (Q1): 56%
– Median: 59%
– Third Quartile (Q3): 67%

130
– Maximum: 67%
• Uncompetitive Compensation Packages
– Minimum: 46%
– First Quartile (Q1): 54%
– Median: 59%
– Third Quartile (Q3): 65%
– Maximum: 65%
• Lack of Funding
– Minimum: 38%
– First Quartile (Q1): 47%
– Median: 49%
– Third Quartile (Q3): 56%
– Maximum: 56%

Measures of Central Tendency and Dispersion
• Mean Percentage for Skills Shortage: 58%
• Standard Deviation for Skills Shortage: 9.13
• Mean Percentage for Staff Burnout and Stress: 60.2%
• Standard Deviation for Staff Burnout and Stress: 6.85
• Mean Percentage for Uncompetitive Compensation Packages: 58.5%
• Standard Deviation for Uncompetitive Compensation Packages: 7.53
• Mean Percentage for Lack of Funding: 49.2%
• Standard Deviation for Lack of Funding: 7.33

131

Conclusion
The analysis highlights prevalent recruitment and retention challenges faced by Ontario
NGOs, with significant issues like skills shortages and staff burnout being reported across
all budget categories. The variability across different factors, as evidenced by the standard
deviations, suggests a considerable range in how these challenges impact NGOs depending
on their size.
Strategy
Signing bonuses
We have not implemented any of these strategies
4-day work week
Onetime bonuses
Succession Planning
Equity training and strategies
Enhanced perks (e.g. reimbursement for cellphone use, transportation support, etc.)
Wellness programs (additional time off, retreats, sabbaticals, etc.)
Increased benefits (e.g. health and dental insurance, pension or other retirement benefits, etc.)
Mental health support (e.g. expanded benefits, counselling, etc.)
Career advancement opportunities (training, mentorship, etc.)
Raised salary
Remote work options (e.g. hybrid, fulltime, etc.)
Flexible working hours
Other

2024
3%
10%
12%
16%
23%
26%
27%
29%
31%
35%
36%
55%
58%
59%
1%

Table 14: Recruitment Strategies of NGO’s in Ontario in 2024

Exploratory Data Analysis of Recruitment Strategies in
Ontario NGOs (2024)
Data Description
Table 14 provides information on the recruitment strategies employed by NGOs in Ontario
in 2024. The strategies range from signing bonuses, flexible working hours, and wellness programs to remote work options and mental health support. The table presents the percentage
of NGOs that have implemented each strategy.

132

Exploratory Data Analysis
Five Number Summary for Recruitment Strategies (2024)
The five-number summary offers insights into the distribution of the implementation rates
for various strategies:
• Signing Bonuses
– Minimum: 3%
– First Quartile (Q1): 3%
– Median: 3%
– Third Quartile (Q3): 3%
– Maximum: 3%
• Flexible Working Hours
– Minimum: 1%
– First Quartile (Q1): 12%
– Median: 26%
– Third Quartile (Q3): 36%
– Maximum: 59%
• Remote Work Options
– Minimum: 1%
– First Quartile (Q1): 29%
– Median: 36%
– Third Quartile (Q3): 50%
– Maximum: 58%
• Mental Health Support

133
– Minimum: 3%
– First Quartile (Q1): 23%
– Median: 31%
– Third Quartile (Q3): 50%
– Maximum: 58%

Measures of Central Tendency and Dispersion
• Mean Percentage for Signing Bonuses: 3%
• Standard Deviation for Signing Bonuses: 2.82
• Mean Percentage for Remote Work Options: 55%
• Standard Deviation for Remote Work Options: 8.51
• Mean Percentage for Flexible Working Hours: 30.25%
• Standard Deviation for Flexible Working Hours: 13.86
• Mean Percentage for Mental Health Support: 16.6
• Standard Deviation for Mental Health Support: 15.21
Space Shortage Reason
We are at risk of losing our space due to the rising cost of rent.
We are at risk of losing our space due to the building being developed, demolished or sold.
We are at risk of losing our space due to the rising cost of mortgages.
We want to own our space but are facing barriers.
We want to expand current ownership of our spaces but are facing barriers.
We do not have space and need it.
Our current space does not meet our needs.
We do not have issues
Others

Percentage of Surveyed Answers
13%
10%
2%
15%
9%
10%
32%
40%
7%

Table 15: Space Shortage Reasons and Percentage of Surveyed Answers

134

Exploratory Data Analysis of Space Shortage Reasons
(2024)
Data Description
Table 15 provides the reasons for space shortages experienced by organizations, along with
the percentage of surveyed respondents who cited each reason. The reasons include the
risk of losing space due to high rent or mortgage costs, barriers to space ownership, the
inadequacy of current space, and other factors.

Exploratory Data Analysis
Five Number Summary for Space Shortage Reasons (2024)
The five-number summary provides a statistical overview of the distribution of the percentages:
• Minimum: 2% (We are at risk of losing our space due to the rising cost of mortgages)
• First Quartile (Q1): 7% (Others)
• Median: 10% (We are at risk of losing our space due to the building being developed,
demolished, or sold)
• Third Quartile (Q3): 15% (We want to own our space but are facing barriers)
• Maximum: 32% (Our current space does not meet our needs)
Additional Measures
• Mean: 14.27%
• Standard Deviation: 9.77

135

Discussion
The most frequently cited reason for space shortages is the inadequacy of current space,
with 32% of respondents indicating this issue. The least common reason is the rising cost
of mortgages (2%). The data shows a moderate variability in responses, as indicated by the
standard deviation.

136

Engaged and Connected Citizenship
In our analysis of factors related to engaged citizens, we identified target variables that
capture the levels of social trust, community engagement, and sense of belonging in the
Greater Toronto Area. These variables include:
• Sense of Belonging: This variable measures the degree to which individuals feel
connected to their community. It is used to assess social cohesion and the likelihood of
active community participation, as well as its impact on mental health and well-being.
• Trust in Institutions: This variable captures the level of trust that individuals
place in various institutions, such as government, law enforcement, healthcare systems,
and educational institutions. It helps to understand how confidence in institutions
influences civic engagement and compliance with social norms.
• Trust in Neighbors: This variable measures the level of trust individuals have in
their neighbors and the broader community. It is used to evaluate social capital and
community support networks, which are important for collective action and mutual
aid.
These target variables provide a comprehensive understanding of factors that influence
community engagement, social trust, and the sense of belonging in the Greater Toronto
Area. By analyzing these variables, we can develop strategies to foster more engaged and
connected communities, thereby enhancing social cohesion and collective well-being.

137

Figure 31: Confidence in Institutions and Media by Province

Exploratory Data Analysis of High Confidence in Institutions and Trust in Media by Province
Data Description
The visualization presents the percentage of individuals with high confidence in institutions
and high trust in the media across various Canadian provinces: Quebec, Prairie provinces,
Ontario, British Columbia, and Atlantic provinces. The data highlights the differences between confidence in institutions and trust in the media for each region.

Exploratory Data Analysis
High Confidence in Institutions
The five-number summary for high confidence in institutions is:
• Minimum: 23% (Atlantic provinces)
• First Quartile (Q1): 24% (British Columbia)

138
• Median: 25% (Ontario)
• Third Quartile (Q3): 27% (Prairie provinces)
• Maximum: 36% (Quebec)
Additional measures:
• Mean: 27%
• Standard Deviation: 4.98
High Trust in the Media
The five-number summary for high trust in the media is:
• Minimum: 12% (Prairie provinces)
• First Quartile (Q1): 13% (Ontario, British Columbia)
• Median: 15% (Atlantic provinces)
• Third Quartile (Q3): 21% (Quebec)
• Maximum: 21% (Quebec)
Additional measures:
• Mean: 15%
• Standard Deviation: 3.73

Discussion
The data reveals that Quebec has the highest percentage of individuals with high confidence
in institutions (36%) and high trust in the media (21%). In contrast, the Prairie provinces
report the lowest levels for both metrics, with 27% confidence in institutions and 12% trust
in the media. The variability in confidence is higher for institutions (standard deviation of

139
4.98) compared to trust in the media (standard deviation of 3.73), indicating more consistent
levels of media trust across the regions.

Figure 32: Racial Discrimination in Canada and the Pandemic

Exploratory Data Analysis of Self-Perceived Racial Discrimination Before and After the Pandemic
Data Description
The visualization displays self-reported experiences of racial discrimination across various
racial groups before and after the onset of the COVID-19 pandemic. The green bars represent
the percentage of individuals perceiving racial discrimination in the five years before the
pandemic, while the brown bars indicate the percentage since the start of the pandemic.
The racial groups included are Black, Filipino, Korean, Chinese, South Asian, West Asian,
Latin American, Southeast Asian, and Arab.

Exploratory Data Analysis
Self-Perceived Discrimination Before the Pandemic
The five-number summary for self-perceived racial discrimination before the pandemic is:

140
• Minimum: 3.1% (Arab)
• First Quartile (Q1): 4.7% (Latin American)
• Median: 5.9% (South Asian)
• Third Quartile (Q3): 8.0% (Filipino)
• Maximum: 8.4% (Black)
Additional measures:
• Mean: 5.95%
• Standard Deviation: 1.88
Self-Perceived Discrimination Since the Start of the Pandemic
The five-number summary for self-perceived racial discrimination since the pandemic is:
• Minimum: 4.4% (Arab)
• First Quartile (Q1): 5.8% (West Asian)
• Median: 7.4% (Korean)
• Third Quartile (Q3): 9.1% (Black)
• Maximum: 10.4% (Chinese)
Additional measures:
• Mean: 7.49%
• Standard Deviation: 1.89

141

Discussion
The data indicates a general increase in the perception of racial discrimination since the start
of the pandemic across all groups. The largest increase is observed in the Chinese group,
where the perception rose from 6.0% before the pandemic to 10.4% after its onset. The Arab
group experienced the smallest increase, with a change from 3.1% to 4.4%. The distribution
of perceived discrimination is more dispersed since the pandemic (standard deviation of 1.89)
compared to before the pandemic (standard deviation of 1.88), indicating slightly increased
variability in experiences among the different groups.

Figure 33: Reasons for discrimination in Canada

Exploratory Data Analysis of Self-Perceived Reasons for
Discrimination Pre and Post Pandemic
Data Description
The visualization illustrates self-perceived reasons for discrimination in two time periods:
the five years before the pandemic (shown in yellow) and post-pandemic (shown in green).
The reasons include Race or Ethnicity, Physical Appearance, Age, Sex, Language, Religion,
Disability, Sexual Orientation, and Gender Identity.

142

Exploratory Data Analysis
Discrimination Before the Pandemic
The five-number summary for perceived reasons for discrimination before the pandemic is:
• Minimum: 5% (Gender Identity)
• First Quartile (Q1): 10% (Disability)
• Median: 17% (Religion)
• Third Quartile (Q3): 29% (Age)
• Maximum: 44% (Race or Ethnicity)
Additional measures:
• Mean: 20.33%
• Standard Deviation: 12.76
Discrimination Post Pandemic
The five-number summary for perceived reasons for discrimination after the pandemic is:
• Minimum: 7% (Gender Identity)
• First Quartile (Q1): 10% (Disability)
• Median: 20% (Language)
• Third Quartile (Q3): 34% (Age)
• Maximum: 50% (Race or Ethnicity)
Additional measures:
• Mean: 22.33%
• Standard Deviation: 13.53

143

Discussion
The data shows an increase in discrimination reported across all categories post-pandemic.
Race or Ethnicity remains the most cited reason for discrimination, rising from 44% before the pandemic to 50% after. The smallest increases are observed in Gender Identity
(from 5% to 7%) and Sexual Orientation (from 9% to 8%). There is a wider spread in
post-pandemic discrimination (standard deviation of 13.53) compared to pre-pandemic discrimination (standard deviation of 12.76), indicating slightly greater variability in the reasons
cited post-pandemic.

Figure 34: Institutional Trust in Canada as of 2022, 2023

Exploratory Data Analysis of Trust in Institutions in
Canada
Data Description
The visualization illustrates the level of trust in various institutions in Canada over three
time points: Fall 2022 (green), Spring 2023 (purple), and Fall 2023 (green). The institutions
include Police, School System, Justice System and Courts, Federal Parliament, and Canadian
Media. Trust is represented as percentages.

144

Exploratory Data Analysis
Trust in Police
The five-number summary for trust in the Police is:
• Minimum: 61% (Spring 2023)
• First Quartile (Q1): 62% (Fall 2022)
• Median: 65% (Fall 2023)
• Third Quartile (Q3): 65% (Fall 2023)
• Maximum: 65% (Fall 2023)
Standard Deviation: 2.08
Trust in School System
The five-number summary for trust in the School System is:
• Minimum: 44% (Spring 2023)
• First Quartile (Q1): 45% (Fall 2023)
• Median: 47% (Fall 2022)
• Third Quartile (Q3): 47% (Fall 2022)
• Maximum: 47% (Fall 2022)
Standard Deviation: 1.25
Trust in Justice System and Courts
The five-number summary for trust in the Justice System and Courts is:
• Minimum: 42% (Spring 2023)
• First Quartile (Q1): 46% (Fall 2022)

145
• Median: 46% (Fall 2022)
• Third Quartile (Q3): 49% (Fall 2023)
• Maximum: 49% (Fall 2023)
Standard Deviation: 3.06
Trust in Federal Parliament
The five-number summary for trust in the Federal Parliament is:
• Minimum: 28% (Spring 2023, Fall 2023)
• First Quartile (Q1): 28% (Spring 2023)
• Median: 32% (Fall 2022)
• Third Quartile (Q3): 32% (Fall 2022)
• Maximum: 32% (Fall 2022)
Standard Deviation: 2.31
Trust in Canadian Media
The five-number summary for trust in Canadian Media is:
• Minimum: 30% (Spring 2023)
• First Quartile (Q1): 31% (Fall 2022)
• Median: 31% (Fall 2022)
• Third Quartile (Q3): 37% (Fall 2023)
• Maximum: 37% (Fall 2023)
Standard Deviation: 3.21

146

Discussion
The data indicates that the highest trust levels are consistently seen in the Police, while the
lowest levels of trust are observed in Federal Parliament and Canadian Media. Over time,
slight variations are noted, with some institutions experiencing small declines (e.g., Police
from Fall 2022 to Spring 2023), while others remain relatively stable (e.g., Canadian Media).

Figure 35: Sense of belonging and Social Trust

Exploratory Data Analysis of Trust in Society by Sense
of Belonging
Data Description
The visualization presents data on trust in society based on individuals’ sense of belonging.
The categories include ”Very Strong,” ”Somewhat Strong,” ”Somewhat Weak,” and ”Very
Weak” senses of belonging, with percentages indicating the proportion of individuals who
reported high trust in society.

147

Exploratory Data Analysis
Trust by Sense of Belonging
The five-number summary for trust based on the sense of belonging is:
• Minimum: 26% (Very Weak)
• First Quartile (Q1): 44% (Somewhat Weak)
• Median: 65% (Somewhat Strong)
• Third Quartile (Q3): 78% (Very Strong)
• Maximum: 78% (Very Strong)
Standard Deviation: 21.64

Discussion
The data demonstrates a clear relationship between the sense of belonging and trust in
society. Individuals with a ”Very Strong” sense of belonging exhibit the highest levels of
trust (78%), while those with a ”Very Weak” sense of belonging show the lowest levels of
trust (26%). This indicates that a stronger sense of belonging is associated with higher trust
in society.

Figure 36: Social Trust by Area

148

Exploratory Data Analysis of Trust in Society by Area
Type
Data Description
The visualization illustrates the percentage of individuals who reported high trust in society
across different area types. The categories include ”Rural Areas,” ”Population of less than
500,000,” ”Population of 500,000 to 1,499,999,” ”Urban Areas,” and ”Population of 1.5
million or more.”

Exploratory Data Analysis
Trust by Area Type
The five-number summary for trust in society by area type is:
• Minimum: 46% (Population of 1.5 million or more)
• First Quartile (Q1): 50% (Urban Areas)
• Median: 51% (Population of 500,000 to 1,499,999)
• Third Quartile (Q3): 55% (Population of less than 500,000)
• Maximum: 66% (Rural Areas)
Standard Deviation: 7.38

Discussion
The data reveals that trust in society is highest among individuals residing in rural areas
(66%), while it is lowest for those living in regions with a population of 1.5 million or more
(46%). This trend suggests that smaller communities may foster a stronger sense of trust,
whereas larger urban populations may experience comparatively lower levels of trust.

149

Figure 37: High Trust in Neighborhood by Age

Exploratory Data Analysis of Trust in Neighbors by Age
Group
Data Description
The visualization shows the percentage of individuals reporting high trust in their neighbors
across different age groups. The age categories represented are ”75 years and older,” ”65 to
74 years,” ”55 to 64 years,” ”45 to 54 years,” ”35 to 44 years,” ”15 to 24 years,” and ”25 to
34 years.”

Exploratory Data Analysis
Trust in Neighbors by Age Group
The five-number summary for the percentage reporting high trust in neighbors is:
• Minimum: 43% (15 to 24 years, 25 to 34 years)
• First Quartile (Q1): 46%
• Median: 54% (45 to 54 years)

150
• Third Quartile (Q3): 65% (65 to 74 years)
• Maximum: 70% (75 years and older)
Standard Deviation: 10.43

Discussion
The data indicates that older age groups exhibit a higher level of trust in their neighbors
compared to younger age groups. The percentage of individuals reporting high trust in
neighbors is greatest among those aged 75 years and older (70%) and lowest among the
younger cohorts (43% for both 15 to 24 years and 25 to 34 years). This trend suggests that
trust in neighbors may increase with age.
Measure
Excellent or very good mental health
Fair or poor mental health
Excellent or very good general health
Fair or poor general health
Persons with a disability or long-term condition
Persons without a disability or long-term condition
Very difficult or difficult to meet financial needs
Easy or very easy to meet financial needs
High life satisfaction (rating from 8 to 10)
Low life satisfaction (rating from 0 to 5)
High sense of meaning and purpose (rating from 8 to 10)
Low sense of meaning and purpose (rating from 0 to 5)
High trust in others
Low trust in others

Low confidence in institutions (%) High confidence in institutions (%)
65
35
85
15
69
31
80
20
78
22
69
31
81
19
61
39
64
36
86
14
65
35
87
13
63
37
80
20

Table 16: Confidence in Institutions in Canada

Exploratory Data Analysis of Confidence in Institutions
in Canada
Data Description
The table presents data on confidence in institutions in Canada based on various factors.
The factors include health status (mental and general health), disability status, financial
difficulty, life satisfaction, sense of meaning and purpose, and trust in others. The data is
categorized into two groups: low confidence in institutions and high confidence in institutions,
with corresponding percentages.

151

Exploratory Data Analysis
Low Confidence in Institutions
The five-number summary for the percentage of low confidence in institutions is:
• Minimum: 61% (Easy or very easy to meet financial needs)
• First Quartile (Q1): 67.5%
• Median: 78% (Persons with a disability or long-term condition, Persons without a
disability or long-term condition)
• Third Quartile (Q3): 85% (Fair or poor mental health)
• Maximum: 87% (Low sense of meaning and purpose)
Standard Deviation: 8.59
High Confidence in Institutions
The five-number summary for the percentage of high confidence in institutions is:
• Minimum: 13% (Low sense of meaning and purpose)
• First Quartile (Q1): 19.5%
• Median: 22% (Persons with a disability or long-term condition)
• Third Quartile (Q3): 31% (Excellent or very good general health)
• Maximum: 39% (High life satisfaction)
Standard Deviation: 7.57

Discussion
The data indicates a significant variation in confidence in institutions across different factors.
Individuals with a low sense of meaning and purpose exhibit the highest percentage of low

152
confidence (87%), while those with high life satisfaction report the highest level of high confidence (39%). This suggests that both subjective well-being and general life circumstances
significantly influence confidence in institutions.

Summary of the Sponsor Project: Insights to Alleviate
Poverty in Greater Toronto Area
Introduction
The data analyses conducted above have provided a comprehensive understanding of various
social issues in the Greater Toronto Area (GTA), including income inequality, homelessness,
housing affordability, and public trust in institutions. The findings reveal valuable insights
that can help United Way Greater Toronto and similar NGOs to better advocate for the poor
and homeless, allocate resources effectively, and implement strategies aimed at alleviating
poverty.

Key Insights and Their Implications
1. Income Disparities and Housing Affordability
The exploratory data analysis of income levels from 1970 to 2015 indicated a significant
decrease in the middle-income population, with an increasing proportion of low-income
households over the years. The housing affordability analysis revealed that a substantial
percentage of households are spending over 30% of their income on shelter, especially renters
and those living in market rental housing.
These findings suggest a need for increased affordable housing options and rent subsidies
to alleviate the financial burden on low-income households. United Way Greater Toronto
could advocate for policies that increase the supply of affordable rental units and expand
housing assistance programs to reduce the risk of homelessness due to high housing costs.

153
2. Homelessness and Eviction Trends
The analysis of homelessness data showed high rates of homelessness among racialized groups,
with Black and Indigenous communities being disproportionately affected. Additionally,
eviction rates were shown to spike in certain years, suggesting economic downturns and
housing crises as contributing factors.
These insights highlight the need for targeted interventions that address the unique challenges faced by racialized and marginalized groups. NGOs can focus their outreach and
support programs in communities with higher eviction rates and implement culturally sensitive services that consider the specific needs of these populations. Preventing evictions
through legal aid, mediation services, and temporary rent support could be an effective
strategy.
3. Employment and Skill Shortages
The findings on employment trends indicated that certain groups, including those with disabilities and people facing mental health challenges, are more likely to report low confidence
in institutions and experience barriers to employment. There is also a noted skills shortage
within NGOs, particularly in areas like fundraising, IT, and grant writing.
To address these issues, United Way Greater Toronto can collaborate with local organizations to offer skill development programs for vulnerable populations, focusing on enhancing
employability in high-demand sectors. Additionally, NGOs can seek to upskill their workforce in critical areas to improve service delivery and organizational sustainability.
4. Public Trust and Institutional Confidence
The data showed a decline in public trust in institutions, especially among individuals with
low life satisfaction, financial difficulties, or poor health. The analysis also revealed that a
strong sense of belonging is associated with higher trust levels.
These findings suggest that efforts to build community trust should focus on engaging
marginalized groups through inclusive policies and programs. NGOs can strengthen social
capital by facilitating community events, support groups, and local networks that foster

154
a sense of belonging. Moreover, advocating for transparent and fair practices in public
institutions can help rebuild trust in these entities.

Strategies for Resource Allocation and Advocacy
1. Targeted Housing Solutions
Based on the analysis, NGOs should prioritize providing housing support to low-income
groups who are struggling to afford shelter costs. Programs like rent subsidies, eviction prevention, and affordable housing initiatives could alleviate the pressure on these households.
Additionally, specific efforts to support racialized groups facing higher risks of homelessness
would ensure resources are allocated where they are needed most.
2. Skill Development and Employment Support
To tackle poverty, initiatives should focus on equipping vulnerable populations with marketable skills, particularly in fields where there are labor shortages. Providing training
programs in IT, fundraising, grant writing, and data management would not only improve
individual employment prospects but also strengthen the NGO sector itself. Collaborating
with local businesses to offer internships or apprenticeships could bridge the gap between
training and employment.
3. Strengthening Community Trust
Programs aimed at increasing public confidence in institutions should be community-centered.
For example, United Way Greater Toronto could organize community forums where residents
discuss their concerns with local authorities, thereby fostering transparency and trust. Emphasizing support for mental health services and life satisfaction programs would also help
in improving trust levels and overall community well-being.
4. Advocacy for Policy Changes
The data indicates that policies targeting affordable housing, fair wages, and inclusive employment practices could significantly impact poverty levels. NGOs should advocate for

155
increased government funding for social housing, expansion of rent control policies, and
wage equity legislation. Engaging policymakers with evidence-based research derived from
the analysis can be a powerful tool for driving policy reforms.

Conclusion
The exploratory data analysis has highlighted critical areas where United Way Greater
Toronto and other NGOs can intervene to alleviate poverty and support marginalized communities in the GTA. By prioritizing affordable housing, employment support, community
trust-building, and targeted policy advocacy, these organizations can effectively address the
root causes of poverty. The insights derived from this project can guide resource allocation
and strategic decision-making to create a more equitable and resilient society.

Recommendations for Future Work
Further research is recommended to continuously monitor the impact of implemented programs and refine strategies based on emerging data trends. Longitudinal studies could help
understand the long-term effects of poverty alleviation efforts, while qualitative research
could offer deeper insights into the lived experiences of affected communities. Collaboration
with academic institutions and data scientists will also be beneficial in leveraging advanced
data analytics techniques for ongoing social impact assessments.

156

Hypothesis Testing and Predictive Analytics
Financial Stability
Gini Coefficient
We analyzed the Gini Coefficient that measures the distribution of wealth, with 0 being
perfect equality and 1 being perfect inequality.
Table 17: Summary of Paired T-tests between City of Toronto and Other Regions and Peel
and York
Comparison
City of Toronto vs Halton Region
City of Toronto vs York Region
City of Toronto vs Peel Region
City of Toronto vs Durham Region
City of Toronto vs Toronto CMA
Peel Region vs York Region

t-value

df

3.86
3.11
2.97
3.19
2.74
-2.15

5
5
5
5
5
5

p-value 95% CI Lower
0.0119
0.0267
0.0312
0.0243
0.0409
0.0842

95% CI Upper

Mean Difference

0.0889
0.1097
0.1337
0.1475
0.0969
0.0023

0.0533
0.0600
0.0717
0.0817
0.0500
-0.0117

0.0178
0.0103
0.0096
0.0158
0.0031
-0.0256

The paired sample t-test results in Table 17 compare the Gini coefficients between the City
of Toronto and other regions, including Halton Region, York Region, Peel Region, Durham
Region, and Toronto CMA, as well as between Peel and York Regions. Each comparison
quantifies the difference in income inequality levels across these regions, as measured by the
mean difference and statistical significance of Gini coefficients.
• City of Toronto vs. Halton Region: The mean difference in Gini coefficients is
0.0533 (p = 0.0119), indicating that Toronto has a higher level of inequality compared
to Halton Region, with a significant difference.
• City of Toronto vs. York Region: The mean difference of 0.0660 (p = 0.0267)
shows that Toronto also has significantly higher inequality than York Region, with a
moderate level of statistical significance.
• City of Toronto vs. Peel Region: The mean difference is 0.0717 (p = 0.0312),
suggesting a substantial difference, with Toronto again having higher income inequality
than Peel Region.

157
• City of Toronto vs. Durham Region: The t-test reveals a mean difference of
0.0817 (p = 0.0243), showing that inequality is higher in Toronto compared to Durham
Region, and this difference is statistically significant.
• City of Toronto vs. Toronto CMA: The mean difference of 0.0500 (p = 0.0409)
indicates that income inequality in the City of Toronto is significantly higher than in
the broader Toronto CMA.
• Peel Region vs. York Region: This comparison shows a mean difference of 0.0117 (p = 0.0842), which, while negative, is not statistically significant, indicating
that income inequality levels between Peel and York Regions are relatively comparable.
In summary, the t-tests reveal that the City of Toronto has significantly higher Gini coefficients, or income inequality levels, compared to its neighboring regions, with Durham
Region showing the largest disparity and Peel Region showing a considerable difference as
well. However, there is no statistically significant difference between Peel and York Regions,
suggesting similar levels of inequality between them. The results emphasize Toronto’s comparatively high inequality within the Greater Toronto Area and its neighboring regions.
Table 18: RMSE Summary for Linear Regression Models
Model

RMSE

City of Toronto Model
York Region Model
Peel Region Model

0.0224
0.0044
0.0052

Table 18 provides a summary of the Root Mean Squared Error (RMSE) values for linear
regression models developed for the City of Toronto, York Region, and Peel Region. RMSE,
a measure of the model’s accuracy, represents the average deviation between predicted and
actual values, with lower values indicating higher model accuracy.
The model for the City of Toronto has an RMSE of 0.0224, which is relatively higher
compared to the other regions, indicating that the predictions for the City of Toronto have a
slightly larger average error. The York Region model exhibits the lowest RMSE at 0.0044,
suggesting that this model achieves the most precise predictions among the three regions.

158
Meanwhile, the Peel Region model has an RMSE of 0.0052, which, although higher than
that of York Region, still demonstrates relatively high accuracy.
In summary, the RMSE values show that the model for York Region has the highest
prediction accuracy, followed by Peel Region, with the City of Toronto model showing slightly
lower accuracy. This variation in RMSE values suggests that the models perform differently
across regions, with York Region’s model fitting the data more closely than the others.

Figure 38: Predictive Linear Model for Gini Index

Table 19: Predicted Gini Index for City of Toronto, York Region, and Peel Region
Year

City of Toronto

York Region

Peel Region

2030

0.3571

0.2127

0.1761

Gini Index Over Time (Observed and Predicted): City of Toronto,
York Region, and Peel Region
The above figure presents a comparative analysis of the observed and predicted values of the
Gini Index for the City of Toronto, York Region, and Peel Region over time. The Gini Index
is a widely used measure of income inequality, with values ranging from 0 (perfect equality)

159
to 1 (maximum inequality). This analysis provides a longitudinal view of income inequality
trends from 1970 to 2030, focusing on both historical data and future projections.
City of Toronto: The Gini Index for the City of Toronto shows a consistent upward
trend across both observed and predicted values. Observed data indicate a steady increase
in inequality from 1970, with the predicted values extending this trend into the future. By
2030, the Gini Index for Toronto is projected to exceed 0.4, highlighting a substantial rise
in income inequality over the examined period. This trend reflects the ongoing challenges of
economic disparity within a highly urbanized and diverse metropolitan area. The observed
data points (depicted as solid blue circles) align closely with the predicted trajectory (dashed
blue line), indicating a robust model fit for this region.
York Region: The York Region demonstrates a more moderate increase in the Gini Index.
The observed values (solid red line with points) show a gradual rise from 1970 to 2010, with
the predicted values (dashed red line) continuing this trend. By 2030, the Gini Index for York
Region is projected to reach approximately 0.25. Although income inequality is increasing
in this region, it remains significantly lower compared to Toronto. This difference may
be attributed to a relatively homogeneous socio-economic profile and slower urbanization
compared to Toronto. The alignment of observed and predicted values suggests the model
effectively captures the dynamics of income distribution in York Region.
Peel Region: Among the three regions, Peel Region exhibits the lowest levels of income
inequality, as indicated by both observed and predicted Gini Index values. Observed data
points (solid green line with points) reveal a relatively stable trend, with a slight upward
trajectory over time. The predicted values (dashed green line) suggest a modest increase,
with the Gini Index projected to remain below 0.2 by 2030. This stability in inequality
levels may be reflective of balanced economic growth and effective policy interventions in the
region. Peel Region’s lower Gini Index values highlight its comparatively equitable income
distribution.
Summary: The above figure underscores distinct regional disparities in income inequality trends across the City of Toronto, York Region, and Peel Region. Toronto emerges as
the region with the highest and fastest-growing inequality, while York Region experiences
moderate growth, and Peel Region exhibits the least inequality. The predictive model shows

160
strong alignment with observed data, indicating its reliability for projecting future trends.
These findings emphasize the need for targeted policy measures to address widening income
gaps, particularly in Toronto, where inequality is expected to rise substantially. The comparative stability in Peel Region and moderate growth in York Region suggest that tailored
regional strategies could effectively mitigate the impact of economic disparities.

Figure 39: Decision Tree Model for Gini Index
The decision tree model depicted in Figure 39 is used to predict and compare Gini coefficients
across various regions, specifically focusing on the City of Toronto, Durham Region, and York
Region. The tree structure provides a set of hierarchical rules based on Gini Index thresholds
to classify the regions according to their income inequality levels.
• Root Node (Gini Index ≥ 0.1958): The model begins with a split at a Gini Index
threshold of 0.1958. Regions with a Gini Index equal to or above this value are classi-

161
fied as the City of Toronto, indicating that Toronto exhibits a higher level of income
inequality compared to other regions. The classification here reflects Toronto’s unique
socioeconomic characteristics, placing it in a distinct category of higher inequality.
• Left Child Node (Gini Index < 0.1958): Regions with a Gini Index below 0.1958
are further divided at a Gini Index threshold of 0.1533. This node represents areas
with moderate inequality levels, dividing the regions into Durham Region and York
Region.
• Durham Region (Gini Index < 0.1533): The branch resulting from a Gini Index
less than 0.1533 is classified as Durham Region. This classification suggests that
Durham has the lowest levels of income inequality among the three regions in the
model, reflecting a relatively more equitable distribution of income.
• York Region (Gini Index ≥ 0.1533 but < 0.1958): Regions with Gini Index
values between 0.1533 and 0.1958 are classified as York Region. This intermediate
range suggests that York Region experiences moderate income inequality, positioned
between the higher inequality observed in Toronto and the lower inequality in Durham.
In summary, the decision tree model classifies the regions based on two key Gini Index
thresholds, effectively categorizing them into high, moderate, and low inequality levels. The
City of Toronto, with a Gini Index greater than or equal to 0.1958, is identified as the
region with the highest inequality. York Region, with values between 0.1533 and 0.1958,
represents moderate inequality, while Durham Region, with values below 0.1533, has the
lowest inequality. This decision tree highlights the clear income inequality distinctions among
these regions, with Toronto standing out for its significantly higher Gini Index.

Living wage
We created a predictive Linear Model for Living Wage for the various regions of the Toronto
CMA. Table 20 presents a summary of the linear regression model used to predict living
wages based on several predictors, including the year, minimum wage, and region-specific

162
Table 20: Summary of Linear Model for Living Wage Prediction
Predictor

Estimate

Std. Error

t-value

Pr

(Intercept)
Year
Minimum Wage
Region: Halton
Region: Peel Region
Region: Toronto
Region: York

-2873.7801
1.4315
-0.1124
3.3758
3.3819
4.1900
6.6000

663.0899
0.3280
0.5046
0.5272
0.5272
0.4828
0.4828

-4.334
4.364
-0.223
6.403
6.415
8.679
13.670

0.00119 **
0.00113 **
0.82778
5.06e-05 ***
4.98e-05 ***
2.99e-06 ***
3.02e-08 ***

factors. The model aims to capture the impact of these variables on the estimated living
wage, with statistically significant predictors highlighted.
• Year: The coefficient for Year is 1.4315 with a p-value of 0.00113, indicating a significant positive trend over time. This suggests that the living wage has been increasing
annually, likely due to inflation and cost-of-living adjustments.
• Minimum Wage: The coefficient for Minimum Wage is -0.1124 with a p-value of
0.82778, which is not statistically significant. This result implies that minimum wage
changes do not have a significant direct impact on the predicted living wage in this
model, potentially due to regional differences in cost structures or the relatively small
changes in minimum wage over time.
• Region Effects:
– Halton Region: The coefficient for Halton is 3.3758 with a highly significant pvalue (5.06e-05), indicating that the predicted living wage in Halton is notably
higher than the baseline region (assumed to be Durham or another region not
explicitly listed).
– Peel Region: Peel Region has a coefficient of 3.3819 with a significant p-value
of 4.98e-05, suggesting that living wages in Peel are also significantly higher than
in the baseline region, comparable to Halton’s effect.
– City of Toronto: The City of Toronto exhibits an even larger positive coefficient
of 4.1900, with a highly significant p-value (2.99e-06). This reflects Toronto’s

163
higher cost of living, where the required living wage is higher than in the baseline
region.
– York Region: York Region shows the highest regional effect with a coefficient of
6.6000 and a p-value of 3.02e-08, indicating a very strong positive impact on the
predicted living wage. This suggests that the cost of living in York is significantly
higher than in all other regions considered in this model.
In summary, this linear model identifies significant regional differences in living wage requirements, with York Region demonstrating the highest predicted living wage, followed by
Toronto, Peel, and Halton. The yearly increase in living wage is statistically significant,
whereas minimum wage does not show a meaningful impact on the predicted living wage.
These findings underscore the variation in living wage needs across regions, likely due to
differences in housing, transportation, and other living expenses.
Table 21: Model Fit Statistics
Statistic
Residual Standard Error
Multiple R-squared
Adjusted R-squared
F-statistic
p-value

Value
0.6828 on 11 degrees of freedom
0.9506
0.9237
35.29 on 6 and 11 DF
1.462e-06

Table 21 presents the model fit statistics for the linear regression model used to predict living
wages. These statistics provide insights into the model’s accuracy, explained variance, and
overall significance.
• Residual Standard Error (RSE): The Residual Standard Error is 0.6828 with
11 degrees of freedom, indicating the typical deviation of observed values from the
predicted values. This relatively low RSE suggests that the model’s predictions are
closely aligned with the actual data.
• Multiple R-squared: The Multiple R-squared value is 0.9506, meaning that approximately 95.06% of the variance in living wages can be explained by the model’s

164
predictors. This high value indicates a strong fit of the model to the data, suggesting
that the chosen predictors are effective in capturing the factors affecting living wage
levels.
• Adjusted R-squared: The Adjusted R-squared is 0.9237, which accounts for the
number of predictors in the model and adjusts for potential overfitting. This value,
slightly lower than the Multiple R-squared, indicates that the model remains robust
and explains a significant portion of the variance even when accounting for model
complexity.
• F-statistic: The F-statistic is 35.29 with 6 and 11 degrees of freedom, along with
an associated p-value of 1.462e-06. This high F-statistic and extremely low p-value
indicate that the overall model is statistically significant, meaning that the predictors
collectively explain a significant portion of the variance in living wages.
• p-value for Model: The overall p-value for the model is 1.462e-06, which is well
below conventional significance levels. This confirms that the probability of observing
the results by random chance is very low, further validating the model’s significance.
In summary, the model fit statistics indicate that this linear regression model is highly effective in predicting living wages, with a strong R-squared value, a low residual standard error,
and a highly significant F-statistic. These metrics suggest that the predictors used in the
model are well-suited to capturing the variation in living wages across regions and over time,
providing a reliable basis for understanding factors influencing living wage requirements.

165

Figure 40: Living Wage Prediction using Random Forests

Table 22: Feature Importance from Random Forest Model
Feature

% Increase in MSE

IncNodePurity

-0.9930
-3.5832
6.1684

8.368
4.389
45.164

Year
Minimum Wage
Region

Table 23: Model Evaluation: RMSE Comparison
Model

RMSE

Linear Regression
Random Forest

1.0293
2.0800

Tables 22 and 23 present the results of the Random Forest model for predicting living wages,
focusing on feature importance and model evaluation through RMSE (Root Mean Squared
Error) comparison with a linear regression model.

166
• Feature Importance (Table 22): Feature importance in the Random Forest model
is assessed based on the % Increase in MSE (Mean Squared Error) and IncNodePurity
metrics.
– Region: The Region variable shows the highest importance, with a 6.1684%
increase in MSE and an IncNodePurity of 45.164. This result indicates that
Region has a substantial impact on predicting living wages, suggesting significant
variations in living wage requirements across different regions.
– Minimum Wage: The Minimum Wage predictor shows a negative contribution
to MSE, with a -3.5832% increase, and a relatively low IncNodePurity of 4.389.
This suggests that Minimum Wage contributes minimally to the model’s predictive power in explaining variations in living wage requirements.
– Year: Similarly, the Year predictor also shows a negative impact on MSE, with
a -0.9930% increase and an IncNodePurity of 8.368. This indicates that the Year
variable does not significantly enhance the Random Forest model’s predictive
accuracy for living wages compared to the Region factor.
• Model Evaluation (Table 23): Table 23 compares the predictive performance of the
Random Forest model with a linear regression model using RMSE as the evaluation
metric.
– Linear Regression Model: The linear regression model demonstrates an RMSE
of 1.0293, indicating a relatively lower average prediction error compared to the
Random Forest model.
– Random Forest Model: The Random Forest model yields a higher RMSE of
2.0800, suggesting that this model may not be as effective as the linear regression
model for predicting living wages in this dataset. The higher RMSE implies that
the Random Forest model struggles to capture the relationship between predictors and the living wage accurately, potentially due to the limited significance of
Minimum Wage and Year in the feature importance analysis.
In summary, the Random Forest model identifies Region as the most critical predictor of

167
living wages, whereas Minimum Wage and Year show minimal impact. Despite its flexibility,
the Random Forest model underperforms compared to the linear regression model in terms of
RMSE, indicating that the linear approach may better capture the underlying relationships
in this dataset for predicting living wage requirements.

Low Income Predictions
We created two models to predict the percentage of the Low Income population in the
Toronto CMA. In one model we included the middle and higher income proportions to
account for possible social mobility and in the other model we used only the year as predictor
in a simple Linear Regression Model.

Figure 41: Low Income Projection without Social Mobility

168

Future Predictions of Low Income Levels by Region Without Social
Mobility
The above figure presents a detailed projection of low-income levels across five regions—Durham,
Halton, Peel Region, Toronto, and York—over the period 2025 to 2030, assuming the absence
of social mobility. This analysis highlights significant disparities in the predicted prevalence
of low-income populations across these regions, shedding light on the potential socioeconomic
challenges each area might face in the coming years.
Peel Region: Among the regions, Peel Region consistently demonstrates the highest
predicted levels of low-income populations throughout the observed period. The trend shows
a gradual but noticeable increase, indicating worsening socioeconomic conditions in the absence of upward mobility. The steady rise reflects systemic barriers that may disproportionately affect residents in Peel Region, exacerbating income inequalities. By 2030, Peel Region
is expected to retain its position as the region with the largest low-income population, which
underscores the need for targeted interventions.
Toronto: Toronto follows Peel Region in terms of predicted low-income levels. While the
trend for Toronto appears relatively stable compared to Peel, the absolute numbers remain
concerning. The lack of significant improvement in low-income levels suggests that structural
inequalities persist, limiting opportunities for economic advancement. Toronto’s role as a
densely populated and economically diverse urban center may contribute to these dynamics,
where high living costs and wage disparities are likely contributing factors.
York Region and Halton: York Region and Halton demonstrate relatively stable
and lower levels of predicted low-income populations. Both regions exhibit minimal change
over the projected period, reflecting a more balanced economic landscape. These trends
suggest that the socioeconomic conditions in these regions are less susceptible to systemic
inequalities, likely due to better access to resources, education, and economic opportunities.
Nevertheless, the stability of low-income levels does not imply the absence of poverty but
rather that the rates remain consistently lower compared to Peel Region and Toronto.
Durham: Durham exhibits the lowest levels of low-income populations among the five
regions, with minimal fluctuations across the projected timeline. This trend indicates that

169
Durham is less affected by systemic barriers to social mobility, possibly due to more equitable
income distribution and local economic conditions. The region’s consistently low levels of
predicted low income underscore its relative resilience to economic disparities, making it an
outlier in this analysis.
Key Insights: The figure highlights persistent regional disparities in low-income levels
under conditions where social mobility is not factored into the analysis. Regions such as
Peel and Toronto exhibit higher predicted levels, indicating that structural inequalities may
be deeply entrenched. Conversely, regions such as York, Halton, and Durham show more
stable and comparatively lower low-income levels, reflecting a more equitable economic environment. The divergence between regions emphasizes the importance of context-specific
policies to address poverty and inequality.
Implications for Policy: The projections in the above figure suggest that without meaningful interventions to enhance social mobility, income disparities are likely to widen, particularly in regions like Peel and Toronto. Policies aimed at improving access to education,
job training, affordable housing, and healthcare could mitigate the projected increases in
low-income populations. Additionally, regional economic development programs tailored to
the unique challenges of each area could help bridge the gap between high- and low-income
regions, fostering greater socioeconomic equity across the board.

170
Model with Social Mobility Included

Figure 42: Low Income Projection with Social Mobility

Table 24: Comparison of RMSE with and without Social Mobility Considered
Region
Toronto City
Durham
Halton
Peel Region
York

RMSE without Social Mobility

RMSE with Social Mobility Considered

1.0145
1.3423
0.0000
6.4762
1.5388

1.0037
0.2051
0.0000
0.8792
1.1358

Table 24 compares the Root Mean Squared Error (RMSE) values for models predicting
low-income levels across various regions, with and without the inclusion of social mobility
factors. RMSE is a measure of the average prediction error, with lower values indicating
more accurate predictions. This table reveals the impact of incorporating social mobility on
model performance across different regions.

171
• Toronto City: The RMSE for the model without social mobility is 1.0145, while it
slightly decreases to 1.0037 when social mobility is included. This marginal improvement suggests that social mobility has a modest effect on increasing the prediction
accuracy for Toronto’s low-income levels.
• Durham: Durham exhibits a significant reduction in RMSE from 1.3423 to 0.2051
with social mobility considered. This substantial decrease indicates that accounting for
social mobility greatly enhances the model’s accuracy in Durham, likely due to higher
income mobility within this region.
• Halton: Both models, with and without social mobility, have an RMSE of 0.0000
for Halton, suggesting perfect accuracy in the model’s predictions for this region. This
stability implies that low-income levels in Halton may be inherently predictable, potentially due to limited variability or high economic stability in this region.
• Peel Region: The RMSE for Peel Region decreases from 6.4762 to 0.8792 when
social mobility is included, indicating a significant improvement in predictive accuracy.
This result highlights the importance of considering social mobility factors in Peel
Region, as they appear to play a crucial role in shaping low-income levels.
• York: For York, the RMSE decreases from 1.5388 to 1.1358 when social mobility
is considered. This moderate improvement suggests that while social mobility has an
impact, it is less pronounced in York compared to Durham and Peel, potentially due
to relatively lower income mobility in this region.
In summary, incorporating social mobility into the predictive model generally improves accuracy, with the most notable effects observed in Durham and Peel Region. These findings
suggest that social mobility plays a significant role in predicting low-income levels, particularly in regions with higher income mobility. The results for Halton, where predictions
remain perfectly accurate with or without social mobility, indicate unique stability in this
region. Overall, the inclusion of social mobility provides a more accurate and nuanced understanding of low-income dynamics across the Toronto CMA.

172

Unemployment
Unemployment in the Peel Region Predicted and compared with Toronto CMA
We modeled unemployment within the Peel region of the Toronto CMA using Linear Regression with Year as a predictor in a simple linear regression model facilitating interpretability.
We compare and contrast the results obtained below and reflect on the RMSE of the different
simple models.
Table 25: RMSE Values for Linear Models by Region
Region

RMSE

Halton
Mississauga
Brampton
Toronto CMA

1.1052
0.8920
1.1369
0.5573

Figure 43: Peel Unemployment Prediction
Table 25 provides the Root Mean Squared Error (RMSE) values for linear models predicting
unemployment rates by region, while Figure 43 visualizes observed and predicted unemploy-

173
ment rates for Peel Region and Toronto CMA up to 2030. The RMSE values indicate the
accuracy of the predictions, with lower values reflecting more precise predictions.

Observed and Predicted Unemployment Rates by Peel Region and
Toronto CMA
The above figure provides a detailed analysis of both observed (2022–2024) and predicted
(2025–2030) unemployment rates for Halton, Mississauga, Brampton, and the Toronto Census Metropolitan Area (CMA). The unemployment rate, measured as the percentage of the
labor force that is unemployed and actively seeking work, is a critical indicator of economic
health and labor market dynamics. This visualization allows for a comparison of historical
trends alongside projections, highlighting regional disparities and trends over time.
Observed Trends (2022–2024): The observed data for 2022 to 2024 reveal significant
variability in unemployment rates across the regions. Halton consistently exhibits the lowest
unemployment rates, stabilizing around 4% throughout the observed period. This trend
suggests that Halton maintains a relatively robust labor market, possibly due to diversified
employment opportunities and economic stability.
In contrast, Brampton and Mississauga, key cities within the Peel Region, show higher
observed unemployment rates. Mississauga, while slightly better than Brampton, fluctuates
between 5% and 6%, indicating moderate instability in the labor market. Brampton, on
the other hand, experiences the highest observed unemployment rates, peaking above 7% in
2022. This trend reflects structural labor market challenges, such as industry-specific job
losses or population growth outpacing job creation.
The Toronto CMA displays unemployment rates similar to those of Mississauga, hovering slightly above 5%. As the economic hub of the region, Toronto’s labor market dynamics
are likely influenced by macroeconomic factors, including global economic conditions and
sector-specific trends.
Predicted Trends (2025–2030): The projections from 2025 to 2030 demonstrate a
decline in unemployment rates across all regions, reflecting potential economic recovery or
labor market adjustments. The most notable trend is observed in Mississauga, which shows a

174
sharp decline in unemployment rates, dropping below 4% by 2030. This indicates significant
improvements in labor market conditions, potentially driven by economic diversification or
policy interventions targeting employment.
Halton maintains its position as the region with the lowest unemployment rates, remaining below 4% throughout the projected period. This stability reinforces the region’s strong
economic foundation and resilience to labor market fluctuations.
Brampton, while still exhibiting higher unemployment rates compared to Halton and
Mississauga, shows gradual improvement. By 2030, Brampton’s unemployment rate is projected to fall below 5.5%, indicating slow but steady progress in addressing labor market
challenges.
The Toronto CMA displays relatively stable unemployment rates over the projected
period, with a slight decline from approximately 5% in 2025 to just below 4.5% by 2030.
This reflects the steady recovery of Toronto’s labor market, driven by its diverse economic
base and ongoing development initiatives.
Key Insights: The above figure highlights clear disparities in unemployment rates across
the regions, with Halton consistently outperforming the others. Mississauga demonstrates
significant projected improvement, while Brampton’s labor market faces persistent challenges, albeit with gradual recovery. The Toronto CMA, as a key metropolitan area, shows
moderate but steady progress in reducing unemployment. These trends underscore the importance of targeted policies to address region-specific labor market conditions, particularly
in Brampton, while maintaining and supporting economic growth in more stable regions like
Halton and Mississauga. Overall, the projections suggest an optimistic outlook for labor
market recovery across the analyzed regions by 2030.
York Unemployment Prediction
Table 26: RMSE Values for Linear Models by Region
Region

RMSE

York Region
Toronto CMA
Ontario

0.1449
0.0623
0.0381

175

Figure 44: Long term Predictions for Unemployment in York
We similarly modeled unemployment within the York region of the Toronto CMA using
Linear Regression with Year as a predictor in a simple linear regression model. We discuss
the results obtained below and comment on the RMSE metric of the different simple models.
Table 26 provides the Root Mean Squared Error (RMSE) values for linear models predicting
unemployment rates by region, while Figure 44 visualizes both observed and predicted unemployment rates for York Region, Toronto CMA, and Ontario up to the year 2030. RMSE
values indicate the prediction accuracy, with lower RMSE values signifying greater accuracy.

Observed and Predicted Unemployment Rates for York Region,
Toronto CMA, and Ontario
The above figure presents observed and predicted unemployment rates for York Region,
Toronto CMA, and Ontario over the period from 2022 to 2030. The unemployment rate is a
critical indicator of labor market health, representing the proportion of the workforce actively
seeking employment. This visualization highlights trends in unemployment rates, providing

176
a comparative analysis across the three regions during both historical and projected periods.
Observed Trends (2022–2024): The observed data reveal regional disparities in unemployment rates at the onset of the study period. In 2022, York Region exhibits slightly
higher unemployment rates compared to Toronto CMA and Ontario, with values exceeding
7%. Over the observed years, York Region demonstrates a gradual decline in unemployment,
reaching close to 6% by 2024. This reduction suggests ongoing economic recovery and labor
market stabilization within the region.
Toronto CMA also begins with relatively high unemployment rates, slightly lower than
York Region but above 6.5%. Similar to York Region, Toronto CMA experiences a steady
decline over the observed period, converging to nearly 5.5% by 2024. As a major metropolitan
area, Toronto CMA’s labor market dynamics are likely influenced by broader macroeconomic
factors, including urban economic restructuring and the recovery from the pandemic-induced
economic downturn.
Ontario, representing the provincial average, shows the lowest unemployment rates among
the three regions throughout the observed period. Starting near 6% in 2022, the unemployment rate in Ontario drops to approximately 5% by 2024. This trend reflects the relative
economic resilience of Ontario as a whole, likely due to its diversified industrial base and
regional policy interventions that mitigate unemployment disparities.
Predicted Trends (2025–2030): Projections for unemployment rates from 2025 to
2030 indicate significant improvements across all three regions. Ontario continues to maintain the lowest unemployment rates, stabilizing below 2% by 2026 and remaining constant
thereafter. This suggests a strong provincial economic outlook, with effective employment
policies contributing to sustained labor market recovery.
Toronto CMA demonstrates a similar trajectory, with unemployment rates falling below
2% by 2026 and maintaining stability through 2030. The consistency in predicted rates
suggests that Toronto’s labor market is expected to benefit from long-term structural adjustments and economic diversification.
York Region shows a more gradual recovery compared to the other two regions. While its
unemployment rates decline significantly from 2024 onwards, reaching approximately 2.5%
by 2026, the rates remain slightly higher than those of Toronto CMA and Ontario through-

177
out the projection period. This indicates persistent regional challenges, including potential
mismatches between labor demand and workforce skills or slower industrial diversification.
Key Insights: The figure underscores both observed and predicted disparities in unemployment rates among York Region, Toronto CMA, and Ontario. While all regions demonstrate a downward trend, York Region lags slightly behind in achieving lower unemployment
rates, suggesting the need for targeted interventions to address localized economic challenges.
Conversely, the projections for Ontario and Toronto CMA highlight their capacity for sustained labor market recovery, driven by economic resilience and policy effectiveness. These
findings emphasize the importance of region-specific strategies to ensure equitable economic
outcomes across the province.

Figure 45: Short term Predictions for Unemployment in York
Figure 45 presents observed and predicted short-term unemployment rates for York Region,
Toronto CMA, and Ontario, covering the period from 2021 to 2025. The figure displays both
observed values and linear model predictions, capturing trends over the next few years.

178
• Toronto CMA and Ontario: Both Toronto CMA and Ontario show a consistent
decline in unemployment rates throughout the short-term period. The predicted trend
suggests a steady decrease to around 2.5% by 2025. This gradual decline indicates
improved employment prospects for these areas, reflecting stable economic recovery.
The model captures these trends effectively, aligning closely with the observed data,
which suggests that the model performs well in regions with stable economic conditions.
• York Region: York Region exhibits a similar downward trend, with predicted unemployment rates declining from above 5% in 2022 to below 3% by 2025. Although
the trend mirrors that of Toronto CMA and Ontario, York Region shows slightly more
variability in the observed data, which indicates some fluctuations in unemployment
rates. This variability may reflect unique economic dynamics within York Region that
add complexity to short-term predictions.
• Comparison Across Regions: While all three regions demonstrate a downward
trend in unemployment rates, York Region’s rate starts from a higher baseline and
decreases more gradually compared to Toronto CMA and Ontario. This indicates that
although York is projected to improve, it may experience a slower economic recovery
relative to its neighboring regions. The model’s predictions highlight the short-term
convergence of unemployment rates across the regions, with all three areas expected
to approach similar levels by 2025.
In summary, Figure 45 illustrates a projected decline in unemployment rates for York Region,
Toronto CMA, and Ontario over the short term, with Toronto CMA and Ontario showing
smoother trends compared to York Region. The consistency in predicted trends across regions suggests positive economic recovery, while York Region’s slight variability underscores
regional economic differences. These results emphasize the model’s effectiveness in capturing
short-term unemployment trends, particularly in regions with more stable economic conditions.

179

Housing stability: Predictive Analytics
Predictions of Eviction Applications in Toronto CMA
We analyzed housing stability in Toronto CMA by using eviction applications and housing
starts for two predictive models.

Figure 46: Eviction Applications in Toronto CMA predictions
Figure 46 presents observed and predicted eviction applications in the Toronto Census
Metropolitan Area (CMA) from 2010 through projected year 2030. This model serves as
a key indicator of housing stability in the region, where declining eviction applications may
suggest improved housing conditions or economic stability.

Observed and Predicted Eviction Applications
The above figure provides a comprehensive analysis of observed and predicted eviction applications from 2010 to 2030. Eviction applications serve as a critical indicator of housing
stability, reflecting the socioeconomic challenges faced by vulnerable populations. The ob-

180
served data spans from 2010 to 2020, while the predictions extend from 2025 to 2030. This
analysis highlights the trends and potential future scenarios in eviction applications, offering insights into housing market dynamics and the impact of policies aimed at mitigating
evictions.
Observed Trends (2010–2020): The observed data reveals a fluctuating trend in
eviction applications over the decade. Starting at approximately 24,000 applications in
2010, the number rises sharply to a peak of nearly 28,000 applications in 2014. This sharp
increase may be indicative of economic instability, housing crises, or policy changes during
this period that heightened housing insecurity. After 2014, the trend reverses, showing a
steady decline in applications, reaching approximately 22,000 by 2020. This decline suggests
that measures to stabilize housing markets, such as rent control policies or economic recovery
efforts, may have contributed to reducing eviction filings. However, the fluctuations in the
observed data indicate persistent challenges in achieving long-term housing stability, as the
reduction in eviction applications does not follow a consistent trajectory.
Predicted Trends (2025–2030): The predicted data demonstrates a continuation of
the declining trend observed in the latter part of the observed period. Eviction applications
are projected to decline steadily, starting at approximately 22,433 in 2025 and dropping to
21,267 by 2030. This represents a reduction of approximately 5.2% over the forecasted fiveyear period. The downward trajectory suggests the potential effectiveness of ongoing housing
policies, economic recovery initiatives, and social interventions in addressing the root causes
of housing instability. The relatively small annual decrease highlights the incremental nature
of these improvements, emphasizing the need for sustained efforts to achieve meaningful
reductions in eviction rates.
The predicted data is accompanied by a Root Mean Square Error (RMSE) value of
1517.796, indicating the degree of accuracy of the predictive model. While the RMSE value
suggests a reasonable fit, it also underscores the inherent uncertainties in forecasting eviction
applications, particularly in the face of unforeseen economic or policy changes.
Key Insights and Implications: The above figure underscores the multifaceted nature
of eviction trends, which are influenced by economic conditions, housing policies, and broader
societal factors. The observed peak in 2014 highlights the vulnerability of renters during

181
periods of economic downturn or housing market instability. The subsequent decline in
observed applications suggests that interventions implemented during this period may have
been effective in mitigating eviction risks. However, the fluctuations observed throughout
the decade indicate that such measures may not have provided consistent or equitable relief.
The projected decline in eviction applications from 2025 to 2030 offers a cautiously optimistic outlook, suggesting that sustained efforts to address housing insecurity could yield
positive outcomes. Nevertheless, the incremental nature of the decline points to the need for
targeted strategies that address the specific needs of vulnerable populations. For example,
expanding access to affordable housing, providing rental assistance, and strengthening tenant protections could accelerate the reduction in eviction applications.
Conclusion: The observed and predicted trends in eviction applications highlight the
progress made in stabilizing housing markets while emphasizing the need for continued vigilance and proactive measures. The data suggests that while eviction rates are declining,
the pace of improvement remains gradual, necessitating sustained efforts to address systemic
barriers to housing stability. Policymakers and stakeholders should leverage these insights
to design interventions that promote equitable access to stable housing, ensuring that the
downward trajectory in eviction applications continues in the years to come.

182
Housing Starts

Figure 47: Housing Starts in Toronto CMA predictions
Figure 47 displays observed and predicted values of total housing starts in the Toronto
Census Metropolitan Area (CMA) from past years through projected values for 2030. This
model is an important indicator for understanding trends in housing supply, with increasing
housing starts suggesting efforts to meet the growing housing demand in the region.

Observed and Predicted Values of Housing Starts Over Time in
Toronto CMA
The above figure provides an analysis of observed and predicted housing starts in the Toronto
Census Metropolitan Area (CMA) over the period from 1990 to 2030. Housing starts, which
represent the commencement of construction on new residential units, are a critical indicator
of housing supply dynamics and economic activity within the construction sector. The
observed data spans from 1990 to 2022, while the predicted values cover the period from

183
2023 to 2030. This analysis highlights key trends, fluctuations, and future projections,
providing insights into the evolution of housing supply in Toronto CMA.
Observed Trends (1990–2022): The observed data reveals significant variability in
housing starts across the decades. In the early 1990s, housing starts were relatively low,
averaging around 20,000 units annually. This period reflects the lingering effects of economic
challenges during the late 1980s and early 1990s, which constrained housing market activity.
The late 1990s mark a period of steady growth, with housing starts increasing sharply
to peak levels of approximately 45,000 units annually by the early 2000s. This upward
trajectory corresponds to a period of economic recovery, rising demand for housing, and
policy interventions that incentivized new construction. However, the mid-2000s show a
marked decline in housing starts, reflecting cyclical downturns in the housing market and
broader economic uncertainties, such as the global financial crisis in 2008.
Between 2010 and 2022, housing starts exhibit a pattern of fluctuations, with peaks
and troughs corresponding to periods of economic growth and contraction. Notably, the
observed data indicates a resurgence in housing starts post-2020, reaching levels comparable
to the early 2000s. This resurgence may be attributed to increased housing demand, policy
measures addressing housing supply shortages, and economic recovery following the COVID19 pandemic.
Predicted Trends (2023–2030): The projected values for housing starts indicate a
continued upward trend over the forecasted period. Housing starts are expected to rise
steadily, reaching approximately 49,045 units in 2025, 50,691 units in 2027, and 53,160 units
by 2030. This represents a cumulative increase of around 8.4% over the seven-year projection
period.
The predicted growth reflects sustained demand for housing in the Toronto CMA, driven
by factors such as population growth, urbanization, and government initiatives aimed at
increasing housing affordability and supply. Additionally, the projections suggest a stabilization of market dynamics, as evidenced by the consistent upward trend in housing starts
with minimal fluctuations.
Key Insights and Implications: The trends in the above figure underscore the cyclical
nature of housing starts, driven by economic, demographic, and policy factors. The observed

184
data highlights the significant impact of macroeconomic conditions, such as the global financial crisis and COVID-19 pandemic, on housing construction activity. The recovery observed
post-2020 demonstrates the resilience of the housing market in the Toronto CMA, supported
by policy measures and a robust demand base.
The predicted data provides an optimistic outlook for the housing market, suggesting
sustained growth in housing starts over the next decade. However, the relatively modest growth rate underscores the challenges associated with meeting the housing needs of a
rapidly growing population. Policymakers and stakeholders must address barriers to housing
construction, such as rising construction costs, labor shortages, and regulatory constraints,
to ensure that the projected growth in housing starts translates into improved housing affordability and availability.
Conclusion: The observed and predicted trends in housing starts provide valuable insights into the evolution of the housing market in the Toronto CMA. While the projections
indicate sustained growth, achieving these targets will require continued efforts to address
structural challenges in the housing sector. The data underscores the need for coordinated
policy interventions to support housing supply, enhance affordability, and meet the needs of
a growing urban population.

Summary of Socioeconomic Trends Analysis in Toronto CMA
This project undertakes a comprehensive analysis of socioeconomic trends in the Toronto
Census Metropolitan Area (CMA) and surrounding regions, focusing on income inequality,
unemployment, housing starts, and living wage projections. The primary objective is to assess
the impact of various factors on regional socioeconomic outcomes, leveraging observed and
predicted data using statistical models such as linear regression and random forests.
The findings provide critical insights into disparities among regions, informing policymakers
about trends in inequality, affordability, and economic stability.
The analysis of income inequality, depicted through the Gini Index, demonstrates
a concerning upward trajectory for the City of Toronto, York Region, and Peel Region.
Projections indicate that by 2030, the City of Toronto will exhibit the highest Gini Index,
signifying a widening income gap. York and Peel Regions, while experiencing moderate

185
increases in inequality, maintain relatively lower levels compared to Toronto. These findings
underscore the pressing need for targeted policies to address income disparities in Toronto,
particularly as population growth and urbanization accelerate.
Living wage projections for the Greater Toronto Area (GTA) reveal relatively stable
trends across regions from 2025 to 2030, as shown in the analysis. While the living wage
remains consistent, it highlights the regional disparities in income adequacy, with certain
regions requiring higher wages to meet basic living standards. Additionally, the inclusion of
social mobility trends in low-income predictions underscores the impact of upward mobility
on economic outcomes, revealing a relatively stable proportion of low-income individuals in
the regions analyzed.
The analysis of unemployment rates, focusing on Peel Region, York Region, and
Toronto CMA, reveals significant regional variation. Observed data from 2022 indicates
higher unemployment rates in Mississauga and Brampton, while Toronto CMA and York
Region show lower rates. Projections up to 2030 reveal a gradual decline in unemployment
across all regions, reflecting recovery and stabilization post-pandemic. The Root Mean Square
Error (RMSE) values for the predictive models demonstrate their reliability, with Toronto
CMA exhibiting the lowest error and York Region showing slightly higher variability.
Housing starts serve as a critical indicator of economic activity and housing supply in
the Toronto CMA. Observed data from 1990 to 2022 highlights significant fluctuations, with
peaks corresponding to periods of economic growth. Projections from 2023 to 2030 indicate
a steady increase in housing starts, reflecting sustained demand and potential policy interventions aimed at addressing housing affordability. However, the upward trend underscores
the need to balance housing supply with equitable distribution to ensure affordability for
low-income populations.
The analysis also explores eviction applications, an indicator of housing insecurity.
Observed data from 2010 to 2020 reveals a peak in applications during the mid-2010s, followed by a decline. Projections up to 2030 suggest a continued downward trend, reflecting
potential improvements in housing stability and policy efforts to mitigate evictions. Despite
this positive outlook, challenges remain in addressing housing affordability and economic
disparities.

186
In conclusion, this study provides a data-driven examination of socioeconomic trends
in the Toronto CMA and surrounding regions. The findings highlight critical disparities
in income distribution, employment, and housing outcomes, offering valuable insights for
policymakers and stakeholders. The predictive models employed in this study demonstrate
robust reliability, enabling informed decision-making to promote economic stability and equity across regions. Future research should focus on the intersection of these socioeconomic
factors to develop integrated policy approaches for sustainable urban development.

187

References
Calculating the living wage: Toronto 2019. (2019). (Accessed: 2024-10-16)
City of Toronto. (2022). 2021 census backgrounder: Families, households, marital status,
and income. Retrieved from https://www.toronto.ca/wp-content/uploads/2022/
07/9877-City-Planning-2021-Census-Backgrounder-Families-Hhlds-Marital
-Status-Income.pdf (Accessed: 2024-10-16)
City of toronto 2021: Affordable housing deficit.

(2021).

https://hart.ubc.ca/our

-resources/city-of-toronto-2021/. (Accessed: 2024-10-16)
City of toronto 2021 street needs assessment results. (2021). Retrieved from https://
www.toronto.ca/legdocs/mmis/2021/ec/bgrd/backgroundfile-171729.pdf (Accessed: 2024-10-16)
Foundation, M. (2015). The working poor in the toronto region: Who they are, where they
live, and how trends are changing. Retrieved from https://metcalffoundation.com/
wp-content/uploads/2015/04/WorkingPoorToronto2015Final.pdf

(Accessed:

2024-10-16)
Leon, S.

(2020).

Forced out:

Evictions, race, and poverty in toronto.

Re-

trieved from https://www.wellesleyinstitute.com/wp-content/uploads/2020/
08/Forced-Out-Evictions-Race-and-Poverty-in-Toronto-.pdf (Accessed: 202410-16)
Lewis, N., de Wolff, A., King, A., Lopes, F., & Zon, N. (2020). The opportunity equation:
Building opportunity in the face of growing income inequality. (Accessed: 2024-10-16)
Mortgage, C., & Corporation, H.
ogy.

(2024).

Starts and completions survey methodol-

Retrieved from https://www.cmhc-schl.gc.ca/professionals/housing

-markets-data-and-research/housing-research/surveys/methodologies
-starts-completions-market-absorption-survey (Accessed: 2024-10-16)
Neighbourhood Change Research Partnership.
tion:

(2020).

The opportunity equa-

Building opportunity in the face of growing income inequality.

Re-

trieved from http://neighbourhoodchange.ca/documents/2020/01/opportunity
-equation-toronto-inequality-update.pdf (Accessed: 2024-10-16)

188
Network, O. L. W.

(2023).

Calculation archive.

Retrieved from https://www

.ontariolivingwage.ca/calculation archive (Accessed: 2024-10-16)
(ONN), O. N. N. (2024, October). 2024 state of the sector - policy report. Retrieved
from https://theonn.ca/publication/2024-survey-policy-report/

(Accessed:

16 October 2024)
Statistics Canada. (2019). Portrait of canadian society: Canadian social survey, 2019. Retrieved from https://www150.statcan.gc.ca/n1/pub/89f0115x/89f0115x2019001
-eng.htm (Catalogue no. 89F0115X2019001)
Statistics Canada. (2022). Study: Diverse generations of canadians: A profile of racialized
canadians in 2016. https://www150.statcan.gc.ca/n1/daily-quotidien/220908/
dq220908a-eng.htm. (Accessed: 2024-10-16)
Workforce Planning Board of York Region.

(2023).

Local labour market plan report

2022. Retrieved from https://www.wpboard.ca/hypfiles/uploads/2023/04/LLMP
-Report-2022-FNL.pdf (Accessed: 2024-10-16)
(City of Toronto 2021: Affordable Housing Deficit, 2021) (Mortgage & Corporation, 2024)
(Leon, 2020) (Lewis et al., 2020) (Foundation, 2015) ((ONN), 2024) (Network, 2023) (Calculating
the Living Wage: Toronto 2019 , 2019) (Neighbourhood Change Research Partnership, 2020)
(Statistics Canada, 2022) (Statistics Canada, 2019) (City of Toronto, 2022) (City of Toronto
2021 Street Needs Assessment Results, 2021) (Workforce Planning Board of York Region,
2023)



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
