from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_google_cloud_storage(stock_data: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    bucket_name = 'verdant-legacy-414217-stock-prices-bucket'
    object_key = 'stock_prices.parquet'

    # Save DataFrame to a local Parquet file
    local_file_path = 'stock_data.parquet'
    stock_data.to_parquet(local_file_path)

    GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).export(
        local_file_path,
        bucket_name,
        object_key,
    )

# Export your stock_data DataFrame to Google Cloud Storage
#export_data_to_google_cloud_storage(stock_data)
