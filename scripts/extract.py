import pandas

def extract_orders(path: str) -> pandas.DataFrame:
    print('Extracting data')
    return pandas.read_csv(path)