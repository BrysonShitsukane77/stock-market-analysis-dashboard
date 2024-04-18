if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from os import path
import numpy as np
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account


@data_exporter
def export_data_to_big_query(data: pd.DataFrame, **kwargs):
    """
    Exports data to a BigQuery table.

    Args:
        data (pd.DataFrame): The DataFrame to export.
        **kwargs: Additional keyword arguments.
    """
    # Store the DataFrame to a CSV file
    csv_file_path = 'data.csv'
    data.to_csv(csv_file_path, index=False, encoding='utf-8')

    # Define the BigQuery table ID
    table_id = 'verdant-legacy-414217.stock_prices_dataset.stock_price_data2'

    # Load the CSV file into BigQuery
    credentials_path = '/home/src/my_creds.json'
    credentials = service_account.Credentials.from_service_account_file(credentials_path)
    client = bigquery.Client(credentials=credentials)
    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField('datetime', 'TIMESTAMP'),
            bigquery.SchemaField('open', 'FLOAT'),
            bigquery.SchemaField('high', 'FLOAT'),
            bigquery.SchemaField('low', 'FLOAT'),
            bigquery.SchemaField('close', 'FLOAT'),
            bigquery.SchemaField('volume', 'INTEGER'),
            bigquery.SchemaField('stock_symbol', 'STRING'),
            bigquery.SchemaField('stock_name', 'STRING'),
        ],
        skip_leading_rows=1,
        source_format=bigquery.SourceFormat.CSV,
    )

    with open(csv_file_path, 'rb') as source_file:
        try:
            job = client.load_table_from_file(source_file, table_id, job_config=job_config)
            job.result()  # Wait for the job to complete
            print("Data loaded successfully.")
        except Exception as e:
            print(f"Error loading data: {e}")

# Example usage:
# data = ...  # Your DataFrame
# export_data_to_big_query(data)
