-- Define a model for the fact_stock_volatility table
{{ config(
    materialized='table',
    unique_key='id'
) }}

WITH stock_data AS (
  SELECT
    *,
    STDDEV(close) OVER (PARTITION BY stock_symbol ORDER BY datetime ROWS BETWEEN 29 PRECEDING AND CURRENT ROW) AS thirty_day_volatility
  FROM
    {{ ref('stg_stock_price_data') }}
),
volatility AS (
  SELECT
    stock_symbol,
    datetime,
    EXTRACT(YEAR FROM datetime) AS year,
    EXTRACT(MONTH FROM datetime) AS month,
    EXTRACT(DAY FROM datetime) AS day,
    thirty_day_volatility
  FROM
    stock_data
)
SELECT
  ROW_NUMBER() OVER () as id,
  stock_symbol,
  datetime,
  year,
  month,
  day,
  thirty_day_volatility
FROM
  volatility
