import requests

def verify_medium_login(token):
    """
    Medium API를 통해 로그인 상태를 확인합니다.
    """
    host = "https://api.medium.com"
    api = "v1/me"
    url = f"{host}/{api}"
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            print("Medium 로그인이 성공했습니다.")
            return True
        else:
            print(f"Medium 로그인 실패: HTTP 상태 {response.status_code}")
            return False
    except Exception as e:
        print(f"Medium 로그인 오류: {e}")
        return False
