if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
from pandas import DataFrame
from typing import Dict, List



@transformer
def transform(stock_data: List[Dict], symbol_mapping: Dict[str, str] = None) -> List[Dict]:
    """
    Transforms a list of dictionaries containing stock symbols by replacing them with representative symbols.

    Args:
        stock_data (List[Dict]): A list of dictionaries where each dictionary represents a row in the DataFrame.
            Each dictionary should have a key named 'stock_symbol'.
        symbol_mapping (Dict[str, str], optional): A dictionary mapping original stock symbols to representative symbols.
            Defaults to None, in which case all unique stock symbols are used as their own representatives.

    Returns:
        List[Dict]: The transformed list of dictionaries with an additional key 'representative_symbol' for each entry.
    """
    if symbol_mapping is None:
        symbol_mapping = {d['stock_symbol']: d['stock_symbol'] for d in stock_data}

    for row in stock_data:
        row['representative_symbol'] = symbol_mapping.get(row['stock_symbol'], row['stock_symbol'])

    return stock_data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
