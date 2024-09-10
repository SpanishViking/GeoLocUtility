import sys
import json
import requests

BASE_URL = "http://api.openweathermap.org/geo/1.0/"
API_KEY = "f897a99d971b5eef57be6fafa0d83239"


def clean_arguments(argv):
    # Remove the file name and location option
    if "--locations" in sys.argv:
        args = argv[2:]
    else:
        args = argv[1:]
    return args


def get_location_data_by_zip(zip):
    return requests.get(BASE_URL + "zip?zip=" + zip + "&limit=5&appid=" + API_KEY).json()


def get_location_data_by_name(name):
    name = name.replace(" ", "")
    return requests.get(BASE_URL + "direct?q=" + name + ",US&limit=5&appid=" + API_KEY).json()


def main(args):
    location_data = []
    cities = clean_arguments(args)
    for city in cities:
        if city.isnumeric():
            location_data.append(json.dumps(get_location_data_by_zip(city), indent=4))
        else:
            location_data.append(json.dumps(get_location_data_by_name(city), indent=4))

    for index, location in enumerate(location_data):
        print(f"Location {index + 1}: " + location)
    return 0


if __name__ == '__main__':
    exit(main(sys.argv))
