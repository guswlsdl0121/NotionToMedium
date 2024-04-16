from notion_client import Client
from notion_exporter import NotionExporter

def get_notion_client(notion_token):
    """제공된 토큰을 사용하여 Notion 클라이언트 객체를 생성하고 반환합니다."""
    return Client(auth=notion_token)

def verify_notion_login(notion):
    """Notion API 로그인을 시도하여 사용자 목록을 요청함으로써 로그인을 확인합니다."""
    try:
        notion.users.list()
        return True
    except Exception as e:
        print(f"Notion 로그인 실패: {e}")
        return False

def fetch_pages_to_publish(notion, database_id):
    """데이터베이스에서 '발행요청' 상태인 페이지의 ID를 조회합니다."""
    query = {
        "filter": {
            "property": "상태",
            "select": {"equals": "발행요청"}
        }
    }
    try:
        response = notion.databases.query(database_id=database_id, **query)
        return [page['id'] for page in response['results']]
    except Exception as e:
        print(f"페이지 조회 실패: {e}")
        return []


def export_markdown_pages(notion_token, page_ids):
    """지정된 페이지를 마크다운으로 변환하여 로컬에 저장합니다."""
    exporter = NotionExporter(notion_token=notion_token)
    exported_pages = exporter.export_pages(page_ids=page_ids)
    for page_id, content in exported_pages.items():
        filename = f"{page_id}.md"
        with open(filename, 'w', encoding='utf-8') as md_file:
            md_file.write(content)
        print(f"마크다운 파일 저장됨: {filename}")
