from datetime import datetime

import pytest

from app.pipelines.global_property_sqm.etl.extract import get_file_date


@pytest.mark.parametrize("input_value, expected_output", [
    ('my_test_website-best_data_01-11-2022.csv', datetime(2022, 11, 1)),
    ('my_test_website-best_data_11-01-2018.csv', datetime(2018, 1, 11))])
def test_get_file_date(input_value, expected_output):
    result = get_file_date(input_value)
    assert result == expected_output
