/* Task 1: Cast the columns of the orders_table to the correct data types. */

ALTER TABLE orders_table
    ALTER COLUMN date_uuid TYPE UUID USING date_uuid::UUID;

ALTER TABLE orders_table
    ALTER COLUMN user_uuid TYPE UUID USING user_uuid::UUID;

ALTER TABLE orders_table
    ALTER COLUMN card_number TYPE VARCHAR(20);

ALTER TABLE orders_table
    ALTER COLUMN store_code TYPE VARCHAR(20);

ALTER TABLE orders_table
    ALTER COLUMN product_code TYPE VARCHAR(20);

ALTER TABLE orders_table
    ALTER COLUMN product_quantity TYPE SMALLINT;





