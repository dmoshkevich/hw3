import pytest
import what_is_year_now
from unittest.mock import patch, MagicMock


@patch('urllib.request.urlopen')
def test_no_current_date(urlopen_mock):
    test_mock = MagicMock()
    test_mock.getcode.return_value = 200
    test_mock.read.return_value = \
        '{' \
        '"$id":"1",' \
        '"currentDT":"2021-04-19T09:50Z",' \
        '"utcOffset":"00:00:00",' \
        '"isDayLightSavingsTime":false,' \
        '"dayOfTheWeek":"Monday",' \
        '"timeZoneName":"UTC",' \
        '"currentFileTime":132632994190993994,' \
        '"ordinalDate":"2021-109",' \
        '"serviceResponse":null' \
        '}'
    test_mock.__enter__.return_value = test_mock
    urlopen_mock.return_value = test_mock

    with pytest.raises(KeyError):
        what_is_year_now.what_is_year_now()


@patch('urllib.request.urlopen')
def test_what_is_year_now(urlopen_mock):
    test_mock = MagicMock()
    test_mock.getcode.return_value = 200
    test_mock.read.return_value = \
        '{' \
        '"$id":"1",' \
        '"currentDateTime":"2021-04-19T09:50Z",' \
        '"utcOffset":"00:00:00",' \
        '"isDayLightSavingsTime":false,' \
        '"dayOfTheWeek":"Monday",' \
        '"timeZoneName":"UTC",' \
        '"currentFileTime":132632994190993994,' \
        '"ordinalDate":"2021-109",' \
        '"serviceResponse":null' \
        '}'
    test_mock.__enter__.return_value = test_mock
    urlopen_mock.return_value = test_mock

    year = what_is_year_now.what_is_year_now()
    assert year == 2021


@patch('urllib.request.urlopen')
def test_what_is_year_now_value_error(urlopen_mock):
    test_mock = MagicMock()
    test_mock.getcode.return_value = 200
    test_mock.read.return_value = \
        '{' \
        '"$id":"1",' \
        '"currentDateTime":"djtfjtfhdf",' \
        '"utcOffset":"00:00:00",' \
        '"isDayLightSavingsTime":false,' \
        '"dayOfTheWeek":"Monday",' \
        '"timeZoneName":"UTC",' \
        '"currentFileTime":132632994190993994,' \
        '"ordinalDate":"2021-109",' \
        '"serviceResponse":null' \
        '}'

    test_mock.__enter__.return_value = test_mock
    urlopen_mock.return_value = test_mock
    with pytest.raises(ValueError):
        what_is_year_now.what_is_year_now()


@patch('urllib.request.urlopen')
def test_what_is_year_now_alternative_format(urlopen_mock):
    test_mock = MagicMock()
    test_mock.getcode.return_value = 200
    test_mock.read.return_value = \
        '{' \
        '"$id":"1",' \
        '"currentDateTime":"19.04.2021T09:50Z",' \
        '"utcOffset":"00:00:00",' \
        '"isDayLightSavingsTime":false,' \
        '"dayOfTheWeek":"Monday",' \
        '"timeZoneName":"UTC",' \
        '"currentFileTime":132632994190993994,' \
        '"ordinalDate":"2021-109",' \
        '"serviceResponse":null' \
        '}'
    test_mock.__enter__.return_value = test_mock
    urlopen_mock.return_value = test_mock

    year = what_is_year_now.what_is_year_now()
    assert year == 2021
