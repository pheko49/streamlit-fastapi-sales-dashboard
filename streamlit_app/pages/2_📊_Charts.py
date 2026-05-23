import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config('Analysis Application', layout='wide')

st.title('📊Visual Insights')

#========================================================================
# SECTION 1 - http request for sales by region
#========================================================================

# url for sales by region
url_sales_by_region = 'https://sales-dashboard-api-4ci8.onrender.com/sales_by_region'

response_sales_by_region = requests.get(url=url_sales_by_region)

# return json format
data_sales_by_region = response_sales_by_region.json()

# Convert to dataframe from json
df_sales_region = pd.DataFrame(data=data_sales_by_region)

#========================================================================
# SECTION 2 - http request for profit by region
#========================================================================

# url for profit by category
url_profit_by_category = 'https://sales-dashboard-api-4ci8.onrender.com/profit_by_category'

response_profit_by_category = requests.get(url=url_profit_by_category)

# Convert to json
data_profit_by_region = response_profit_by_category.json()

# Convert json to dataframe
df_profit_by_category = pd.DataFrame(data=data_profit_by_region)

#========================================================================
# SECTION 3 - http request for profit by segment
#========================================================================

# url profit by segment
url_profit_by_segment = 'https://sales-dashboard-api-4ci8.onrender.com/profit_by_segment'

response_profit_by_segment = requests.get(url=url_profit_by_segment)

# Convert to json
data_full_dataset = response_profit_by_segment.json()

# Convert json to dataframe
df_profit_by_segment = pd.DataFrame(data=data_full_dataset)

#========================================================================
# SECTION 4 - http request for top sales by State
#========================================================================

# url top sales by state
url_top_sales_by_state = 'https://sales-dashboard-api-4ci8.onrender.com/top_state_sales'

response_top_sales_by_state = requests.get(url=url_top_sales_by_state)

# Convert to json
data_top_sales_by_state = response_top_sales_by_state.json()

# Convert json to dataframe
df_top_sales_by_state = pd.DataFrame(data=data_top_sales_by_state)

# re-order totals sales as streamlit by default re-orders
# df_top_sales_by_state = df_top_sales_by_state.sort_values(
#     by='total_sales',
#     ascending=False
# ).reset_index(drop=True)

#===============
# CHARTS
# ==============

chart_col1, chart_col2 = st.columns(2)

chart_col1.subheader('Sales by Region')
chart_col1.bar_chart(df_sales_region,x='Region', y='total_sales')

chart_col2.subheader('Profit by Category')
chart_col2.bar_chart(df_profit_by_category, x='Category', y='total_profit')

st.divider()

chart_col3, chart_col4 = st.columns(2)

chart_col3.subheader('Profit by Segment')
chart_col3.bar_chart(df_profit_by_segment, x='Segment', y='total_profit')


# Use plotly as bar chart re-orders the order automatically and cant be rectified

fig = px.bar(
    df_top_sales_by_state,
    x='State',
    y='total_sales',
    title='Top 10 States by Sales',
    # orientation='h'
)

chart_col4.plotly_chart(
    fig,
    use_container_width=True
)
# chart_col4.subheader('Top 10 States by Sales')
# chart_col4.bar_chart(df_top_sales_by_state, x='State', y='total_sales')