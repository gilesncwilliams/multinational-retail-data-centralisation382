import pandas as pd
from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

# below code is for task 3 - extact the user data from RDS. The first part is setting up the connection, then extracting the list of table
# credentials = DatabaseConnector.read_db_creds()
# engine = DatabaseConnector.init_db_engine(credentials)
# list_of_tables = DatabaseConnector.list_db_tables(engine)
# print(list_of_tables)

# # this next part of code is reading the required table, cleaning and uploading
# users_info_df = DataExtractor.read_rds_table('legacy_users', engine)
# cleaned_database = DataCleaning.clean_user_data(users_info_df)

# print(cleaned_database.info())
# print(cleaned_database.head(50))

# DatabaseConnector.upload_to_db(cleaned_database, 'dim_users')

# # below code is for task 4 - extract card details
# pdf = DataExtractor.retrieve_pdf_data()
# cleaned_card_data = DataCleaning.clean_card_data(pdf)

# print(cleaned_card_data.info())
# print(cleaned_card_data.head(50))

# DatabaseConnector.upload_to_db(cleaned_card_data, 'dim_card_details')

# below code is for task 5 - return number of stores
# store_number = DataExtractor.list_number_of_stores(number_of_stores_endpoint='https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores', header_details={'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'})

# below code is for task 5 - extract each store data into a dataframe
# list_of_store_data = list()
# store_number_value = int(store_number['number_stores'])
# for store_number in range(store_number_value):
#     store_data_df = DataExtractor.retrieve_stores_data(retrieve_a_store_endpoint=f'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}', header_details={'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'})
#     list_of_store_data.append(store_data_df)
#     combined_store_data_df = pd.concat(list_of_store_data, ignore_index=True)

# cleaned_store_data = DataCleaning.clean_store_data(combined_store_data_df)

# print(cleaned_store_data.info())
# print(cleaned_store_data.head(50))

# DatabaseConnector.upload_to_db(cleaned_store_data, 'dim_store_details')

# below code is for task 6 - extract and clean the product details 
product_df = DataExtractor.extract_from_s3('s3://data-handling-public/products.csv')
converted_product_df = DataCleaning.convert_product_weights(product_df)
cleaned_product_df = DataCleaning.clean_products_data(converted_product_df)

print(cleaned_product_df.info())
print(cleaned_product_df.head(50))

DatabaseConnector.upload_to_db(cleaned_product_df, 'dim_products')

# below code is for task 7 - extract and clean the orders table
# credentials = DatabaseConnector.read_db_creds()
# engine = DatabaseConnector.init_db_engine(credentials)
# list_of_tables = DatabaseConnector.list_db_tables(engine)
# print(list_of_tables)

# orders_table_df = DataExtractor.read_rds_table('orders_table', engine)
# cleaned_orders_table = DataCleaning.clean_orders_data(orders_table_df)

# print(cleaned_orders_table.info())
# print(cleaned_orders_table.head(50))

# DatabaseConnector.upload_to_db(cleaned_orders_table, 'orders_table')

# task 8 code - extract and clean the date events data
# date_events_df = DataExtractor.extract_json_from_s3()
# cleaned_date_events_df = DataCleaning.clean_date_events_data(date_events_df)

# print(cleaned_date_events_df.info())
# print(cleaned_date_events_df.head(50))

# DatabaseConnector.upload_to_db(cleaned_date_events_df, 'dim_date_times')


