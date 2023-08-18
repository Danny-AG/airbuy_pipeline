import csv
import pandas as pd
from config import CAPITAL_CITY_DATA_PATH, GLOBAL_SQM_PRICE_DATA_PATH


def is_word_in_string_list(word, string_list):
    return any(word.lower() in string.lower() for string in string_list)


def get_country_capital_dict():
    """Return a dictionary of countries and their capital cities."""

    with open(CAPITAL_CITY_DATA_PATH, 'r') as csv_file:
        # Create a CSV reader
        csv_reader = csv.DictReader(csv_file)
        country_capital_dict = {row['Country']:row['Capital City'] for row in csv_reader}

    return country_capital_dict



def get_global_sqm_prices_df():
    df = pd.read_csv(GLOBAL_SQM_PRICE_DATA_PATH)
    return df


def map_capital_cities(df):
    country_capital_dict = get_country_capital_dict()
    df['Capital City'] = df['Country/City'].map(country_capital_dict)
    return df


def manually_map_missiing_cities(df):
    df.loc[df['Country/City'] == 'Hong Kong', 'Capital City'] = 'Hong Kong'
    df.loc[df['Country/City'] == 'Taiwan', 'Capital City'] = 'Taipei'
    df.loc[df['Country/City'] == 'Puerto Rico', 'Capital City'] = 'San Juan'
    df.loc[df['Country/City'] == 'Czech Republic', 'Capital City'] = 'Prague'
    df.loc[df['Country/City'] == 'Turkey', 'Capital City'] = 'Ankara'


def get_cleaned_global_sqm_prices_df():
    df = get_global_sqm_prices_df()
    map_capital_cities(df)
    manually_map_missiing_cities(df)
    return df
