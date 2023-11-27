import csv
import re
from datetime import datetime

from app.config import CAPITAL_CITY_DATA_PATH, EURO_TO_USD_EXCHANGE_RATE_NOV_2022


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


def convert_str_to_date(date_string, str_format):
    return datetime.strptime(date_string, str_format)


def convert_str_price_to_int(val):
    return float(''.join(val[1:].split(',')))


def convert_to_usd_float(val):
    if val[0] == '$':
        return round(convert_str_price_to_int(val))
    elif val[0] == '€':
        return round(convert_str_price_to_int(val) * EURO_TO_USD_EXCHANGE_RATE_NOV_2022)
    else:
        raise ValueError("Price is neither USD or EURO", val)


def find_brackets(input_str):
    brackets = ['[', ']', '(', ')']
    return [bracket for bracket in brackets if bracket in input_str]


def remove_brackets(input_str, brackets_to_remove):
    # Create a pattern to match any of the characters
    pattern = '|'.join(re.escape(bracket) for bracket in brackets_to_remove)

    # Split the string using the pattern
    parts = re.split(pattern, input_str)

    # Remove parts that follow a bracket
    return parts[0]
