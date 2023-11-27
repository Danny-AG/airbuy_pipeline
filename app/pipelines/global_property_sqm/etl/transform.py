import pandas as pd

from app.common.utils import (
    convert_to_usd_float,
    find_brackets,
    get_country_capital_dict,
    map_capital_cities,
    remove_brackets,
)
from app.config import GLOBAL_PROPERTY_SQM_FILE_NAME, GLOBAL_PROPERTY_SQM_SOURCE_URL
from app.pipelines.global_property_sqm.utils import convert_global_sqm_str_to_date


def manually_map_missiing_cities(df):
    df.loc[df['country'] == 'Hong Kong', 'city'] = 'Hong Kong'
    df.loc[df['country'] == 'Taiwan', 'city'] = 'Taipei'
    df.loc[df['country'] == 'Puerto Rico', 'city'] = 'San Juan'
    df.loc[df['country'] == 'Czech Republic', 'city'] = 'Prague'
    df.loc[df['country'] == 'Turkey', 'city'] = 'Ankara'


def clean_global_sqm_prices(df):
    map_capital_cities(df)
    manually_map_missiing_cities(df)
    return df


def drop_unnecessary_columns(df):
    return df.drop(columns=['Price/Rent\nRatio (x)', 'Gross\nRental Yield'])


def rename_columns(df):
    return df.rename(columns={'Country/City': 'country',
                              'Buying Price\nUS $ per Sq. M.': 'purchase_price_per_sqm_usd',
                              'Rent per\nMonth ($ or €)': 'rent_per_month_usd'})


def get_file_date(file_name):
    date_of_data = file_name.split('_')[-1][:-4]
    return convert_global_sqm_str_to_date(date_of_data)


def add_metadata(df):
    file_date = get_file_date(GLOBAL_PROPERTY_SQM_FILE_NAME)
    df['data_source_date'] = file_date
    df['data_source_url'] = GLOBAL_PROPERTY_SQM_SOURCE_URL


def get_usd_value_for_row_element(row, column_name):
    try:
        result = convert_to_usd_float(row[column_name])
        return result
    except ValueError as e:
        print(f"Exception occurred at element {column_name} in row: {row}")
        print("Error:", e)
        return None  # Return a value or indicator of failure


def clean_currency_columns(df):
    df['rent_per_month_usd'] = df.apply(get_usd_value_for_row_element, args=['rent_per_month_usd'], axis=1)
    df['purchase_price_per_sqm_usd'] = df.apply(get_usd_value_for_row_element,
                                                args=['purchase_price_per_sqm_usd'],
                                                axis=1)
    df['rent_per_month_usd'] = df['rent_per_month_usd'].astype(pd.Int64Dtype())


def map_cities(df):
    country_capital_dict = get_country_capital_dict()
    df['city'] = df['country'].map(country_capital_dict)
    manually_map_missiing_cities(df)


def remove_bracketed_info(input_str):
    brackets_to_remove = find_brackets(input_str)
    if len(brackets_to_remove) == 0:
        result = input_str
    else:
        result = remove_brackets(input_str, brackets_to_remove).rstrip()

    return result


def clean_city_values(df):
    df['city'] = df['city'].apply(remove_bracketed_info)


def rearrange_columns(df):
    return pd.concat([df['city'], df.drop('city', axis=1)], axis=1)
