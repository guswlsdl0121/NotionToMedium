from notion_client import Client
from notion_exporter import NotionExporter

def get_notion_client(notion_token):
    """클라이언트 객체 생성"""
    return Client(auth=notion_token)

def verify_notion_login(notion):
    """로그인 확인"""
    try:
        notion.users.list()
        print("Notion에 성공적으로 로그인했습니다.")
        return True
    except Exception as e:
        print(f"Notion에 로그인을 실패하였습니다: {e}")
        return False

def fetch_pages_to_publish(notion, database_id):
    """데이터베이스에서 "발행요청" 상태의 페이지를 조회합니다."""
    query = {
        "filter": {
            "property": "상태",
            "select": {"equals": "발행요청"}
        }
    }
    try:
        response = notion.databases.query(database_id=database_id, **query)
        page_ids = [page['id'] for page in response['results']]
        if not page_ids:
            print("'발행요청'상태의 페이지가 존재하지 않습니다.")
        return page_ids
    except Exception as e:
        print(f"api에 대한 응답을 받아오지 못했습니다: {e}")
        return []

def export_markdown_pages(notion_token, page_ids):
    """마크다운 파일을 추출해서 저장합니다."""
    exporter = NotionExporter(notion_token=notion_token)
    exported_pages = exporter.export_pages(page_ids=page_ids)
    for page_id, content in exported_pages.items():
        filename = f"{page_id}.md"
        with open(filename, 'w', encoding='utf-8') as md_file:
            md_file.write(content)
        print(f"마크다운 파일이 저장되었습니다. {filename}")