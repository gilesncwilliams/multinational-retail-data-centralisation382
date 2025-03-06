"""
Functions to extract data from a variety of data sources.

Classes:
    DataExtractor

"""

import boto3
import pandas as pd
import requests
import tabula


class DataExtractor:
    """Class for data extraction and conversion to a Pandas dataframe.
    
    Contains multiple functions for retrieveing or extracting data
    from AWS RDS, S3, API, and converting PDF, JSON and CSV files 
    into Pandas dataframes prior to cleaning. 

    The staticmethods are specific to the extraction of those
    individual table from the RDS database.

    Functions:
    read_rds_table(rds sql table) -> pandas.Dataframe
    retrieve_pdf_data(pdf flie) -> pandas.Dataframe
    list_number_of_stores(api connection) -> integer
    retrieve_stores_data(api connection) -> pandas.Dataframe
    extract_from_S3 (csv) -> pandas.Dataframe
    extract_json_from_S3(json) -> pandas.Dataframe

    """

    def __init__(self, table_name, rds_engine):
        """Initializes the DataExtractor class with a table name and engine.

            Args:
                table_name (str): The name of the RDS table to be read.
                rds_engine (str): The RDS engine connection.
        """
        self.table_name = table_name
        self.rds_engine = rds_engine

    def read_rds_table(self):
        """Reads an AWS RDS database table.
    
        Args:
            table_name: the name of the table from the RDS database to extract.
            engine: the sqlalchemy connection engine for the RDS database.

        Returns:
            df: a Pandas dataframe.
        """
        df = pd.read_sql_table(self.table_name, self.rds_engine)
        return df
    
    @staticmethod
    def retrieve_pdf_data(pdf_url):
        """Reads a pdf file and converts to a Pandas dataframe.
    
        Uses the tabula-py package to extract data from a pdf 
        before converting into a Pandas dataframe.

        Returns:
            pdf_df: a Pandas dataframe.
        """
        pdf = tabula.read_pdf(pdf_url, pages='all')
        pdf_df = pd.concat(pdf)
        return pdf_df
    
    @staticmethod
    def list_number_of_stores(number_of_stores_endpoint, header_details):
        """Lists the number of stores using an API get method.
    
        Uses the Requests package to extract data from an API and 
        returns the number of stores.

        Args:
            number_of_stores_endpoint: the API's endpoint
            headers: a dictionary of the API's header details.

        Returns:
            number_of_stores: an integer of the number of stores.
        """
        response = requests.get(number_of_stores_endpoint, headers=header_details)
        if response.status_code == 200:
            number_of_stores = response.json()
        return number_of_stores
    
    @staticmethod
    def retrieve_stores_data(retrieve_a_store_endpoint, header_details):
        """Retrieves data for a retail store from it's API endpoint.
    
        Uses the Requests package to extract data from an API 
        and returns the store data.

        Args:
            retrieve_a_store_endpoint: the API endpoint for each store.
            headers: a dictionary of the API's header details.

        Returns:
            store_data_df: a Pandas dataframe of the store data.
        """
        response = requests.get(
            retrieve_a_store_endpoint,
            headers=header_details
        )
        store_data = response.json()
        store_data_df = pd.DataFrame(data=store_data, index=[0])
        return store_data_df
    
    @staticmethod
    def extract_from_s3(s3_address):
        """Extract data from an AWS S3 bucket and converts to Pandas dataframe.
    
        Uses the boto3 package to connect to AWS S3 bucket from its URL,
        and then extracts data from a CSV file.

        Args:
            file_df: a Pandas dataframe.
    
        Returns:
            store_data_df: a Pandas dataframe of the store data.
        """
        s3_address_split = s3_address.split('/')
        s3 = boto3.client('s3')
        s3.download_file(
            s3_address_split[2],
            s3_address_split[3],
            s3_address_split[3]
        )
        file_df = (pd.read_csv(s3_address_split[3]))
        return file_df

    @staticmethod
    def extract_json_from_s3():
        """Extract data from a JSON file on S3 and converts to Pandas dataframe.

        Uses the boto3 package to connect to AWS S3 bucket from its URL, 
        and extract data from a JSON file. The URL in this case was not extracted 
        using the .split() method and instead has been manually entered 
        for this specific connection. 
        Those conncection details will need to be update for a different AWS URL
        if using this function for another S3 bucket.

        Returns:
            json_as_df: a Pandas dataframe of the store data.
        """
        s3 = boto3.client('s3')
        # The URL has been split up manually into the required arguements for the boto3 download function.
        s3.download_file(
            'data-handling-public', 
            'date_details.json', 
            'date_details.json'
        )
        json_as_df = (pd.read_json('date_details.json'))
        return json_as_df
        
    
 