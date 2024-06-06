import requests
import json
from config import Config

class ZendeskService:
    def __init__(self, base_url=Config.BASE_URL, headers=Config.HEADERS, page_size=Config.PAGE_SIZE):
        self.base_url = base_url
        self.headers = headers
        self.page_size = page_size

    def fetch_data(self, data_key):
        endpoint = f"{self.base_url}/{data_key}"
        params = {'page[size]': self.page_size}
        all_data = []
        while endpoint:
            try:
                response = requests.get(url=endpoint, params=params, headers=self.headers)
                response.raise_for_status()  # Raise an exception for non-200 status codes
                data = response.json()
                all_data.extend(data.get(data_key, []))  # Extend data list
                # Check for next page and update endpoint
                if data.get('meta', {}).get('has_more', False):
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

    @staticmethod
    def write_to_file(data, filename):
        with open(filename, 'w') as outfile:
            json.dump(data, outfile, indent=4)
        print("=================\nSuccessfully written to {}".format(filename))
