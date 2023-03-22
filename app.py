import pandas as pd
import datetime
import streamlit as st
from Utils.dashboard_utils import *

df = pd.read_csv(r"C:\Users\archi\OneDrive\Desktop\retail_dashboard\new_csv_file.csv")

with st.form("my_form"):
    start_date = st.date_input("Start date", datetime.date.today())

    end_date = st.date_input("End date", datetime.date.today() + datetime.timedelta(days=7))
    
    submit_button = st.form_submit_button(label='Submit')

if submit_button and start_date <= end_date:
    # do something with start_date and end_date
    st.success(f"Start date: {start_date}  \nEnd date: {end_date}")
elif submit_button and start_date > end_date:
    st.error("Error: End date must be after start date.")
   
# Call the functions with the user input
revenue_by_product = get_revenue_by_product(df, start_date, end_date)
print(revenue_by_product)

revenue_by_country = get_revenue_by_country(df, start_date, end_date)
print(revenue_by_country)

revenue_by_month = get_revenue_by_month(df, start_date, end_date)
print(revenue_by_month)

top_5_products = top_products(df, start_date, end_date)
print(top_5_products)

bottom_5_products = bottom_products(df, start_date, end_date)
print(bottom_5_products)

customers_per_day = customers_per_day(df, start_date, end_date)
print(customers_per_day)

avg_units_per_customer=avg_units_per_customer(df,start_date,end_date)
print(avg_units_per_customer)

total_customers=total_customers(df,start_date,end_date)
print(total_customers)

avg_transaction_price=avg_transaction_price(df,start_date,end_date)
print(avg_transaction_price)



