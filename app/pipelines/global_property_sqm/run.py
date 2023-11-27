from app.config import GLOBAL_PROPERTY_SQM_DATA_PATH
from app.pipelines.global_property_sqm.etl.extract import get_df
from app.pipelines.global_property_sqm.etl.transform import (
    add_metadata,
    clean_city_values,
    clean_currency_columns,
    drop_unnecessary_columns,
    map_cities,
    rearrange_columns,
    rename_columns,
)


def main():
    df = get_df(GLOBAL_PROPERTY_SQM_DATA_PATH)
    df = drop_unnecessary_columns(df)
    df = rename_columns(df)
    add_metadata(df)
    clean_currency_columns(df)
    map_cities(df)
    clean_city_values(df)
    df = rearrange_columns(df)
    print(df)
