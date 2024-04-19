if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd

@transformer
def transform(stock_data, *args, **kwargs):
    """
    Rounds the values in the DataFrame to 2 decimal places and saves the DataFrame to a CSV file.

    Args:
        stock_data: DataFrame containing stock data.

    Returns:
        DataFrame with values rounded to 2 decimal places.
    """
    # Round the values to 2 decimal places
    stock_data = stock_data.round(2)

    # Change 'datetime' column to pandas datetime
    stock_data['datetime'] = pd.to_datetime(stock_data['datetime'])

    # Drop duplicates
    stock_data.drop_duplicates(inplace=True)

    # Drop null values
    stock_data.dropna(subset=['stock_name'], inplace=True)

    # Return dates in ascending order
    stock_data.sort_values(by=['datetime'], ascending=[False], inplace=True)

    stock_data.reset_index(drop=True, inplace=True)

    # Save the DataFrame to a CSV file
    stock_data.to_csv('stock_prices.csv', index=False)

    return stock_data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'