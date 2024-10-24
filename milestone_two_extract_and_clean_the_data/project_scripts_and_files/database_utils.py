from sqlalchemy import create_engine, inspect
import yaml


class DatabaseConnector:

    def read_db_creds():
        with open('db_creds.yaml', 'r') as f:
            credentials = yaml.safe_load(f)
        return credentials

    def init_db_engine(credentials):
        engine = create_engine(f"postgresql+psycopg2://{credentials['RDS_USER']}:{credentials['RDS_PASSWORD']}@{credentials['RDS_HOST']}:{credentials['RDS_PORT']}/{credentials['RDS_DATABASE']}")
        return engine
    
    def list_db_tables(engine):
        inspector = inspect(engine)
        return list(inspector.get_table_names())      
       
    def upload_to_db(cleaned_df, table_name):
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        HOST = 'localhost'
        USER = 'postgres'
        PASSWORD = 'CSN&YpWi!969'
        DATABASE = 'sales_data'
        PORT = 5432
        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
        cleaned_df.to_sql(table_name, engine, if_exists='replace', index=False)


# if __name__ == '__main__':
#     connection = DatabaseConnector()
#     credentials = connection.read_db_creds()
#     engine = connection.init_db_engine(credentials)
#     list_of_tables = connection.list_db_tables(engine)
#     print(list_of_tables)