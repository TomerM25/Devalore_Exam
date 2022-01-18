import pytest
from main import *


#checking if the status of the json and if the function is return dict
def test_get_json_data():
    data = get_json_data()
    assert data.get("success")
    assert type(data) == dict


#checking if the function is return list
def test_get_rates_lower_than_ten():
    assert type(get_rates_lower_than_ten(get_json_data())) == list


#checking if the function is return list
def test_get_countries_rates():
    assert type(get_countries_rates()) == list