import requests
import json


API = "http://api.exchangeratesapi.io/v1/latest?access_key="
# If I had time I would find a better way to encript the ACCESS_KEY
with open("source_file.json", 'r') as f:
    source = json.loads(f.read())
    ACCESS_KEY = source.get("API_KEY")
    ENV = source.get("env")


def get_json_data():
    """
    According to environment reading Json data.
    Prod environment -  return real data from the api.
    Dev environment -  return a mock data.
    
    Raises:
        Exception: If could not get API response raise an Exception.

    Returns:
        dict: dict holding all the Json data that returns from API.
        {"success":true, ...}
    """

    json_data = {}

    if ENV == "prod":
        response = requests.get(f"{API}{ACCESS_KEY}")
        if response.status_code != 200:
            raise Exception(f"Could not get API response {response.reason} HTTP status is {response.status_code}")
        json_data = response.json()
    
    elif ENV == "dev":
        with open("api_response.json", 'r') as f:
            json_data = json.load(f)

    else:
        raise Exception(f"Wrong environment variable {ENV}")
    return json_data


def get_rates_lower_than_ten(json_data):
    """
    Get all names of countries which their currency is less than 10.

    Args:
        json_data (dict): dict from the Json data. 

    Returns:
        list: list holding all countries which their currency is smaller than 10.
        ['AED', ...]
    """

    rates = json_data.get("rates")
    if not rates:
        raise Exception(f"Could not get rates info from json. Available data: {json_data.keys()}")

    rates_lower_ten = [country for country, rate in rates.items() if rate < 10]

    return rates_lower_ten


def get_countries_rates():
    """
    Get all names of countries.

    Returns:
        list: list of all countries.
        ['AED', ...]
    """

    json_data = get_json_data()
    return get_rates_lower_than_ten(json_data)


if __name__ == "__main__":

    print(get_countries_rates())