-- Define a model for the fact_stock_moving_avg table
{{ config(
    materialized='table',
    unique_key='id'
) }}

WITH stock_data AS (
  SELECT
    *,
    AVG(close) OVER (PARTITION BY stock_symbol ORDER BY datetime ROWS BETWEEN 29 PRECEDING AND CURRENT ROW) AS thirty_day_ma
  FROM
    {{ ref('stg_stock_price_data') }}
),
averages AS (
  SELECT
    stock_symbol,
    datetime,
    EXTRACT(YEAR FROM datetime) AS year,
    EXTRACT(MONTH FROM datetime) AS month,
    EXTRACT(DAY FROM datetime) AS day,
    AVG(open) AS avg_open,
    AVG(high) AS avg_high,
    AVG(low) AS avg_low,
    AVG(close) AS avg_close,
    AVG(volume) AS avg_volume,
    thirty_day_ma
  FROM
    stock_data
  GROUP BY
    stock_symbol,
    datetime,
    thirty_day_ma
)
SELECT
  ROW_NUMBER() OVER () as id,
  stock_symbol,
  datetime,
  year,
  month,
  day,
  avg_open,
  avg_high,
  avg_low,
  avg_close,
  avg_volume,
  thirty_day_ma
FROM
  averages
