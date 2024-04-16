import configparser
from notion import fetch_all_database_entries, print_all_entries

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    integration_token = config['NOTION_CREDENTIAL']['APIKey']
    database_id = config['NOTION_CREDENTIAL']['DatabaseId']

    all_entries = fetch_all_database_entries(database_id, integration_token)
    print_all_entries(all_entries)