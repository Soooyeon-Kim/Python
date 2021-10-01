import requests
from bs4 import BeautifulSoup

def get_href(soup) :
    div = soup.find('ul', class_='type06_headline')
    result = []
    for a in div.find_all('a', class_='nclicks(fls.list)'):
        result.append(a['href'])
    return result
    
def get_request(section) :
    custom_header = {
        'referer' : 'https://www.naver.com/',
        'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    
    url = "https://news.naver.com/main/list.nhn"
    
    sections = {
        "정치": 100,
        "경제": 101,
        "사회": 102,
        "생활": 103,
        "세계": 104,
        "과학": 105
        }
    req = requests.get(url, headers = custom_header,
            params = {"sid1": sections[section]}) # params 매개변수 설정
    return req

def main() :
    list_href = []
    
    # 섹션을 입력하세요.
    section = input('"정치", "경제", "사회", "생활", "세계", "과학" 중 하나를 입력하세요.\n  > ')
    
    req = get_request(section)
    soup = BeautifulSoup(req.text, "html.parser")
    
    list_href = get_href(soup)
    
    print(list_href)


if __name__ == "__main__" :
    main()
