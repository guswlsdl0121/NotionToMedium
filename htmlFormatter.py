from bs4 import BeautifulSoup

def modify_html_file(html_filename):
    """HTML 파일을 읽고 첫번째 <p> 태그를 삭제하며, 모든 <h2> 태그 앞과 <h1> 태그 뒤에 여러 개의 <br> 태그를 추가합니다."""
    with open(html_filename, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # 첫번째 <p> 태그 삭제
    first_p = soup.find('p')
    if first_p:
        first_p.decompose()

    # 모든 <h2> 태그 찾기 및 각 <h2> 앞에 세 개의 <br> 추가
    for h2 in soup.find_all('h2'):
        for _ in range(3):  # 3번 반복
            h2.insert_before(soup.new_tag('br'))
    
    # <h1> 태그 뒤에 두 개의 <br> 추가
    h1 = soup.find('h1')
    if h1:
        for _ in range(2):  # 2번 반복
            h1.insert_after(soup.new_tag('br'))

    # 변경된 HTML 내용을 파일에 다시 쓰기
    with open(html_filename, 'w', encoding='utf-8') as file:
        file.write(str(soup))