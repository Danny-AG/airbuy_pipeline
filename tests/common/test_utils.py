from datetime import datetime

from app.common.utils import convert_str_to_date, is_word_in_string_list


def test_is_word_in_string_list():
    assert is_word_in_string_list('apple', ['Apple', 'Banana', 'Orange'])
    assert is_word_in_string_list('apple', ['apple', 'Banana', 'Orange'])
    assert is_word_in_string_list('apple', ['there might be an apple', 'banana', 'banana'])
    assert not is_word_in_string_list('apple', ['there might be a tomato', 'banana', 'banana'])


def test_convert_str_to_date():
    assert convert_str_to_date('2021-01-01', '%Y-%m-%d') == datetime(2021, 1, 1)
    assert convert_str_to_date('2021-01-01', '%Y-%m-%d').year == 2021
    assert convert_str_to_date('2021-01-01', '%Y-%m-%d').month == 1
    assert convert_str_to_date('2021-01-01', '%Y-%m-%d').day == 1
    assert convert_str_to_date('2021-01-01', '%Y-%m-%d').hour == 0
    assert convert_str_to_date('2021-01-01', '%Y-%m-%d').minute == 0
    assert convert_str_to_date('2021-01-01', '%Y-%m-%d').second == 0
    assert convert_str_to_date('2021-01-01', '%Y-%m-%d').microsecond == 0
    assert convert_str_to_date('2021-01-01', '%Y-%m-%d').tzinfo is None
