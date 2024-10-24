"""
Clean data retrieved and extracted from retail business's varied data sources.

Classes:
    DataCleaning

Functions:
    remove_null_values(object) -> pandas.Dataframe
    clean_user_data(object) -> pandas.Dataframe
    clean_card_data(object) -> pandas.Dataframe
    clean_store_data(object) -> ppandas.Dataframe
    weight_conversion(object) -> string
    convert_product_weights(object) -> pandas.Dataframe
    clean_products_data(object) -> pandas.Dataframe
    clean_orders_data(object) -> pandas.Dataframe
    clean_date_events_data(object) -> pandas.Dataframe
"""

import numpy as np
import pandas as pd


class DataCleaning:

    def remove_null_values(df):
        df = df.replace('NULL', np.nan)
        df = df.dropna(how='all')
        return df
    
    def clean_user_data(df):
        df = DataCleaning.remove_null_values(df)
        df.join_date = pd.to_datetime(df.join_date, errors='coerce', dayfirst=True, format='mixed')
        df = df.dropna()
        df['country_code'] = df['country_code'].str.replace('GGB', 'GB')
        return df
    
    def clean_card_data(df):
        df = DataCleaning.remove_null_values(df)
        df.date_payment_confirmed = pd.to_datetime(df.date_payment_confirmed, errors='coerce', dayfirst=True, format='mixed')
        df = df.dropna()
        df = df.astype({'card_number': 'string'})
        df['card_number'] = df['card_number'].str.replace('?', '')
        df['card_number'] = df['card_number'].astype(int)
        df = df.drop_duplicates(subset='card_number')
        return df
    
    def clean_store_data(df):
        df = DataCleaning.remove_null_values(df)
        # df = df.drop(['lat'], axis=1)
        df.opening_date = pd.to_datetime(df.opening_date, errors='coerce', dayfirst=True, format='mixed')
        df = df.dropna(subset=['opening_date'])
        df['continent'] = df['continent'].str.replace('eeAmerica', 'America')
        df['continent'] = df['continent'].str.replace('eeEurope', 'Europe')
        df['staff_numbers'] = df['staff_numbers'].str.strip()
        df['staff_numbers'] = df['staff_numbers'].str.replace(r'[^0-9]+', '', regex=True)
        df['staff_numbers'] = df['staff_numbers'].astype(int)
        return df
    
    def weight_conversion(weight):
                if 'x' in weight:
                    weight = weight.replace('g', '')
                    split_list = weight.split('x')
                    weight = float(split_list[0]) * float(split_list[1])
                    weight = float(weight) / 1000 
                elif weight.endswith('.'):
                    weight = weight.replace('g .', '')
                    weight = float(weight) / 1000
                elif weight.endswith('kg'):  
                    weight = weight.replace('kg', '')
                    weight = float(weight)
                elif weight.endswith('g'):
                    weight = weight.replace('g', '')
                    weight = float(weight) / 1000
                elif weight.endswith('oz'):
                    weight = weight.replace('oz', '')
                    weight = float(weight) / 35.274
                return weight

    def convert_product_weights(df):
        df = DataCleaning.remove_null_values(df)
        # As the products.csv alraedy includes an 'index' column without any NULL values, 
        # this specific funtions requires a .dropna() with threshold set to 2 to remove rows containing NULLs other than the index column. 
        df = df.dropna(thresh=2)
        df['weight'] = df['weight'].str.strip()
        df['weight'] = df['weight'].str.replace('ml', 'g')
        df['weight'] = df['weight'].apply(DataCleaning.weight_conversion)
        return df

    def clean_products_data(df):
        df = DataCleaning.remove_null_values(df)
        df.date_added = pd.to_datetime(df.date_added, errors='coerce', dayfirst=True, format='mixed')
        df = df.dropna(subset=['date_added'])
        df = df.astype({'weight' : 'float'})
        return df
    
    def clean_orders_data(df): 
        df = DataCleaning.remove_null_values(df)
        df = df.drop(columns=['first_name', 'last_name', '1'])
        return df
   
    def clean_date_events_data(df):
        df = DataCleaning.remove_null_values(df)
        df['date_timestamp'] = pd.to_datetime(df['year'] + '-' + df['month'] + '-' + df['day'] + ' ' + df['timestamp'], errors='coerce')
        df[['year', 'month', 'day']] = df[['year', 'month', 'day']].apply(pd.to_numeric, errors='coerce')
        df = df.dropna() 
        df = df.astype({'year': 'int', 'month': 'int', 'day' : 'int'})
        return df
    

        
      



