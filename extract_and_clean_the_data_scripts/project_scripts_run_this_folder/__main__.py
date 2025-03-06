"""
Code to run a data extraction and cleaning pipeline from multiple sources.

Contains code to access, extract and clean sales data from multiple
data sources. Importing classes containing functions for each process,
before converting each data source into a Pandas dataframe.
Each dataframe is then uploaded to a PostgreSQL database as a new 
table. 

Example:
    Typical usage would be to run the full pipeline to extract data
    in one go. Run the full code by running the python file in the 
    project folder:

    $ python3 project_scripts

"""

import pandas as pd
from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

# Initialize a DatabaseConnector instance with example details.
db_connector = DatabaseConnector("db_creds.yaml", "sales_data", "example_password")

# Create engines.
rds_engine = db_connector.init_rds_engine()
pg_engine = db_connector.init_pg_engine()

# List and print tables.
tables_rds = db_connector.list_db_tables(rds_engine)
print(tables_rds)

# Extract and clean the 'legacy_users' table. 
db_extractor_users = DataExtractor('legacy_users', rds_engine)
users_df = db_extractor_users.read_rds_table()
clean_users_df = DataCleaning.clean_user_data(users_df)

# Print table info and first 10 rows.
print(clean_users_df.info())
print(clean_users_df.head(10))

# Upload the dataframe to a PostgreSQL database.
db_connector.upload_to_db(clean_users_df, 'dim_users')

# Extract and clean the card details.
pdf = DataExtractor.retrieve_pdf_data(
    'https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf'
)
cleaned_card_data = DataCleaning.clean_card_data(pdf)

# Print table info and first 10 rows.
print(cleaned_card_data.info())
print(cleaned_card_data.head(10))

# Upload the dataframe to a PostgreSQL database.
db_connector.upload_to_db(cleaned_card_data, 'dim_card_details')

# Return the number of stores from an API. 
store_number = DataExtractor.list_number_of_stores(
    number_of_stores_endpoint='https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores', 
    header_details={'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
)

# Extract each store's data into a dataframe.
list_of_store_data = list()
store_number_value = int(store_number['number_stores'])
# Iterate through the stores data from an API, using each store's number 
# to extract its data before adding to a dataframe.
for store_number in range(store_number_value):
    store_data_df = DataExtractor.retrieve_stores_data(
        retrieve_a_store_endpoint=f'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}',
        header_details={'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
    )
    list_of_store_data.append(store_data_df)
    combined_store_data_df = pd.concat(list_of_store_data, ignore_index=True)

# Clean the store data.
cleaned_store_data = DataCleaning.clean_store_data(combined_store_data_df)

# Print table info and first 10 rows.
print(cleaned_store_data.info())
print(cleaned_store_data.head(10))

# Upload to PostgreSQL database.
db_connector.upload_to_db(cleaned_store_data, 'dim_store_details')

# Extract and clean the product details from S3.
product_df = DataExtractor.extract_from_s3(
    's3://data-handling-public/products.csv'
)
converted_product_df = DataCleaning.convert_product_weights(product_df)
cleaned_product_df = DataCleaning.clean_products_data(converted_product_df)

# Print table info and first 10 rows.
print(cleaned_product_df.info())
print(cleaned_product_df.head(10))

# Upload to PostgreSQL database.
db_connector.upload_to_db(cleaned_product_df, 'dim_products')

# Extract and clean the orders table from the RDS.
db_extractor_orders = DataExtractor('orders_table', rds_engine)
orders_table_df = db_extractor_orders.read_rds_table()
cleaned_orders_table = DataCleaning.clean_orders_data(orders_table_df)

# Print table info and first 10 rows.
print(cleaned_orders_table.info())
print(cleaned_orders_table.head(10))

# Upload to PostgreSQL database.
db_connector.upload_to_db(cleaned_orders_table, 'orders_table')

# Extract and clean the date events data from JSON in S3.
date_events_df = DataExtractor.extract_json_from_s3()
cleaned_date_events_df = DataCleaning.clean_date_events_data(date_events_df)

# Print table info and first 10 rows.
print(cleaned_date_events_df.info())
print(cleaned_date_events_df.head(10))

# Upload to PostgreSQL database.
db_connector.upload_to_db(cleaned_date_events_df, 'dim_date_times')