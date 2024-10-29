/* Tasks 4 and 5: make change to the dim_products table to assist 
   the delivery team, and update table with required data types.
   Firstly, remove '£' symbol from product_price column */

UPDATE dim_products
SET
    product_price = REPLACE(product_price, '£', '')
WHERE 
    product_price LIKE '£%';

/* Creating new weight_class column based on a range of product weights.
   The first query creates the new column, and the second uses a CASE aggregation 
   to categorise the weights into classes for the delivery team. */

ALTER TABLE dim_products
    ADD COLUMN weight_class VARCHAR(100);

UPDATE dim_products
SET weight_class = CASE 
            WHEN weight > 0 AND weight < 2 THEN 'Light'
            WHEN weight >= 2 AND weight < 40 THEN 'Mid_Sized'
            WHEN weight >= 40 AND weight < 140 THEN 'Heavy'
            ELSE 'Truck_Required'
            END;

/* Updates dim_products table data types */

ALTER TABLE dim_products
    ALTER COLUMN product_price TYPE NUMERIC USING product_price::NUMERIC(7,2);

ALTER TABLE dim_products
    ALTER COLUMN weight TYPE NUMERIC USING weight::NUMERIC(8,3);

ALTER TABLE dim_products
    ALTER COLUMN "EAN" TYPE VARCHAR(20);

ALTER TABLE dim_products
    ALTER COLUMN product_code TYPE VARCHAR(20);

ALTER TABLE dim_products
    ALTER COLUMN date_added TYPE DATE USING date_added::DATE;

ALTER TABLE dim_products
   ALTER COLUMN uuid TYPE UUID USING uuid::UUID;

/* These queries update the existing 'removed' column to a new Boolean
   column named 'still_available'.
   Note the mis-spelling of values 'Still_avaliable' in the original data
   set for this column */

ALTER TABLE dim_products
    RENAME removed TO still_available;

UPDATE dim_products
SET still_available = CASE still_available
            WHEN 'Still_avaliable' THEN 'YES'
            WHEN 'Removed' THEN 'NO'
            END;

ALTER TABLE dim_products
    ALTER COLUMN still_available TYPE BOOL USING still_available::BOOL;

/* Removes the Unnamed: 0 column from the table. */

ALTER TABLE dim_products
    DROP COLUMN "Unnamed: 0";