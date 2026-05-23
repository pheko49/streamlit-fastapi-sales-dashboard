import streamlit as st
import pandas as pd
import requests

st.set_page_config('Analysis Application', layout='wide')

url = 'https://sales-dashboard-api-4ci8.onrender.com/superstore_data'

response = requests.get(url=url)


data = response.json()

df = pd.DataFrame(data=data)

# Page title
st.title('🎯 KPI Summary')

# KPI calculations
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = len(df)
avg_discount = df['Discount'].mean() * 100

# Create KPI columns
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    'Total Sales',
    f"${total_sales:,.0f}"
)

col2.metric(
    'Total Profit',
    f"${total_profit:,.0f}"
)

col3.metric(
    'Total Orders',
    f"{total_orders:,}"
)

col4.metric(
    'Average Discount',
    f"{avg_discount:.1f}%"
)

st.divider()

best_region = (
    df.groupby('Region')['Profit'].sum().idxmax()
)

top_category = (
    df.groupby('Category')['Sales'].sum().idxmax()
)

worst_subcategory = (
    df.groupby('Sub-Category')['Sales'].sum().idxmin()
)

st.subheader('📌 Business Insights')

insight_col1, insight_col2, insight_col3 = st.columns(3)

insight_col1.success(
    f'🏆 Best Region: {best_region}'
)

insight_col2.info(
    f'📦 Top Category: {top_category}'
)

insight_col3.error(
    f'⚠️ Weakest Sub-Category: {worst_subcategory}'
)

