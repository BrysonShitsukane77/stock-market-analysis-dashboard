if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd


@transformer
def transform(data, *args, **kwargs):
    """
    Perform quality checks on the loaded data.

    Args:
        data: The output from the upstream parent block

    Returns:
        DataFrame: The transformed data
    """
    # Check for null values
    null_counts = data.isnull().sum()

    # Check for duplicates
    duplicate_counts = data.duplicated().sum()

    # Check data types
    data_types = data.dtypes

    # Log the results of the quality checks
    print("Null Value Counts:")
    print(null_counts)
    print("\nDuplicate Counts:")
    print(duplicate_counts)
    print("\nData Types:")
    print(data_types)

    # Change 'datetime' column to pandas datetime
    data['datetime'] = pd.to_datetime(data['datetime'])

    # Drop duplicates
    data.drop_duplicates(inplace=True)

    # Log the results of the transformations
    print("After Transformation - Null Value Counts:")
    print(data.isnull().sum())
    print("\nAfter Transformation - Duplicate Counts:")
    print(data.duplicated().sum())
    print("\nAfter Transformation - Data Types:")
    print(data.dtypes)

    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
