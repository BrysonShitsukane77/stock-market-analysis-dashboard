-- Define a model for the fact_stock_rsi table (Relative Strength Index)
{{ config(
    materialized='table',
    unique_key='id'
) }}

WITH stock_data AS (
  SELECT
    *,
    LAG(close, 1) OVER (PARTITION BY stock_symbol ORDER BY datetime) AS prev_close,
    close - LAG(close, 1) OVER (PARTITION BY stock_symbol ORDER BY datetime) AS price_change,
    CASE
        WHEN close - LAG(close, 1) OVER (PARTITION BY stock_symbol ORDER BY datetime) > 0 THEN close - LAG(close, 1) OVER (PARTITION BY stock_symbol ORDER BY datetime)
        ELSE 0
    END AS gain,
    CASE
        WHEN close - LAG(close, 1) OVER (PARTITION BY stock_symbol ORDER BY datetime) < 0 THEN ABS(close - LAG(close, 1) OVER (PARTITION BY stock_symbol ORDER BY datetime))
        ELSE 0
    END AS loss
  FROM
    {{ ref('stg_stock_price_data') }}
),
averages AS (
  SELECT
    stock_symbol,
    datetime,
    AVG(gain) AS avg_gain,
    AVG(loss) AS avg_loss
  FROM
    stock_data
  GROUP BY
    stock_symbol,
    datetime
)
SELECT
  ROW_NUMBER() OVER () AS id,
  stock_symbol,
  datetime,
  100 - (100 / (1 + (AVG(avg_gain) OVER (PARTITION BY stock_symbol ORDER BY datetime ROWS BETWEEN 13 PRECEDING AND CURRENT ROW)) / (AVG(avg_loss) OVER (PARTITION BY stock_symbol ORDER BY datetime ROWS BETWEEN 13 PRECEDING AND CURRENT ROW)))) AS rsi
FROM
  averages
