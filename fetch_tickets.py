from zendesk_service import fetch_data, write_to_file
from config import BASE_URL

def main():
    """
    THINGS TO EDIT:
    - data_key
    """
    data_key = "tickets"
    result = fetch_data(data_key)
    write_to_file(result, "data/{}.json".format(data_key))

if __name__ == "__main__":
    main()