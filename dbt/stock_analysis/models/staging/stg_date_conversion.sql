-- Create a staging table for date conversion
SELECT
  DATE(datetime) AS date,
  EXTRACT(YEAR FROM datetime) AS year,
  EXTRACT(MONTH FROM datetime) AS month,
  EXTRACT(DAY FROM datetime) AS day
FROM
  {{ source('staging', 'stock_price_data') }}
GROUP BY 1, 2, 3, 4
