import os

ROOT_DIR = os.path.abspath('')

DATA_DIR = os.path.join(ROOT_DIR, 'data')

CAPITAL_CITY_DATA_PATH = os.path.join(DATA_DIR, 'country_capital_city.csv')

AIRBNB_DATA_URL = "http://insideairbnb.com/get-the-data/"
AIRBNB_DATA_DIR = os.path.join(DATA_DIR, 'listings')

GLOBAL_PROPERTY_SQM_DATA_PATH = os.path.join(
    DATA_DIR, 'global_property_guide-global_sqm_prices_by_country_01-11-2022.csv')
