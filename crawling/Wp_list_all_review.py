# link list all

# import list
import requests
from urllib.request import urlopen

import time, re, csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

import pandas as pd

# 크롬창(웹드라이버) 열기
driver = webdriver.Chrome('C:/Users/sooyeon/Downloads/chromedriver.exe')

# 최종 리뷰 수집 리스트
resultw=[]

# 한 페이지 내부의 영화 모음 링크
linkl = []

# 2019년 개봉 영화 수록 url 
url = 'https://pedia.watcha.com/ko-KR/decks/rjNrOHQZF45G'
re = requests.get(url)
soup = BeautifulSoup(re.text, "html.parser")
#div = soup.find('div', class_='css-1gkas1x-Grid e1689zdh0').find('ul', class_='css-27z1qm-VisualUl-ContentGrid')
#li = soup.find('div',class_='css-1y901al-Row emmoxnt0').find_all('li',class_='css-1hp6p72')

# 각 영화마다 선택할 박스들
li = soup.find_all('li',class_='css-1hp6p72')

# 링크 리스트 안담겼던 오류 수정 
links = [url + tag.find('a').get('href','') if tag.find('a') else '' for tag in li]

# css selector로 얻어진 href 정보로는 영화 상세 페이지로 접근할 수 없었음
# 출력해서 확인해보니 추가적인 str 정보가 붙어있어서 반복문을 사용하여 각 링크마다 replace로 제거해서 link 리스트에 다시 담아주는 과정을 거침

for link in links:
    linkl.append(link.replace('/decks/rjNrOHQZF45G/ko-KR','')) 

# 2021 페이지 접속   
driver.get(url)
    
# 시간 지연
# time.sleep(2)

# 한 페이지에 보여지는 영화의 수는 12개 4X3
for i in range(0,12):
    # i번째 링크 접속하기
    driver.get(linkl[i])

    # 시간 지연 
    time.sleep(1)

    try:

        # 영화 제목
        title = driver.find_element_by_css_selector("#root > div > div.css-1fgu4u8 > section > div > div > div > section > div.css-p3jnjc-Pane.e1svyhwg12 > div > div > div > div > h1").text


        # 리뷰 더보기 클릭
        driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/section/div/div/div/div/div/div[1]/div[1]/div/div/section[5]/div[1]/div/header/div/div/a').click()
        
        # 평점
        score = []

        # 리뷰 내용
        content= []

        # 각 리뷰에 해당하는 박스 선택
        boxes = driver.find_elements_by_css_selector("#root > div > div.css-1fgu4u8 > section > section > div > div > div > ul")

        # 대기 시간 정의
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

        # 최대 가져올 수 있는 리뷰 개수를 지정 후 반복문
        # chrome에서 제공해주는 영화 리뷰는 최대 20개
        for i in range(1,20):
            try:
                for box in boxes:
                    score.append(box.find_element_by_css_selector(f"div:nth-child({i}) > div.css-4obf01 > div.css-yqs4xl > span").text)
                    contentpre = box.find_element_by_css_selector(f"div:nth-child({i}) > div.css-4tkoly > div > span").text
                    contentpre = contentpre.replace('\n','')
                    content.append(contentpre)
            except:
                continue

        # 데이터 프레임 생성 
        df = pd.DataFrame({'title':title,'score':score,'content':content})
        resultw.append(df)

    # 예외 처리
    except NoSuchElementException:
        continue
    except IndexError:
        continue