/* Task 3: Update the dim_store_details table. 
   Merge two lattitude columns */

UPDATE dim_store_details
SET 
    latitude = COALESCE(latitude, lat);

/* Remove redundant lat column */

ALTER TABLE dim_store_details
    DROP COLUMN lat;

/* Change website location N/A values to NULL. */

UPDATE dim_store_details
SET 
    longitude = NULL,
    latitude = NULL,
    locality = NULL,
    address = NULL
WHERE 
    longitude = 'N/A'
    OR latitude = 'N/A'
    OR locality = 'N/A'
    OR address = 'N/A';

/* Set data types for each column */

ALTER TABLE dim_store_details
    ALTER COLUMN longitude TYPE NUMERIC USING longitude::NUMERIC(7,5);

ALTER TABLE dim_store_details
    ALTER COLUMN locality TYPE VARCHAR(255);

ALTER TABLE dim_store_details
    ALTER COLUMN store_code TYPE VARCHAR(20);

ALTER TABLE dim_store_details
    ALTER COLUMN staff_numbers TYPE SMALLINT;

ALTER TABLE dim_store_details
    ALTER COLUMN opening_date TYPE DATE USING opening_date::DATE;

ALTER TABLE dim_store_details
    ALTER COLUMN store_type TYPE VARCHAR(255);

ALTER TABLE dim_store_details
    ALTER COLUMN latitude TYPE NUMERIC USING latitude::NUMERIC(8,5);

ALTER TABLE dim_store_details
    ALTER COLUMN country_code TYPE VARCHAR(5);

ALTER TABLE dim_store_details
    ALTER COLUMN continent TYPE VARCHAR(255); 
