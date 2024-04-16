import configparser
from notion import get_notion_client, verify_notion_login, fetch_pages_to_publish, export_markdown_pages

def load_config():
    """config.ini 파일로부터 토큰과 데이터베이스 id를 가져옵니다."""
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['NOTION_CREDENTIAL']['INTEGRATION_TOKEN'], config['NOTION_CREDENTIAL']['DatabaseId']

def main():
    notion_token, database_id = load_config()
    notion = get_notion_client(notion_token)
    if verify_notion_login(notion):
        print("API연결이 확인됐습니다.")
        page_ids = fetch_pages_to_publish(notion, database_id)
        if page_ids:
            export_markdown_pages(notion_token, page_ids)
        else:
            print("Markdown으로 추출할 이미지가 존재하지 않습니다.")
    else:
        print("API연결에 실패했습니다. 토큰을 확인하세요.")

if __name__ == '__main__':
    main()