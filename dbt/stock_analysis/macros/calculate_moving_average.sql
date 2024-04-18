-- Create a macro to calculate moving average
{% macro calculate_moving_average(stock_data, window_size, value_column) %}
WITH ranked_data AS (
  SELECT
    *,
    ROW_NUMBER() OVER (ORDER BY datetime) AS row_num
  FROM {{ stock_data }}
),
averages AS (
  SELECT
    *,
    AVG({{ value_column }}) OVER (
      ORDER BY row_num
      ROWS BETWEEN {{ window_size }} PRECEDING AND CURRENT ROW
    ) AS moving_avg
  FROM ranked_data
)
SELECT
  *,
  DATE(datetime) AS date,
  moving_avg
FROM averages
{% endmacro %}
