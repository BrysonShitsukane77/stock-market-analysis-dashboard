# Stock Market Analysis

## Introduction

This data engineering project focuses on analyzing historical stock price data to provide insights for potential stock investments. The project aims to help stakeholders, such as individual investors, financial advisors, or investment firms, make informed decisions regarding stock investments by identifying trends and patterns in stock prices.

## Problem Statement

The primary objective of this project is to analyze historical stock price data to:

1. Identify trends and patterns in stock prices.
2. Identify potential investment opportunities based on historical stock performance.
3. Provide insights to stakeholders to make informed decisions regarding stock investments.

## Data Source

The project will utilize historical stock price data obtained from Twelve Data using their API. This data will be processed and analyzed to extract meaningful insights for stock market analysis. This is the [api_url](https://api.twelvedata.com/time_series?symbol={stock}&interval={interval}&apikey={api_key}&format=CSV&outputsize=5000&delimiter=,)

## Tools
- GCP (GCS & BigQuery)
- Terraform
- Docker
- Python
- Mage
- dbt
- Looker Studio

## Methodology

The project will follow these steps:

1. **Data Extraction:** Historical stock price data will be obtained from Twelve Data API.
2. **Data Transformation:** The data will be transformed into a format suitable for analysis, including cleaning and formatting.
3. **Export to Google Cloud Storage (GCS):** The transformed data is exported to GCS.
4. **Data Loading:** Data is loaded from GCS.
5. **Further Minor Transformation:** Another round of minor transformation is applied.
6. **Export to BigQuery (BQ):** The data is exported to BigQuery.
7. **Orchestration with Mage:** Mage is used as an orchestrator throughout the process.
8. **Data Modeling and Complex Transformation with dbt:** dbt is used for data modeling and complex transformations to generate final aggregated tables.
9. **Data Analysis:** Various analysis techniques will be applied to identify trends and patterns in stock prices.
10. **Data Visualization with Google Data Studio:** The final aggregated tables are visualized using Google Data Studio; and iInsights will be generated based on the analysis to help stakeholders make informed decisions.

## Solution



## Conclusion

By analyzing historical stock price data, this project aims to provide valuable insights for potential stock investments. The project's outcome will assist stakeholders in making informed decisions regarding stock investments, ultimately enhancing their investment strategies.

## Dashboard

![image](https://github.com/BrysonShitsukane77/stock-market-analysis-dashboard/assets/124519816/30485990-01ea-48f9-b19b-536ef96ba84f)

## Reproducibility

To reproduce the whole project, go to this [link](https://github.com/BrysonShitsukane77/stock-market-analysis-dashboard/blob/main/reproducibility/README.md)

## Repository Structure

<pre>
stock-market-analysis-dashboard/
├── dbt/
│   ├── stock_analysis/
│   │   ├── models
│   │   │   └── marts
│   │   │       └── dim_date.sql
│   │   │       └── fact_stock_moving_avg.sql
│   │   │   └── staging
│   │   │       └── sources.yml
│   │   │       └── stg_date_conversion.sql
│   │   │       └── stg_stock_price_data.sql
│   │   └── dbt_project.yml
│   │   └── packages.yml
├── mage/
│   ├── stock_analysis/
│   │   └── data_exporters
│   │   │   └── export_to_bigquery.py
│   │   │   └── export_to_gcs
│   │   └── data_loaders
│   │   │   └── load_api_data.py
│   │   │   └── load_gcs_stock_data.py
│   │   └── pipelines
│   │   │   └── api_to_gcs  
│   │   │   └── gcs_to_bigquery
│   │   └── transformers
│   │   │   └── data_mapping.py
│   │   │   └── fix_values.py
│   │   │   └── transform_staged_data.py
│   │   └── io_config.yaml
│   │   └── metadata.yaml
│   │   └── requirements.txt
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── requirements.txt
├── reproducibility/
│   └── README.md
├── terraform/
│   └── main.tf
│   └── variables.tf
├── .gitignore
└── README.md
</pre>
