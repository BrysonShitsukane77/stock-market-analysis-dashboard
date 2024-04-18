if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(stock_data, *args, **kwargs):
    """
    Rounds the values in the DataFrame to 2 decimal places.

    Args:
        stock_data: DataFrame containing stock data.

    Returns:
        DataFrame with values rounded to 2 decimal places.
    """
    # Round the values to 2 decimal places
    stock_data = stock_data.round(2)

    # Return dates in ascending order
    stock_data.sort_values(by=[ 'datetime'], ascending=[False], inplace=True)
    
    stock_data.reset_index(drop=True, inplace=True)

    return stock_data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
