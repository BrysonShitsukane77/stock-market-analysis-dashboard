if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path
import numpy as np

# # @data_exporter
# # def export_data_to_big_query(data: DataFrame, **kwargs) -> None:
#     """
#     Exports data to BigQuery after storing it in a CSV file.

#     Args:
#         data: The DataFrame to be exported
#         **kwargs: Additional keyword arguments
#     """
#     # Store the DataFrame to a CSV file
#     # csv_file_path = 'data.csv'
#     # data.to_csv(csv_file_path, index=False)

#     # Save DataFrame to a local Parquet file
#     # parquet_file_path = 'data.parquet'
#     # data.to_parquet(parquet_file_path)

#     # Specify BigQuery table configuration
#     # config_path = path.join(get_repo_path(), 'io_config.yaml')
#     # config_profile = 'default'
#     # table_id = 'verdant-legacy-414217.stock_prices_dataset.stock_price_data2'

#     # # Export the CSV file to BigQuery
#     # BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
#     #     parquet_file_path,
#     #     table_id,
#     #     if_exists='replace',  # Specify resolution policy if table name already exists
#     # )