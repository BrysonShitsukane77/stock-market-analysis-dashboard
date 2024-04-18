-- Define a model for the date dimension
{{ config(
    materialized='table',
    unique_key='date_key'
) }}

SELECT
    ROW_NUMBER() OVER () AS date_key,
    date,
    EXTRACT(DAYOFWEEK FROM date) AS day_of_week,
    EXTRACT(MONTH FROM date) AS month,
    EXTRACT(QUARTER FROM date) AS quarter,
    EXTRACT(YEAR FROM date) AS year,
    CASE
        WHEN date IN ('2024-01-01', '2024-07-04', '2024-12-25') THEN TRUE
        ELSE FALSE
    END AS is_holiday
FROM
    {{ ref('stg_date_conversion') }}
