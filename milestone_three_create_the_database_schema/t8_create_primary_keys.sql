/* Add Primary Keys to dim tables */

ALTER TABLE dim_users 
    ADD CONSTRAINT dim_users_primary_key PRIMARY KEY (user_uuid);

ALTER TABLE dim_store_details
    ADD CONSTRAINT dim_store_details_primary_key PRIMARY KEY (store_code);

ALTER TABLE dim_products
    ADD CONSTRAINT dim_products_primary_key PRIMARY KEY (product_code);

ALTER TABLE dim_date_times
    ADD CONSTRAINT dim_date_times_primary_key PRIMARY KEY (date_uuid);

ALTER TABLE dim_card_details
    ADD CONSTRAINT dim_card_details_primary_key PRIMARY KEY (card_number);