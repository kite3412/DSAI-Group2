{{ config(materialized='view') }}

SELECT
    ROW_NUMBER() OVER (ORDER BY product_id) AS product_key,
    product_id,
    product_category_name AS product_category,
    product_weight_g AS weight,
    product_length_cm AS length,
    product_height_cm AS height,
    product_width_cm AS width
FROM {{ ref('stg_products') }}

