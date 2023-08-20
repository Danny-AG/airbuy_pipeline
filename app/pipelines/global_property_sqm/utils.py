
import pandas as pd

from app.common.utils import map_capital_cities
from app.config import GLOBAL_PROPERTY_SQM_DATA_PATH


def get_global_sqm_prices_df():
    df = pd.read_csv(GLOBAL_PROPERTY_SQM_DATA_PATH)
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
