-- Define an incremental model for fact_stock_volatility
{{ config(
    materialized='incremental',
    unique_key='id',
    target_schema='stock_prices_dataset',
    target_table='fact_stock_volatility_incremental'
) }}

WITH latest_data AS (
    SELECT *
    FROM {{ ref('fact_stock_volatility') }}
),
new_data AS (
    SELECT
        ROW_NUMBER() OVER () AS id,
        stock_symbol,
        datetime,
        thirty_day_volatility
    FROM
        {{ ref('fact_stock_volatility') }}
)
SELECT
    new_data.*
FROM
    new_data
LEFT JOIN
    latest_data USING (id)
WHERE
    latest_data.id IS NULL
