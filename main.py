import sys
import configparser
from notion import get_notion_client, verify_notion_login, fetch_pages_to_publish, export_markdown_pages
from medium import verify_medium_login

def load_config():
    """config.ini 파일에서 토큰과 데이터베이스 ID를 로드합니다."""
    config = configparser.ConfigParser()
    config.read('config.ini')
    return (config['MEDIUM_CREDENTIAL']['INTEGRATION_TOKEN'],
            config['NOTION_CREDENTIAL']['INTEGRATION_TOKEN'],
            config['NOTION_CREDENTIAL']['DatabaseId'])

def main():
    medium_token, notion_token, database_id = load_config()
    notion = get_notion_client(notion_token)
    if not verify_notion_login(notion):
        sys.exit("Notion API 연결 실패.")
    
    pages = fetch_pages_to_publish(notion, database_id)
    if not pages:
        sys.exit("내보낼 페이지가 없습니다.")
    
    export_markdown_pages(notion_token, pages)
    
    if not verify_medium_login(medium_token):
        sys.exit("Medium API 연결 실패.")

if __name__ == '__main__':
    main()
