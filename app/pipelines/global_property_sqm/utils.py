from app.common.utils import convert_str_to_date
from app.config import GLOBAL_PROPERTY_DATE_STR_FORMAT


def convert_global_sqm_str_to_date(date_string):
    return convert_str_to_date(date_string, GLOBAL_PROPERTY_DATE_STR_FORMAT)
