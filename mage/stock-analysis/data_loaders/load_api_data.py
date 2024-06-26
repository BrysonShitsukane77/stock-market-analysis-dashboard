import io
import pandas as pd
import requests
import time
import os
import logging
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
from mage_ai.data_preparation.shared.secrets import get_secret_value

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@data_loader
def load_data_from_api(*args, **kwargs):
    # Define the list of stocks to load data for
    stocks = [
     "AAPL", "MSFT", "AMZN", "GOOGL", "TSLA", "NVDA", "JPM", "JNJ", "V", "PYPL", "DIS", "PG", "MA", "NFLX", "HD", "UNH", "VZ", "CRM",
    "BAC", "ADBE", "INTC", "CSCO", "XOM", "KO", "PFE", "ABT", "MRK", "NKE", "ACN", "MCD", "WMT", "T", "ORCL", "IBM", "C", "AVGO", "QCOM",
    "CVX", "COST", "GILD", "TXN", "ABBV", "BMY", "DHR", "LLY", "UPS", "SBUX", "CAT", "MDLZ", "MMM", "HON", "LIN", "LOW", "AMGN", "MO",
    "BKNG", "TMO", "CHTR", "WFC", "NEE", "AAP", "LMT", "ZTS", "ADP", "MET", "UNP", "NOW", "CME", "GE", "AMD", "INTU", "MU", "ISRG", "ABNB",
    "FIS", "FDX", "GM", "CI", "MMC", "RMD", "SPGI", "ADSK", "REGN", "EXC", "AON", "WM", "COO", "APD", "SYK", "BK", "DXCM", "EA",
    "DE", "HUM", "SYY", "KLAC", "ECL", "ED", "ITW", "DUK", "NSC", "ICE", "DD", "NEM", "CTAS", "VRSK", "CDNS", "ZBRA", "IDXX", "CPRT",
    "SNPS", "ALGN", "ANSS", "MKTX", "TGT", "FTNT", "EFX", "PAYX", "MSCI", "ORLY", "SPG", "CHD", "MCO", "RSG", "AXP", "VRTX",
    "ADS", "DLTR", "BIIB", "EW", "RMD", "ESS", "ROP", "CTSH", "PGR", "HCA", "IPGP", "SRE", "CARR", "LHX", "WST", "KEYS",
    "TRV", "PSA", "NTAP", "NVR", "A", "HLT", "WDC", "PHM", "ALB", "BR", "EXPE", "AMAT", "WY", "O", "CCL", "NDAQ", "VLO", "REG",
    "NCLH"
]

    # Define the API key
    api_key = get_secret_value('TWELVEDATA_API_KEY')

    # Define the interval
    interval = "1day"

    # Create a list to store the dataframes for each stock
    stock_dfs = []

    # Create a cached session
    #cache_session = CachedSession('.cache', expire_after=3600)

    # Loop over the stocks
    for stock in stocks:
        api_url = f"https://api.twelvedata.com/time_series?symbol={stock}&interval={interval}&apikey={api_key}&format=CSV&outputsize=5000&delimiter=,"
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            stock_data = pd.read_csv(io.StringIO(response.text))
            stock_data['stock_symbol'] = stock
            stock_dfs.append(stock_data)
        except Exception as e:
            logger.error(f"Failed to fetch data for {stock}: {e}")
            # Continue to the next stock if fetching fails
            continue

        # Sleep for a short time to avoid hitting rate limits
        time.sleep(10)

    # Concatenate the dataframes for each stock into a single dataframe
    stock_data = pd.concat(stock_dfs)

    # Return the dataframe
    return stock_data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    # Assert that the output is not None
    assert output is not None, 'The output is undefined'