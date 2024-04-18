-- Define a model for the fact_stock_bollinger_bands table
{{ config(
    materialized='table',
    unique_key='id'
) }}

WITH stock_data AS (
  SELECT
    *,
    AVG(close) OVER (PARTITION BY stock_symbol ORDER BY datetime ROWS BETWEEN 19 PRECEDING AND CURRENT ROW) AS ma_20,
    STDDEV(close) OVER (PARTITION BY stock_symbol ORDER BY datetime ROWS BETWEEN 19 PRECEDING AND CURRENT ROW) AS sd_20
  FROM
    {{ ref('stg_stock_price_data') }}
)
SELECT
  ROW_NUMBER() OVER () AS id,
  stock_symbol,
  datetime,
  ma_20 + (2 * sd_20) AS upper_band,
  ma_20 - (2 * sd_20) AS lower_band
FROM
  stock_data
