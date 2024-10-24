import boto3
import pandas as pd
import requests
import tabula


class DataExtractor:

    def read_rds_table(table_name, engine):
        df = pd.read_sql_table(table_name, engine)
        return df
    
    def retrieve_pdf_data():
        pdf = tabula.read_pdf('https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf', pages='all')
        pdf_df = pd.concat(pdf)
        return pdf_df

    def list_number_of_stores(number_of_stores_endpoint, header_details):
        response = requests.get(number_of_stores_endpoint, headers=header_details)
        if response.status_code == 200:
            number_of_stores = response.json()
        return number_of_stores
    
    def retrieve_stores_data(retrieve_a_store_endpoint, header_details):
        response = requests.get(retrieve_a_store_endpoint, headers=header_details)
        store_data = response.json()
        store_data_df = pd.DataFrame(data=store_data, index=[0])
        return store_data_df
    
    def extract_from_s3(s3_address):
        s3_address_split = s3_address.split('/')
        s3 = boto3.client('s3')
        s3.download_file(s3_address_split[2], s3_address_split[3], s3_address_split[3])
        file_df = (pd.read_csv(s3_address_split[3]))
        return file_df

    def extract_json_from_s3():
        s3 = boto3.client('s3')
        s3.download_file('data-handling-public', 'date_details.json', 'date_details.json')
        json_as_df = (pd.read_json('date_details.json'))
        return json_as_df
        
    

# if __name__ == '__main__':
    # connection = DatabaseConnector()
    # credentials = connection.read_db_creds()
    # engine = connection.init_db_engine(credentials)
    # users_df_t = DataExtractor.read_rds_table('legacy_users', engine)
    # users_df_t[['date_of_birth', 'join_date']] = users_df_t[['date_of_birth', 'join_date']].apply(pd.to_datetime, errors='coerce', dayfirst=True, format='mixed')
    # users_df_drop = users_df_t.dropna()
    # print(users_df_drop.info())

    
 