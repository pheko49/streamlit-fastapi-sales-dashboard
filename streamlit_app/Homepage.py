import streamlit as st
import requests
import pandas as pd

response = requests.get(
    url='https://sales-dashboard-api-4ci8.onrender.com/preview_data'
)

# print(response.status_code)

st.title('Retail Data Analysis - Sample Superstore📈💰📊')

st.set_page_config('Analysis Application', layout='wide')

st.sidebar.success('Select Page Above')

# st.write(""" 
# This application is used to analyse the retail data in order to obtain insights to make better business decisions
# """)

st.header('About The Application')

st.subheader('Project Overview')

st.write("""
This application is an end-to-end retail analytics platform built to explore and visualize Amazon sales data using modern data engineering and analytics tools.
The project demonstrates the complete data workflow:
""")

st.code('Data Acquisition → Data Cleaning → Database Storage → API Development → Interactive Dashboard', language=None)

st.markdown("""
The application was developed using:
* **Python** for data processing and analysis
* **Pandas** for data manipulation
* **SQLite** as the database layer
* **FastAPI** for backend API development
* **Streamlit** for interactive dashboard visualisation        
            
""")

st.divider()

st.subheader('Objectives of the Application')

st.markdown("""

The goal of the application is to provide business insights by answering questions such as:
* Which product categories generate the most revenue?
* Which regions are the most profitable?
* Which segments underperform despite high sales?
* Which cities and states generate the most revenue?
* Which sub-categories underperform despite strong sales?


            """)

st.divider()

st.subheader('Key Features')

st.markdown("""
* Interactive sales dashboard
* Profit and revenue analysis
* Regional performance tracking
* Database-driven analytics
* API-powered data access          
""")


st.divider()

st.header('About the Dataset')

st.subheader('Dataset Overview')
st.text('This project uses a sample Superstore retail sales dataset containing transactional information related to customer orders, product categories, regional performance, sales revenue, discounts, and profitability. The dataset provides insight into how products perform across different customer segments, cities, states, and regions. It is designed to support business intelligence and sales performance analysis within a retail environment.')
st.markdown("""

The dataset includes the following business-focused fileds:
* Shipping mode information
* Country, city, state, and region location data
* Quantity ordered
* Product categories and sub-categories
* Sales revenue and profit
* Customer and regional information                                
            
            """)



# ==========================
# Show preview data
#===========================

checkbox = st.checkbox(label='Show Preview Data', value=True)

if checkbox:

    data_preview = response.json()

    # print(type(data_preview))

    df_preview = pd.DataFrame(data_preview)

    st.dataframe(df_preview)




