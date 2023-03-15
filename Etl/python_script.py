import os
import pandas as pd

# Set the path to your source and destination folders
source_folder = "C:/Users/archi/OneDrive/Desktop/Internship/sftp"
destination_folder = "C:/Users/archi/OneDrive/Desktop/Internship/processed_transaction"

# Loop through each file in the source folder
for filename in os.listdir(source_folder):
    # Check if the file is a CSV file
    if filename.endswith('.csv'):

        # Create the full path to the input and output files
        input_path = os.path.join(source_folder, "OnlineRetail.xlsx.csv")
        
        
        # Read the input CSV file into a Pandas DataFrame
        df = pd.read_csv(input_path)

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

        # Apply functions to extract additional columns
        df = extract_day(df)
        df = extract_month(df)
        df = extract_time(df)
        df = extract_date(df)
        df = extract_quarter(df)

        # Drop rows with null values
        df = drop_null_values(df)

        # Output resulting DataFrame to new CSV file
        #df.to_csv('new_csv_file.csv', index=False)

        # Write the processed data to the output CSV file
        df.to_csv(os.path.join(destination_folder, 'new_csv_file'), index=False)

