"""
Clean data extracted from a retail business's varied data sources.

Contains multiple function for data cleaning Pandas Dataframes based on 
specific cleaning requirements for each data source of sales data. 

Classes:
    DataCleaning

"""

import numpy as np
import pandas as pd


class DataCleaning:
    """Class containing data cleaning functions.

    Each of the multiple data sources created by the business needs specific 
    data cleaning functions applied to it before uploading to a new SQL 
    database for analysis.

    Functions:
    remove_null_values(pandas.Dataframe) -> pandas.Dataframe
    clean_user_data(pandas.Dataframe) -> pandas.Dataframe
    clean_card_data(pandas.Dataframe) -> pandas.Dataframe
    clean_store_data(pandas.Dataframe) -> pandas.Dataframe
    weight_conversion(object) -> string
    convert_product_weights(pandas.Dataframe) -> pandas.Dataframe
    clean_products_data(pandas.Dataframe) -> pandas.Dataframe
    clean_orders_data(pandas.Dataframe) -> pandas.Dataframe
    clean_date_events_data(pandas.Dataframe) -> pandas.Dataframe

    """

    @staticmethod    
    def remove_null_values(df):
        """Removes rows containing only NULL values from the table.

        Converts any text written as, for example, 'N/A' or 'NULL' into a NULL value.
        Then subsequently drops those rows that contain all NULL values 
        across all the columns as not required in the database.

        Args:
            df: a Pandas dataframe

        Returns:
            df: a Pandas dataframe  
        """
        df = df.replace('NULL', np.nan)
        df = df.dropna(how='all')
        return df
    
    @staticmethod
    def clean_user_data(df):
        """Applies data cleaning functions to the customer user data.

       Applies the remove_null_values function to the dataframe.
       Converts the 'join_date' column values to a datetime data type. 
       Any errors are coerced to NULL, then drops rows with those NULL
       datetime values. Then fixes typing errors for some of the country
       code inputs.

        Args:
            df: a Pandas dataframe

        Returns:
            df: a Pandas dataframe  
        """ 
        df = DataCleaning.remove_null_values(df)
        df.join_date = pd.to_datetime(
            df.join_date, 
            errors='coerce', 
            dayfirst=True, 
            format='mixed'
        )
        df = df.dropna()
        df['country_code'] = df['country_code'].str.replace('GGB', 'GB')
        return df
    
    @staticmethod
    def clean_card_data(df):
        """Applies data cleaning functions to the users' credit card data.

        Applies the remove_null_values function to the dataframe.
        Converts the 'date_payment_confirmed' column values to a datetime data type. 
        Any errors are coerced to NULL, then drops rows with those NULL datetime values.
        Then fixes typing errors for some of the card_number inputs before converting 
        to integer data type and dropping any duplicate card numbers.

        Args:
            df: a Pandas dataframe

        Returns:
            df: a Pandas dataframe  
        """ 
        df = DataCleaning.remove_null_values(df)
        df.date_payment_confirmed = pd.to_datetime(
            df.date_payment_confirmed, 
            errors='coerce', 
            dayfirst=True, 
            format='mixed'
        )
        df = df.dropna()
        # fixes the card number errors 
        df = df.astype({'card_number': 'string'})
        df['card_number'] = df['card_number'].str.replace('?', '')
        df['card_number'] = df['card_number'].astype(int)
        df = df.drop_duplicates(subset='card_number')
        return df
    
    @staticmethod
    def clean_store_data(df):
        """Applies data cleaning functions to the retail business's store data.

        Applies the remove_null_values function to the dataframe.
        Converts the 'opening_date' column values to a datetime data type. 
        Any errors are coerced to NULL, then drops rows with those NULL datetime values.
        Then fixes typing errors for some of the continent and staff number inputs.

        Args:
            df: a Pandas dataframe

        Returns:
            df: a Pandas dataframe  
        """ 

        # Remove rows with null values using the custom DataCleaning method
        df = DataCleaning.remove_null_values(df)

        # Convert the 'opening_date' column to datetime, handling errors and specifying the format
        df.opening_date = pd.to_datetime(
            df.opening_date,
            errors='coerce',  # Coerce invalid dates into NaT (Not a Time)
            dayfirst=True,   
            format='mixed'    
        )

        # Drop rows where 'opening_date' is NaT (after coercion of invalid dates)
        df = df.dropna(subset=['opening_date'])

        # Replace occurrences of 'eeAmerica' with 'America' in the 'continent' column
        df['continent'] = df['continent'].str.replace('eeAmerica', 'America')

        # Replace occurrences of 'eeEurope' with 'Europe' in the 'continent' column
        df['continent'] = df['continent'].str.replace('eeEurope', 'Europe')

        # Strip leading and trailing spaces from the 'staff_numbers' column
        df['staff_numbers'] = df['staff_numbers'].str.strip()

        # Replace non-numeric characters with an empty string (keeping only numbers) in 'staff_numbers'
        df['staff_numbers'] = df['staff_numbers'].str.replace(
            r'[^0-9]+', '',  # Regex to match anything that is not a number
            regex=True        # Ensure regex replacement
        )

        # Convert the 'staff_numbers' column to an integer type
        df['staff_numbers'] = df['staff_numbers'].astype(int)

        # Return the cleaned DataFrame
        return df


    
    @staticmethod
    def weight_conversion(weight):
        """Applies weight conversion functions to weight of products.

        Removes any non-digit characters from strings and converts any
        product weight measurements not already in kilograms.

        Args:
            weight: a string of weights and their measurements

        Returns:
            weight: a string of converted weights in kilograms  
        """         
        if 'x' in weight:
        # Converts product items in multi-packs to their total weight in kilograms.
            weight = weight.replace('g', '')
            split_list = weight.split('x')
            weight = float(split_list[0]) * float(split_list[1])
            weight = float(weight) / 1000
        # Converts any product weights in grams with additional '.' characters to kilograms.
        elif weight.endswith('.'):
            weight = weight.replace('g .', '')
            weight = float(weight) / 1000
        # Removes 'kg' from any weights already in kilograms.
        elif weight.endswith('kg'):  
            weight = weight.replace('kg', '')
            weight = float(weight)
        # Converts any product weigths in grams to kilograms.
        elif weight.endswith('g'):
            weight = weight.replace('g', '')
            weight = float(weight) / 1000
        # Converts any product weights in ounces to kilograms.
        elif weight.endswith('oz'):
            weight = weight.replace('oz', '')
            weight = float(weight) / 35.274
        return weight

    @staticmethod
    def convert_product_weights(df):
        """Removes whitespace and null columns and applies weight conversion.

        Removes whitespace and null columns from the product data and applies 
        the weight_conversion() function to the weight column.
        
        Args:
            df: a Pandas dataframe

        Returns:
            df: a Pandas dataframe  
        """ 
        df = DataCleaning.remove_null_values(df)
        # As the products.csv alraedy includes an 'index' column without any NULL values, 
        # this specific funtions requires a .dropna() with threshold set to 2 to 
        # remove rows containing NULLs other than the index column. 
        df = df.dropna(thresh=2)
        df['weight'] = df['weight'].str.strip()
        df['weight'] = df['weight'].str.replace('ml', 'g')
        df['weight'] = df['weight'].apply(DataCleaning.weight_conversion)
        return df

    @staticmethod
    def clean_products_data(df):
        """Applies data cleaning functions to the product data.

        Re-applies the remove_null_values function to the dataframe, 
        just to catch any null values created by the weight conversion. 
        Then converts the 'opening_date' column values to a datetime data type. 
        Any errors are coerced to NULL, then drops rows with those NULL datetime values.
        Before finally converting the weight datatype to float.

        Args:
            df: a Pandas dataframe

        Returns:
            df: a Pandas dataframe  
        """ 
        df = DataCleaning.remove_null_values(df)
        df.date_added = pd.to_datetime(
            df.date_added,
            errors='coerce',
            dayfirst=True,
            format='mixed')
        df = df.dropna(subset=['date_added'])
        df = df.astype({'weight' : 'float'})
        return df
    
    @staticmethod
    def clean_orders_data(df):
        """Applies data cleaning functions to the sales orders data.

        Applies the remove_null_values function to the dataframe. 
        Then removes columns that are not required.

        Args:
            df: a Pandas dataframe

        Returns:
            df: a Pandas dataframe  
        """  
        df = DataCleaning.remove_null_values(df)
        df = df.drop(columns=['first_name', 'last_name', '1'])
        return df
   
    @staticmethod
    def clean_date_events_data(df):
        """Applies data cleaning functions to the sales orders date events data.

        Applies the remove_null_values function to the dataframe. 
        Then creates a new 'date_timestamp' column from the existing 'year', 
        'month' and 'day' columns. Before converting those same columns to 
        integer data types and removing any rows containing NULL values.

        Args:
            df: a Pandas dataframe

        Returns:
            df: a Pandas dataframe  
        """  
        df = DataCleaning.remove_null_values(df)
        df['date_timestamp'] = pd.to_datetime(
            df['year'] + '-' + df['month'] + '-' + df['day'] + ' ' + df['timestamp'],
            errors='coerce'
        )
        df[['year', 'month', 'day']] = df[['year', 'month', 'day']].apply(
            pd.to_numeric, errors='coerce'
        )
        df = df.dropna() 
        df = df.astype({'year': 'int', 'month': 'int', 'day' : 'int'})
        return df
    

        
      



