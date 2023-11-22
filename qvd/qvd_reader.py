from .qvd import QvdReader
import pandas as pd


def read(file_name):
    reader = QvdReader(file_name)
    data = reader.fetch_rows(10)
    data = reader.fetch_rows(5)
    df = pd.DataFrame.from_dict(data)
    return df


def read_to_dict(file_name):
    reader = QvdReader(file_name)
    data = reader.fetch_rows(10)
    return data
