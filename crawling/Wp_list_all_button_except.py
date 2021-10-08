import pandas as pd

# 크롬창(웹드라이버) 열기
driver = webdriver.Chrome('C:/Users/sooyeon/Downloads/chromedriver.exe')
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

resultw=[]
linkl = []
url = 'https://pedia.watcha.com/ko-KR/decks/S6rH4jxDhJ8i'
re = requests.get(url)
soup = BeautifulSoup(re.text, "html.parser")
#div = soup.find('div', class_='css-1gkas1x-Grid e1689zdh0').find('ul', class_='css-27z1qm-VisualUl-ContentGrid')
#li = soup.find('div',class_='css-1y901al-Row emmoxnt0').find_all('li',class_='css-1hp6p72')
li = soup.find_all('li',class_='css-1hp6p72')
links = [url + tag.find('a').get('href','') if tag.find('a') else '' for tag in li]
for link in links:
    linkl.append(link.replace('/decks/S6rH4jxDhJ8i/ko-KR','')   ) 
# 2021 페이지 접속   
driver.get(url)
    
# 시간 지연
# time.sleep(2)


for i in range(0,12):
    # i번째 링크 접속하기
    driver.get(linkl[i])

    # 시간 지연 
    time.sleep(1)
    try:
        # 제목
        title = driver.find_element_by_css_selector("#root > div > div.css-1fgu4u8 > section > div > div > div > section > div.css-p3jnjc-Pane.e1svyhwg12 > div > div > div > div > h1").text

        # //*[@id="root"]/div/div[1]/section/div/div/div/div/div/div[1]/div[1]/div/div/section[4]/div[1]/div/header/div/div/a
        #//*[@id="root"]/div/div[1]/section/div/div/div/div/div/div[1]/div[1]/div/div/section[5]/div[1]/div/header/div/div/a
        # 리뷰 더보기 클릭
        driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/section/div/div/div/div/div/div[1]/div[1]/div/div/section[4]/div[1]/div/header/div/div/a').click()
        
        # 평점
        score = []
        # 리뷰 내용
        content= []

        boxes = driver.find_elements_by_css_selector("#root > div > div.css-1fgu4u8 > section > section > div > div > div > ul")

        SCROLL_PAUSE_SEC = 1

        # 스크롤 높이 가져옴
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # 끝까지 스크롤 다운
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # 1초 대기
            time.sleep(SCROLL_PAUSE_SEC)

            # 스크롤 다운 후 스크롤 높이 다시 가져옴
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        for i in range(1,40):
            try:
                for box in boxes:
                    score.append(box.find_element_by_css_selector(f"div:nth-child({i}) > div.css-4obf01 > div.css-yqs4xl > span").text)
                    contentpre = box.find_element_by_css_selector(f"div:nth-child({i}) > div.css-4tkoly > div > span").text
                    contentpre = contentpre.replace('\n','')
                    content.append(contentpre)
            except:
                continue

        df = pd.DataFrame({'title':title,'score':score,'content':content})
        resultw.append(df)
    except NoSuchElementException:
        # 리뷰 더보기 클릭
        driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/section/div/div/div/div/div/div[1]/div[1]/div/div/section[5]/div[1]/div/header/div/div/a').click()
        
        # 평점
        score = []
        # 리뷰 내용
        content= []

        boxes = driver.find_elements_by_css_selector("#root > div > div.css-1fgu4u8 > section > section > div > div > div > ul")

        SCROLL_PAUSE_SEC = 1

        # 스크롤 높이 가져옴
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # 끝까지 스크롤 다운
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # 1초 대기
            time.sleep(SCROLL_PAUSE_SEC)

            # 스크롤 다운 후 스크롤 높이 다시 가져옴
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        for i in range(1,40):
            try:
                for box in boxes:
                    score.append(box.find_element_by_css_selector(f"div:nth-child({i}) > div.css-4obf01 > div.css-yqs4xl > span").text)
                    contentpre = box.find_element_by_css_selector(f"div:nth-child({i}) > div.css-4tkoly > div > span").text
                    contentpre = contentpre.replace('\n','')
                    content.append(contentpre)
            except:
                continue

        df2 = pd.DataFrame({'title':title,'score':score,'content':content})
        resultw.append(df2)
        continue
    except IndexError:
        continue
