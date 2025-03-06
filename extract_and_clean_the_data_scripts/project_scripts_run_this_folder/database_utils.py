"""
Facilitates connections to AWS RDS and PostgreSQL databases.

Classes:
    DatabaseConnector

"""

from sqlalchemy import create_engine, inspect
import yaml


class DatabaseConnector:
    """Class for utility functions to connect to PostgreSQL and AWS RDS databases.

    Functions:
    read_db_creds(yaml file) -> dictionary
    init_rds_engine() -> sqlalchemy database engine
    init_pg_engine() -> sqlalchemy database engine
    list_db_tables(sqlalchemy database engine) -> list
    upload_to_db(pandas.DataFrame) -> sql

    """
    
    def __init__(self, yaml_file, pg_database, pg_password):
        """
        Initializes the DatabaseConnector class with credentials.

        Args:
            yaml_file (str): Path to the YAML file containing AWS RDS credentials.
            pg_database (str): PostgreSQL database name.
            pg_password (str): PostgreSQL password.
        """
        self.credentials = self.read_db_creds(yaml_file)
        self.pg_database = pg_database
        self.pg_password = pg_password

    def read_db_creds(self, yaml_file):
        """
        Reads credentials for an AWS RDS database from a YAML file.

        Args:
            yaml_file (str): Path to the YAML file containing credentials.

        Returns:
            dict: A dictionary of the database credentials.
        """
        with open(yaml_file, 'r') as f:
            credentials = yaml.safe_load(f)
        return credentials

    def init_rds_engine(self):
        """
        Initializes an SQLAlchemy engine for AWS RDS.

        Returns:
            engine: An SQLAlchemy engine for AWS RDS.
        """
        engine = create_engine(
            f"postgresql+psycopg2://{self.credentials['RDS_USER']}:"
            f"{self.credentials['RDS_PASSWORD']}@{self.credentials['RDS_HOST']}:"
            f"{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}"
        )
        return engine

    def init_pg_engine(self, pg_user="postgres", pg_host="localhost", pg_port=5432):
        """
        Initializes an SQLAlchemy engine for a local PostgreSQL database.

        Args:
            pg_user (str): PostgreSQL username. Defaults to 'postgres'.
            pg_host (str): PostgreSQL host. Defaults to 'localhost'.
            pg_port (int): PostgreSQL port. Defaults to 5432.

        Returns:
            engine: An SQLAlchemy engine for the local PostgreSQL database.
        """
        DATABASE_TYPE = "postgresql"
        DBAPI = "psycopg2"
        HOST = pg_host
        USER = pg_user
        PASSWORD = self.pg_password
        DATABASE = self.pg_database
        PORT = pg_port

        engine = create_engine(
            f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
        )
        return engine

    def list_db_tables(self, engine):
        """
        Creates a list of database tables from the database connection.

        Args:
            engine: SQLAlchemy engine instance.

        Returns:
            list: A list of table names in the database.
        """
        inspector = inspect(engine)
        return list(inspector.get_table_names())

    def upload_to_db(self, df, table_name):
        """
        Uploads a Pandas dataframe to a PostgreSQL database.

        Args:
            df (pd.DataFrame): A Pandas dataframe.
            table_name (str): The name of the new table in the PostgreSQL database.
        """
        engine = self.init_pg_engine()
        df.to_sql(table_name, engine, if_exists="replace", index=False)
