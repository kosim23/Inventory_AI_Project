import pandas as pd

def get_latest_data(file_path='data/raw/retail_sales.csv'):
    """
    Маълумотлар омборидан ёки CSV-дан янги маълумотларни юклайди.
    """
    try:
        data = pd.read_csv(file_path, index_col='date', parse_dates=True)
        return data
    except Exception as e:
        print(f"Маълумотни юклашда хато: {e}")
        return None