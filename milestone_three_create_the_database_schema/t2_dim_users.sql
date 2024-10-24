/* Task 2: Cast the columns of the dim_users to the correct data types. */

ALTER TABLE dim_users
    ALTER COLUMN first_name TYPE VARCHAR(255);

ALTER TABLE dim_users
    ALTER COLUMN last_name TYPE VARCHAR(255);

ALTER TABLE dim_users
    ALTER COLUMN date_of_birth TYPE DATE USING date_of_birth::DATE;

ALTER TABLE dim_users
    ALTER COLUMN country_code TYPE VARCHAR(5);

ALTER TABLE dim_users
    ALTER COLUMN user_uuid TYPE UUID USING user_uuid::UUID;

ALTER TABLE dim_users
    ALTER COLUMN join_date TYPE DATE USING join_date::DATE;