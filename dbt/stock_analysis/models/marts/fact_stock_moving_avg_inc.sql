-- Define an incremental model for fact_stock_moving_avg
{{ config(
    materialized='incremental',
    unique_key='id',
    target_schema='stock_prices_dataset',
    target_table='fact_stock_moving_avg_incremental'
) }}

WITH latest_data AS (
    SELECT *
    FROM {{ ref('fact_stock_moving_avg') }}
),
new_data AS (
    SELECT
        ROW_NUMBER() OVER () AS id,
        stock_symbol,
        datetime,
        avg_open,
        avg_high,
        avg_low,
        avg_close,
        avg_volume,
        thirty_day_ma
    FROM
        {{ ref('fact_stock_moving_avg') }}
)
SELECT
    new_data.*
FROM
    new_data
LEFT JOIN
    latest_data USING (id)
WHERE
    latest_data.id IS NULL
