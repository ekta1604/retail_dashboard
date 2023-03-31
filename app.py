import pandas as pd
import datetime
import streamlit as st
from Utils.dashboard_utils import *
import plotly.express as px

df = pd.read_csv(r"C:\Users\archi\OneDrive\Desktop\retail_dashboard\new_csv_file.csv")
st.set_page_config(page_title="Retail-store Dashboard",
               page_icon=":bar_chart:",
               layout="wide")


#st.title("Date")

st.sidebar.header("Please Filter Here:")
with st.sidebar.form("my_form"):
    
    start_date = st.date_input("Start date", datetime.date(2011, 9, 12))
    end_date = st.date_input("End date", datetime.date(2012, 1, 10))
    Country = st.multiselect("Select the Country:",
                            options=df["Country"].unique(),
                            default=df["Country"].unique())
    submit_button = st.form_submit_button(label='Submit')


if submit_button and start_date <= end_date:
    st.success(f"Start date: {start_date}  \nEnd date: {end_date}")
    
    filter_by_date=filter_by_date(df,start_date,end_date)
    df = df[df["Country"].isin(Country)]
    
    total_customers_col, avg_units_per_customer_col, avg_transaction_price_col = st.columns(3)
    
    total_customers = total_customers(df, start_date, end_date)
    total_customers_value = round(float(total_customers), 2)
    delta_customers = round(total_customers_value - 10)
    total_customers_col.metric(label="Total Customers ⏳", value=total_customers_value, delta=delta_customers)

    avg_units_per_customer_df = avg_units_per_customer(df, start_date, end_date)
    avg_units_per_customer_value = round(float(avg_units_per_customer_df['Quantity'].mean()), 2)
    avg_units_per_customer_metric = avg_units_per_customer_col.metric(label="Avg Units Per Customer 🛒", value=avg_units_per_customer_value)

    avg_transaction_price = avg_transaction_price(df,start_date, end_date)
    avg_transaction_price_col.metric(label="Avg Transaction Price 💰", value=round(float(avg_transaction_price)))
    
    revenue_by_product = get_revenue_by_product(df, start_date, end_date)
    #st.write(revenue_by_product)
    fig = px.bar(revenue_by_product, x='Description', y='Revenue')
    #st.plotly_chart(fig)

    revenue_by_month = get_revenue_by_month(df, start_date, end_date)
    # st.write(revenue_by_month)
    fig1 = px.pie(revenue_by_month, values='Revenue',names='month',hole=0.6)
    #st.plotly_chart(fig1)
    
    top_5_products = top_products(df, start_date, end_date)
        
    bottom_5_products = bottom_products(df, start_date, end_date)
        
    # Get revenue by time
    revenue_by_day_df = revenue_by_day(df, start_date, end_date)
    fig2 = px.bar(revenue_by_day_df, x="Hour", y="Revenue")
    #st.plotly_chart(fig2)

    customers_per_day = customers_per_day(df, start_date, end_date)
    # st.write(customers_per_day)
    fig4 = px.line(customers_per_day, x='InvoiceDate', y='CustomerID')
    #st.plotly_chart(fig4)
    
    # Group the data by customer ID and calculate the total revenue for each customer
    customer_revenue = df.groupby("CustomerID")["Revenue"].sum()

    # Sort the list of customer revenues in descending order
    sorted_revenue = customer_revenue.sort_values(ascending=False)

    # Select the top 3 customers from the sorted list
    top_3_customers = sorted_revenue.head(3)

    # Create a Streamlit app and display the top 3 customers
    st.write("Top 3 Customers by Revenue")
    st.write(top_3_customers)
    
    container1 = st.container()
    col1, col2 = st.columns(2)

    with container1:
        with col1:
            st.write('Revenue by Product:')
            fig
        with col2:
            st.write('Revenue by Month:')
            fig1


    container2 = st.container()
    col3, col4 = st.columns(2)

    with container2:
        with col3:
            st.write("Top 5 Products")
            st.table(top_5_products)
        with col4:
            st.write('Bottom 5 products:')
            st.table(bottom_5_products)
        
    container3 = st.container()
    col5, col6 = st.columns(2)
    
    with container2:
        with col5:
            st.write('Customers per day:')
            fig4
        with col6:
            st.write('Hourly Revenue')
            fig2
        

elif submit_button and start_date > end_date:
    st.error("Error: End date must be after start date.")