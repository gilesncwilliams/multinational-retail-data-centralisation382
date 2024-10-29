/* Milestone 4: Querying the database. 
   Task 1: How many stores does the business have and in which countires? */

SELECT country_code AS country,
       COUNT(country_code) AS total_no_stores
FROM 
    dim_store_details
GROUP BY
    country_code
ORDER BY 
    total_no_stores DESC;
 
/* Task 2: Which locations currently have the most stores? */ 

SELECT locality,
       COUNT(locality) AS total_no_stores
FROM 
    dim_store_details
GROUP BY
    locality
ORDER BY 
    total_no_stores DESC
LIMIT 
    7;

/* Task 3: Which months produced the largest amount of sales? */ 

SELECT SUM(product_quantity * product_price) AS total_sales,
       month
FROM 
    orders_table
JOIN 
    dim_date_times ON orders_table.date_uuid = dim_date_times.date_uuid
JOIN 
    dim_products ON orders_table.product_code = dim_products.product_code
GROUP BY
    month
ORDER BY 
    total_sales DESC
LIMIT 
    6;

/* Task 4: How many sales are coming from online? */ 

SELECT COUNT(date_uuid) AS numbers_of_sales,
       SUM(product_quantity) AS product_quantity_count,
CASE 
    WHEN store_type IN ('Local', 'Super Store', 'Outlet', 'Mall Kiosk') THEN 'Offline'
    ELSE 'Web'
END AS location
FROM 
    orders_table
JOIN dim_store_details ON orders_table.store_code = dim_store_details.store_code
GROUP BY
    location;


/* Task 5: What percentage of sales come through each type of store? 
   Note: % results slightly different to answer on AiCore portal */ 

SELECT store_type,
       SUM(product_quantity * product_price) AS total_sales,
       ROUND(SUM(product_quantity * product_price) * 100 / SUM(SUM(product_quantity * product_price)) OVER (), 2) AS "sales_made (%)"
FROM 
    orders_table
JOIN 
    dim_products ON orders_table.product_code = dim_products.product_code
JOIN
    dim_store_details ON orders_table.store_code = dim_store_details.store_code
GROUP BY
    store_type
ORDER BY 
    total_sales DESC;

/* Task 6: Which month in each year produced the highest cost of sales? */ 

SELECT SUM(product_quantity * product_price) AS total_sales,
       year,
       month
FROM 
    orders_table
JOIN 
    dim_date_times ON orders_table.date_uuid = dim_date_times.date_uuid
JOIN 
    dim_products ON orders_table.product_code = dim_products.product_code
GROUP BY
    year, 
    month
ORDER BY 
    total_sales DESC
LIMIT 
    10;

/* Task 7: What is our staff headcount? */ 

SELECT SUM(staff_numbers) AS total_staff_numbers,
       country_code
FROM 
    dim_store_details
GROUP BY
    country_code
ORDER BY 
    total_staff_numbers DESC;

/* Task 8: Which German store type is selling the most? */ 

SELECT SUM(product_quantity * product_price) AS total_sales,
       store_type,
       country_code
FROM
    orders_table
JOIN 
    dim_products ON orders_table.product_code = dim_products.product_code
JOIN
    dim_store_details ON orders_table.store_code = dim_store_details.store_code
WHERE   
    country_code = 'DE'
GROUP BY
    store_type,
    country_code
ORDER BY 
    total_sales;


/* Task 9: How quickly is the company making sales? */ 

WITH time_taken_cte AS (
    SELECT  year,
            LEAD(date_timestamp) OVER (ORDER BY date_timestamp) - date_timestamp AS actual_time_taken
    FROM
        dim_date_times
    GROUP BY
        year,
        date_timestamp
)
SELECT year,
       AVG(actual_time_taken) as actual_time_taken
FROM
    time_taken_cte
GROUP BY
    year
ORDER BY
    actual_time_taken DESC
LIMIT
    5;
