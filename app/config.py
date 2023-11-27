import os

ROOT_DIR = os.path.abspath('../')

DATA_DIR = os.path.join(ROOT_DIR, 'data')

CAPITAL_CITY_DATA_PATH = os.path.join(DATA_DIR, 'country_capital_city.csv')

# Inside Airbnb data
AIRBNB_DATA_URL = "http://insideairbnb.com/get-the-data/"
AIRBNB_DATA_DIR = os.path.join(DATA_DIR, 'listings')

# Global Property Guide data
GLOBAL_PROPERTY_SQM_FILE_NAME = 'global_property_guide-global_sqm_prices_by_country_01-11-2022.csv'
GLOBAL_PROPERTY_SQM_DATA_PATH = os.path.join(DATA_DIR, GLOBAL_PROPERTY_SQM_FILE_NAME)
GLOBAL_PROPERTY_SQM_SOURCE_URL = r'https://www.globalpropertyguide.com/most-expensive-cities'

GLOBAL_PROPERTY_DATE_STR_FORMAT = '%d-%m-%Y'


EURO_TO_USD_EXCHANGE_RATE_NOV_2022 = 1.0098
