import requests
import os

def verify_medium_login(token):
    """
    Medium API를 통해 로그인 상태를 확인하고, 유저 ID를 반환합니다.
    """
    host = "https://api.medium.com"
    api = "v1/me"
    url = f"{host}/{api}"
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            print("Medium 로그인이 성공했습니다.")
            user_id = response.json()["data"]["id"]
            return user_id
        else:
            print(f"Medium 로그인 실패: HTTP 상태 {response.status_code}")
            return None
    except Exception as e:
        print(f"Medium 로그인 오류: {e}")
        return None


def post_file(token, user_id, pages):
    """Medium에 스토리를 포스팅합니다."""
    host = "https://api.medium.com"
    api = f"v1/users/{user_id}/posts"
    url = f"{host}/{api}"
    headers = {"Authorization": f"Bearer {token}"}

    for page in pages:
        print(page)
        md_file_path = page.markdown_path  # 직접 마크다운 파일 경로 사용
        print(md_file_path)

        if not os.path.exists(md_file_path):
            print(f"마크다운 파일을 찾을 수 없습니다: {md_file_path}")
            continue

        try:
            with open(md_file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            data = {
                "title": page.title,
                "contentFormat": "html",
                "content": content,
                "tags": page.tags,
                "publishStatus": page.publish_type,
            }

            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 201:
                print(f"페이지 '{page.title}'를 Medium에 성공적으로 게시했습니다.")
            else:
                print(f"페이지 '{page.title}'의 게시에 실패했습니다. HTTP 상태 코드: {response.status_code}")
        except Exception as e:
            print(f"페이지 '{page.title}'의 게시 중 오류가 발생했습니다: {e}")