import os
from zendesk_service import ZendeskService

def main():
    data_key = "users"
    service = ZendeskService()
    result = service.fetch_data(data_key)
    filename = f"data/{data_key}.json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    service.write_to_file(result, filename)

if __name__ == "__main__":
    main()
