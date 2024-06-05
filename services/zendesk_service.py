import requests
import json
from config import HEADERS, PAGE_SIZE, BASE_URL

def fetch_data(data_key):
    endpoint = f"{BASE_URL}/{data_key}"
    params = {'page[size]': PAGE_SIZE}
    all_data = []
    while endpoint:
        try:
            response = requests.get(url=endpoint, params=params, headers=HEADERS)
            response.raise_for_status()  # Raise an exception for non-200 status codes
            data = response.json()
            all_data.extend(data.get(data_key))  # Extend data list
            # Check for next page and update endpoint
            if data['meta']['has_more']:
                endpoint = data['links']['next']
                print("Next URL: {}".format(endpoint))
            else:
                endpoint = None  # Exit the loop if there are no more pages
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving data: {e}")
            break
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON data: {e}")
            break
    return all_data

def write_to_file(data, filename):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent=4)
    print("=================\nSuccessfully written to {}".format(filename))
