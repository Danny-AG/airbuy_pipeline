import pandas as pd


def get_df(file_path):
    df = pd.read_csv(file_path)
    return df
