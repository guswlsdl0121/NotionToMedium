from page import Page
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
    """데이터베이스에서 '발행요청' 상태인 페이지의 정보를 조회하고 Page 클래스 인스턴스로 반환합니다."""
    query = {
        "filter": {
            "property": "상태",
            "select": {"equals": "발행요청"}
        }
    }
    pages = []
    try:
        response = notion.databases.query(database_id=database_id, **query)
        for page in response['results']:
            # 페이지 속성 추출
            page_id = page['id']
            title = page['properties']['제목']['title'][0]['text']['content']
            status = page['properties']['상태']['select']['name']
            tags = [tag['name'] for tag in page['properties']['태그']['multi_select']]
            publish_type = page['properties']['발행종류']['select']['name']
            markdown_path = f"/{page_id}.md"

            pages.append(Page(page_id, title, status, tags, publish_type, markdown_path))
        return pages
    except Exception as e:
        print(f"페이지 조회 실패: {e}")
        return []


def export_markdown_pages(notion_token, pages):
    """지정된 페이지들을 마크다운으로 변환하여 로컬에 저장합니다."""
    exporter = NotionExporter(notion_token=notion_token)
    # Page 객체 리스트에서 ID 추출
    page_ids = [page.id for page in pages]
    print(page_ids)
    exported_pages = exporter.export_pages(page_ids=page_ids)
    for page_id, content in exported_pages.items():
        filename = f"{page_id}.md"
        with open(filename, 'w', encoding='utf-8') as md_file:
            md_file.write(content)
        print(f"마크다운 파일 저장됨: {filename}")