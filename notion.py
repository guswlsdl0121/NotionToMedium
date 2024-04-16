import requests
import json

def fetch_all_database_entries(database_id, integration_token):
    all_data = []
    # 여기서 최신Notion-Version 확인 : https://developers.notion.com/reference/changes-by-version
    headers = {
        "Authorization": f"Bearer {integration_token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    
    has_more = True
    start_cursor = None
    
    while has_more:
        if start_cursor:
            payload = json.dumps({"start_cursor": start_cursor})
            response = requests.post(url, headers=headers, data=payload)
        else:
            response = requests.post(url, headers=headers)
        
        if response.status_code == 200:
            result = response.json()
            all_data.extend(result['results'])
            has_more = result.get('has_more', False)
            start_cursor = result.get('next_cursor', None)
        else:
            print("오류 발생:", response.status_code, response.text)
            break

    return all_data

def print_all_entries(all_data):
    for entry in all_data:
        print(json.dumps(entry, ensure_ascii=False, indent=4))