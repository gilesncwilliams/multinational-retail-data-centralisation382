/* Update dim_date_times table data types */

ALTER TABLE dim_date_times
    ALTER COLUMN month TYPE VARCHAR(2);

ALTER TABLE dim_date_times
    ALTER COLUMN year TYPE VARCHAR(4);

ALTER TABLE dim_date_times
    ALTER COLUMN day TYPE VARCHAR(2);

ALTER TABLE dim_date_times
    ALTER COLUMN time_period TYPE VARCHAR(20);

ALTER TABLE dim_date_times
   ALTER COLUMN date_uuid TYPE UUID USING date_uuid::UUID;