/* Task 9: add foreign keys to the orders table connecting it to the 
   five 'dim' tables and creating the star-based schema of the database. */

ALTER TABLE orders_table
    ADD CONSTRAINT dim_users_foreign_key 
    FOREIGN KEY (user_uuid) REFERENCES dim_users(user_uuid);

ALTER TABLE orders_table
    ADD CONSTRAINT dim_card_details_foreign_key 
    FOREIGN KEY (card_number) REFERENCES dim_card_details(card_number);

ALTER TABLE orders_table
    ADD CONSTRAINT dim_date_times_foreign_key 
    FOREIGN KEY (date_uuid) REFERENCES dim_date_times(date_uuid);

ALTER TABLE orders_table
    ADD CONSTRAINT dim_products_foreign_key 
    FOREIGN KEY (product_code) REFERENCES dim_products(product_code);

ALTER TABLE orders_table
    ADD CONSTRAINT dim_store_details_foreign_key 
    FOREIGN KEY (store_code) REFERENCES dim_store_details(store_code);