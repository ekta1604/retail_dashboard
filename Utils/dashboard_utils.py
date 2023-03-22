import pandas as pd
def filter_by_date(df, start_date, end_date):
    return df[(df['InvoiceDate'] >= start_date) & (df['InvoiceDate'] <= end_date)]

def get_revenue_by_product(df, start_date, end_date):
    filtered_df = filter_by_date(df, start_date, end_date)
    return filtered_df.groupby(['StockCode', 'Description'])['Revenue'].sum().reset_index()

def get_revenue_by_country(df, start_date, end_date):
    filtered_df = filter_by_date(df, start_date, end_date)
    return filtered_df.groupby('Country')['Revenue'].sum().reset_index()

def get_revenue_by_month(df, start_date, end_date):
    filtered_df = filter_by_date(df, start_date, end_date)
    return filtered_df.groupby('month')['Revenue'].sum().reset_index()

def top_products(df, start_date, end_date):
    filtered_df = filter_by_date(df, start_date, end_date)
    y = filtered_df.groupby(['StockCode', 'Description'])['Revenue'].sum().reset_index()
    return y.sort_values('Revenue', ascending=False).head(5)

def bottom_products(df, start_date, end_date):
    filtered_df = filter_by_date(df, start_date, end_date)
    return filtered_df.groupby(['StockCode', 'Description'])['Revenue'].sum().reset_index().sort_values('Revenue', ascending=True).head(5)

def customers_per_day(df, start_date, end_date):
    filtered_df = filter_by_date(df, start_date, end_date)
    df['date_column'] = pd.to_datetime(df['date_column'].dt.date)
    return filtered_df.groupby('date_column')['CustomerID'].nunique().reset_index()

def avg_units_per_customer(df,start_date, end_date):
    filtered_df = filter_by_date(df, start_date, end_date)
    return filtered_df.groupby('CustomerID')['Quantity'].mean().reset_index()
    
def total_customers(df,start_date, end_date):
    filtered_df = filter_by_date(df, start_date, end_date)
    total_customers = filtered_df['CustomerID'].nunique()
    return total_customers

def avg_transaction_price(df,start_date, end_date):
    filtered_df = filter_by_date(df, start_date, end_date)
    return filtered_df.groupby('InvoiceNo')['Revenue'].sum().mean()
   



