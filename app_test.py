import pandas as pd
import datetime
import streamlit as st
from Utils.dashboard_utils import *

with st.form(key='date_range'):
    # Set default start and end dates to today
    today = datetime.date.today()
    start_date = st.date_input('Start date', today)
    end_date = st.date_input('End date', today)

    # Add a submit button to run the functions with the selected dates
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    df = pd.read_csv(r"C:\Users\archi\OneDrive\Desktop\retail_dashboard\new_csv_file.csv")

    revenue_by_product = get_revenue_by_product(df, start_date, end_date)
    st.write('Revenue by product:')
    st.write(revenue_by_product)

    revenue_by_country = get_revenue_by_country(df, start_date, end_date)
    st.write('Revenue by country:')
    st.write(revenue_by_country)

    revenue_by_month = get_revenue_by_month(df, start_date, end_date)
    st.write('Revenue by month:')
    st.write(revenue_by_month)

    top_5_products = top_products(df, start_date, end_date)
    st.write('Top 5 products:')
    st.write(top_5_products)

    bottom_5_products = bottom_products(df, start_date, end_date)
    st.write('Bottom 5 products:')
    st.write(bottom_5_products)

    customers_per_day = customers_per_day(df, start_date, end_date)
    st.write('Customers per day:')
    st.write(customers_per_day)

    avg_units_per_customer = avg_units_per_customer(df, start_date, end_date)
    st.write('Average units per customer:')
    st.write(avg_units_per_customer)

    total_customers = total_customers(df, start_date, end_date)
    st.write('Total customers:')
    st.write(total_customers)

    avg_transaction_price = avg_transaction_price(df, start_date, end_date)
    st.write('Average transaction price:')
    st.write(avg_transaction_price)
