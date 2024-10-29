"""
Facilitates the connection to a PostgreSQL database.

Contains multiple function for data cleaning Pandas Dataframes based
on specific cleaning requirments for each data source of sales data. 

Classes:
    DatabaseConnector

Functions:
    read_db_creds(yaml file) -> dictionary
    init_db_engine(dictionary) -> sqlalchemy database engine
    list_db_tables(sqlalchemy database engine) -> list
    upload_to_db(pandas.Dataframe) -> sql
"""

from sqlalchemy import create_engine, inspect
import yaml


class DatabaseConnector:
    """Class for utility functions to connect to a PostgreSQL database."""

    def read_db_creds():
        """
        Reads credentials for an AWS RDS database from a yaml file.

        Returns:
            credentials: a dictionary of the database credentials  
        """
        with open('db_creds.yaml', 'r') as f:
            credentials = yaml.safe_load(f)
        return credentials

    def init_db_engine(credentials):
        """
        Initialises an sqlalchemy database engine.

        Args:
            credentials: a dictionary of the database credentials  
        
        Returns:
            engine: an sqlalchmey engine
        """
        engine = create_engine(f"postgresql+psycopg2://{credentials['RDS_USER']}:{credentials['RDS_PASSWORD']}@{credentials['RDS_HOST']}:{credentials['RDS_PORT']}/{credentials['RDS_DATABASE']}")
        return engine
    
    def list_db_tables(engine):
        """
        Creates a list of database tables from the database connection.

        Using SQLalchemy's inspect function to view the RDS database and 
        create a list of tables contained within it.

        Args:
            engine: sqlalchmey engine  
        
        Returns:
            inspector: a list of the table names
        """
        inspector = inspect(engine)
        return list(inspector.get_table_names())      
       
    def upload_to_db(cleaned_df, table_name):
        """
        Uploads a Pandas dataframe to a PostgreSQL database.

        Using the PostgreSQL's database details to upload a cleaned Pandas
        dataframe as a new table in the PostgreSQL database.
        Please update the required details below to connect to your
        database and upload the table. Including the password and database 
        name you assigned to the database.

        Args:
            cleaned_df: a Pandas dataframe 
            table_name: the name of the new table in the PostgreSQL database. 
        """
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        HOST = 'localhost'
        USER = 'postgres'
        # Insert your password here:
        PASSWORD = '{your password}'
        # Insert your database name here:
        DATABASE = '{your database name}'
        PORT = 5432
        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
        cleaned_df.to_sql(table_name, engine, if_exists='replace', index=False)


