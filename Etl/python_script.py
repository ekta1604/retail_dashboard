import pandas as pd

def extract_day(df):
    df['day'] = pd.to_datetime(df['InvoiceDate']).dt.day
    return df

def extract_month(df):
    df['month'] = pd.to_datetime(df['InvoiceDate']).dt.month
    return df

def extract_time(df):
    df['time'] = pd.to_datetime(df['InvoiceDate']).dt.time
    return df

def extract_date(df):
    df['date'] = pd.to_datetime(df['InvoiceDate']).dt.date
    return df

def extract_quarter(df):
    df['quarter'] = pd.to_datetime(df['InvoiceDate']).dt.quarter
    return df

def drop_null_values(df):
    df = df.dropna()
    return df

# Read CSV file
df = pd.read_csv("C:/Users/archi/OneDrive/Desktop/retail_dashboard/OnlineRetail.xlsx - Online Retail.csv")

# Apply functions to extract additional columns
df = extract_day(df)
df = extract_month(df)
df = extract_time(df)
df = extract_date(df)
df = extract_quarter(df)

# Drop rows with null values
df = drop_null_values(df)

# Output resulting DataFrame to new CSV file
df.to_csv('new_csv_file.csv', index=False)
