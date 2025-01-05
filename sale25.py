import pandas as pd
import streamlit as st
import plotly.express as px
st.set_page_config(page_title='My Sale Dashboard',page_icon=':bar_chart:',layout='wide')
df = pd.read_csv('all_df.csv')
st.sidebar.header('Please Filter Here')
product_name = st.sidebar.multiselect(
    "Select Product:",
    options = df['Product'].unique(),
    default = df['Product'].unique()[:5]
)
city_name = st.sidebar.multiselect(
    "Select City:",
    options = df['City'].unique(),
    default = df['City'].unique()[:5]
)
month_name = st.sidebar.multiselect(
    "Select Month",
    options = df['Month'].unique(),
    default = df['Month'].unique()[:5]
)
st.title(':bar_chart: Sales Dashboard for 2019')
total_sales = df['Total'].sum()
total_product = df['Product'].nunique()
a,b = st.columns(2)
with a:
    st.subheader('Total Sales')
    st.subheader(f'US $ {total_sales}')
with b:
    st.subheader('No. of Product')
    st.subheader(total_product)
selection = df.query('City == @city_name and Product == @product_name and Month == @month_name')
total_sale_by_product = selection.groupby('Product') ['Total'].sum().sort_values()
fig_by_product = px.bar(
    total_sale_by_product,
    x =  total_sale_by_product.values,
    y =  total_sale_by_product.index,
    title = 'Sales by Product'
)
c,d,e = st.columns(3)
c.plotly_chart(fig_by_product,use_container_width = True)

fig_by_city = px.pie(
    selection, 
    values='Total', 
    names='City', 
    title='Sales of City')
d.plotly_chart(fig_by_city,use_container_width = True)

total_sale_by_month = selection.groupby('Month') ['Total'].sum().sort_values()
fig_by_month = px.bar(
    total_sale_by_month,
    x =  total_sale_by_month.values,
    y =  total_sale_by_month.index,
    title = 'Sales by Month'
)
e.plotly_chart(fig_by_month,use_container_width = True)

f,g = st.columns(2)
fig_by_line_month = px.line(
    total_sale_by_month,
    x =  total_sale_by_month.values,
    y =  total_sale_by_month.index,
    title = 'Sales by Month')
f.plotly_chart(fig_by_line_month,use_container_width = True)

fig_by_quantityOrdered = px.scatter(
    selection,
    x =  'Total',
    y =  'QuantityOrdered',
    title = 'Total Sale Amount')
g.plotly_chart(fig_by_quantityOrdered,use_container_width = True)