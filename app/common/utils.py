import csv

from app.config import CAPITAL_CITY_DATA_PATH


def is_word_in_string_list(word, string_list):
    return any(word.lower() in string.lower() for string in string_list)


def get_country_capital_dict():
    """Return a dictionary of countries and their capital cities."""

    with open(CAPITAL_CITY_DATA_PATH, 'r') as csv_file:
        # Create a CSV reader
        csv_reader = csv.DictReader(csv_file)
        country_capital_dict = {row['Country']: row['Capital City'] for row in csv_reader}

    return country_capital_dict


def map_capital_cities(df):
    country_capital_dict = get_country_capital_dict()
    df['Capital City'] = df['Country/City'].map(country_capital_dict)
    return df
