# Multinational Retail Data Centralisation Project

![Static Badge](https://img.shields.io/badge/Welcome%20To-blue)

![Static Badge](https://img.shields.io/badge/The%20Multinational%20Retail%20Data%20Centralisation%20Project-blue)

![Static Badge](https://img.shields.io/badge/A%20Data%20Training%20Project%20By-blue)

![Static Badge](https://img.shields.io/badge/Giles%20Williams-blue)


## Table of Contents

- Introduction
- Installation Instructions
- Usage Instructions
- Task's Data Cleaning Considerations
- Resulting ERD and Answers to SQL Queries
- Project File Structure
- Licensing Information



## Introduction 


![Static Badge](https://img.shields.io/badge/Project%20Summary%3A-blue)

The project goal is to produce a system for a fictional multinational retail business to store its historical sales data into a database, which will act as the single source of truth for the business and can be accessed from one centralised location.  


![Static Badge](https://img.shields.io/badge/Project%20Scope%3A-blue)

A multinational retail business, selling a range of, nearly, 2,000 products across multiple vertical markets (including home goods and applicances; health and beauty; food and beverages; and sport and leisure), is looking to update how they manage and use their data.

Currently, their sales data is spread across many different data sources meaning it is not easily accessible or analysable by current members of the team. In an effort to become more data-driven, the organisation would like to make its sales data accessible from one centralised location, allowing senior management to view up-to-date metrics and help inform business decisions.

My task was to extract the data from the multitude of data sources (e.g. sales orders, product details, customers details) and formats (including CSV, PDF, AWS S3 and RDS), clean it, and then store it in a new relational database. Finally, answer some business related questions to query the data using SQL. 

The project was designed to test my knowlege of Git and GitHub, Python (including and Object Orientated Programming and data cleaning package Pandas), SQL language and PostgresQL database.

The project is divided into 4 milestones:

![Static Badge](https://img.shields.io/badge/Milestone%201%3A%20set%20up%20the%20dev%20environment-blue)

Setting a GitHub repo, local conda environment and database in pgAdmin4.

![Static Badge](https://img.shields.io/badge/Milestone%202%3A%20extract%20and%20clean%20the%20data-blue)

Extract the data from multiple sources and clean it with Pandas before uploading to a PostgreSQL database.

![Static Badge](https://img.shields.io/badge/Milestone%203%3A%20create%20the%20database%20schema-blue)

Using SQL, cast the columns in each table in the database to the correct datatype, and assign primary and foreigh keys to create the star-based scheme of the database. 

![Static Badge](https://img.shields.io/badge/Milestone%204%3A%20analyse%20the%20data-blue)

Write SQL queries to answer questions asked by the business about the sales data.



## Installation Instructions

1. The first step to begin the installation process is to clone this repository to your local machine

Follow [these](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository) instructions on how to clone a repository.


2. Environment setup using a package manager e.g Conda.

Ensure you are using a new environment before starting the set up process. Follow the instructions [here](https://github.com/conda/conda/blob/main/docs/source/user-guide/tasks/manage-environments.rst) on how to create a new environment.

Next, using your package manager, install Python3.

To peform the data extraction and cleaning tasks by running the code contained within the project, you will require these 3rd party packages installed into your Python environmnet. Using pip to install them:

- boto3
- numpy
- pandas
- psycopg2 (install as pip psycopg2-binary)
- requests
- sqlalchemcy
- tabula
- yaml

3. Setting up the PostgreSQL database

Firstly, install PostgreSQL and pgAmin4 to your local machine to manage the database.

For Mac and Window users, follow this [link](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) and select the version according to your OS. Then select the latest version and follow instructions to install. You will be asked to create a password for your new user during the installation. You will need the password to connect to the database later to please keep a record of it.

To create a database, open pgAdmin and right click on Databases and select 'Create' then 'Database'.

![alt text](<README images and gifs/image.png>)

Name your database, e.g. 'sales_data' and copy the details below from your database as you will need them for the upload to database function later.

- DATABASE_TYPE = 'postgresql'
- DBAPI = 'psycopg2'
- HOST = 'localhost'
- USER = 'postgres'
- PASSWORD = '{your password}'
- DATABASE = '{your database name}'
- PORT = 5432


## Usage Instructions

![Static Badge](https://img.shields.io/badge/How%20to%20run%20the%20data%20cleaning%20pipeline-blue)


1. Firstly, update your PostgreSQL database details created above in the upload_to_db function in the database_utils.py script, and save it without changing the files name. For example:

![alt text](<README images and gifs/Screenshot 2024-10-28 at 11.39.56.png>)


2. To run the pipeline to extract and clean the data from the multiple data sources, navigate to the 'milestone_two_extract_and_clean_the_data' folder in your terminal.
   
   Then type 'python3 project_scripts_run_this_folder' in your terminal to run the full data cleaning pipeline, extracting each data source in turn and uploading it to your PostgreSQL database in pgDAmin.

   ![alt text](<README images and gifs/Run project gif.gif>)
   
   I have included .info() and .head() print statements on each Pandas dataframe so you can see the data as it is cleaned in the terminal and review the results.

   Once the pipeline has been run, refresh your PostgreSQL database in pgAdmin to see the newly imported tables (right click on the database name and select 'refresh')



3. To create the database schema, switch to pgAdmin and open each of the sql files in turn (see gif below). They are ordered based on each task (t1, t2, etc) and each file relates to the data cleaning and setting up requried for each of the tables in ther database, plus the creation of the primary and foreign keys. 

![alt text](<README images and gifs/import sql file in pgadmin.gif>)

Run each sql script in turn by importing and clicking the play button in the query window (or highlight each query and use shortcut F5)

![alt text](<README images and gifs/run sql file in pg admin.gif>)


4. To view the queries run on the business's sales data, import the m4_query_the_data_all_tasks.sql into pgAmin and run each query by highlighting a query one at a time to view the results.


## Task's Data Cleaning Considerations


During the data cleaning tasks of the project (Milestone 2), there were several issues with the data that I identified and cleaned.

These issue are listed below, along with solutions I employed using Pandas data cleaning package to resolve them. Each task contains references to the specific Python functions that I created to clean each dataframe stored within in the data_cleaning.py file.

As a general starting point, any values that had a generic 'N/A' or 'NULL' text value were replaced with null values, and any rows that contained only null values across all columns were dropped. Both these actions were wrapped in a user-created function called 'remove_null_values' and were applied to all tables.

Following this, any columns with obvious date/time values were converted into a datetime data type, and other obvious data type conversions were carried out within each task's function.

In addition, for each Pandas dataframe, some specific data cleaning was required:

Task 3: clean_user_data function.
- A small number of values had mis-spelt 'GB' country codes and were corrected with the str.replace() function in Pandas.

Task 4: clean_card_data function.
- Some rows contained incorrect values, formatting the date_payment_confirmed column turned those values to NULL, which meant those rows could be easily identified and dropped.
- Some credit cards had typing errors with a '?' at the front of the card numbers. I used the str.replace() function to remove these, after converting to a string data type.
- Any duplicate card numbers were also dropped.

Task 5: clean_store_data function
- Corrected errors in the 'continent' column. Replacing 'eeAmerica' and 'eeEurope' with the correct continents using the str.repalce() function.
- Removed any symbols, letters, or non-digit characters from the 'store_numbers' columne with the str.replace() function.

Task 6: convert_product_weights and clean_products_data functions
- As the weight data had been recorded in multiple measurements (g, kgs, oz, ml), each one of these needed to be converted to KGs. I created a 'weight_conversion' function containing an if statement to apply a different conversion method to each measurement type within the data set; as well removing some small errors with additional characters (e.g. '.').

Task 7: clean_order_data function
- Drop unwanted columns 'first_name', 'last_name', '1' using Pandas .drop() function.

Task 6: clean_data_events_ data function
- Created a new data_timestamp column for each sale using the existing 'year', 'month' and 'day' columns using the pd.to.datetime(function) for later use in the project. 


## Resulting ERD and Answers to SQL Queries

![Static Badge](https://img.shields.io/badge/Database%20ERD-blue)


After cleaning and upload the data to PostgreSQL, and assiging primary and foreign keys with SQL, the resulting star-based schema for the database in pgAdmin looks like this:

![alt text](<README images and gifs/multinational_retail_data_centralisation_project.png>)



![Static Badge](https://img.shields.io/badge/Querying%20the%20Data-blue)


Below are the results of SQL queries in Milestone 4 run on the database to answer business related questions, and the details behind the relevant SQL functions applied.
(See m4_query_the_data_all_tasks.sql file to view each of the SQL queries.)

1. How many stores does the business have and in which countires?

![alt text](<README images and gifs/Screenshot 2024-10-28 at 10.39.12.png>)

Using the COUNT aggregate function, grouped by country_code to identify the total number of stores in each country, and then displayed in descending order.


2. Which locations currently have the most stores?

![alt text](<README images and gifs/Screenshot 2024-10-28 at 10.39.29.png>)

Using the COUNT aggregate function, grouped by locality to identify the locations with the most stores, and then displayed in descending order.

3. Which months produced the largest amount of sales?

![alt text](<README images and gifs/Screenshot 2024-10-28 at 10.39.55.png>)

Joining the dim_date_times and dim_products tables to the orders_table to collate the required information for sales and product details, then using the SUM aggregate function, grouped by month, to calculate the total sales for each month and displayed in descending order.

4. How many sales are coming from online?

![alt text](<README images and gifs/Screenshot 2024-10-28 at 10.40.13.png>)

Starting by joining the dim_store_details table to the order_table on their keys, then using a CASE statement to evaluate the 'store_type' column to categorise each store type into either 'Web' or 'Offline' for the bricks and mortar stores.  Finally, using the COUNT and SUM aggreate functions to calculate the number of sales and product quantities sold for each store category.

5. What percentage of sales come through each type of store?

![alt text](<README images and gifs/Screenshot 2024-10-28 at 10.40.30.png>)

Creating a joined table from the orders_table, dim_products and dim_store_details tables, then using a window function to calculate the percentage of total sales for each type of store (we want the function to be applied to the full result so no partioning or ordering is required). The result is displayed in descending order.

6. Which month in each year produced the highest cost of sales?

![alt text](<README images and gifs/Screenshot 2024-10-28 at 10.41.04.png>)

Again, from the orders_table, dim_date_times and products_table creating a joined table containing all the orders and sales data, and then using the SUM aggregate function to find the total sales, grouped by year and month to identify the best monthly performance, before being displayed in descending order.

7. What is our staff headcount?

![alt text](<README images and gifs/Screenshot 2024-10-28 at 10.41.20.png>)

A simple SUM aggregate function to calculate the staff numbers grouped by each country, displayed in descending order.

8. Which German store type is selling the most?

![alt text](<README images and gifs/Screenshot 2024-10-28 at 10.41.38.png>)

Using the same joined table from Q5 to collate the sales data for each store, then, with a WHERE statement to identify the German stores, group by store type.

9. How quickly is the company making sales?

![alt text](<README images and gifs/Screenshot 2024-10-28 at 10.41.58.png>)

Here we have employed a common table expression containing a LEAD() window function to calculate the time taken between each sale for all the orders in the dim_date_times table. 

We then perform an average calculation on the CTE to find the resulting average time taken for each year, before ordering them in ascending order by year so the year with lowest average time difference between orders is shown at the top.


## Project File Structure


 * multinational-retail-data-centralisation382
   * milestone_two_extract_and_clean_the_data
     * project_files
       * db_creds.yaml
     * project_scripts_run_this_folder
       * __main__.py
       * data_cleaning.py
       * data_extraction.py
       * database_utils.py
   * milestone_three_create_the_database_schema
     * t1_orders_table.sql
     * t2_dim_users.sql
     * t3_dim_store_details.sql
     * t4_t5_dim_products.sql
     * t6_dim_date_times.sql
     * t7_dim_card_details.sql
     * t8_create_primary_keys.sql
     * t9_add_foreign_keys.sql
   * milestone_four_query_the_data
     * m4_query_the_data_all_tasks.sql
   * README.md
   * .gitignore                           



## License Information
This repo is unlicensed as it was intended only for training purposes.


