-- Define a model for the stock symbols/names dimension (unique identifiers)
{{ config(
    materialized='table',
    unique_key='symbol_key'
) }}

SELECT
    SHA256(CONCAT(stock_symbol, stock_name)) AS symbol_key,
    stock_symbol,
    stock_name
FROM
    {{ ref('stg_stock_price_data') }}
GROUP BY
    stock_symbol,
    stock_name
