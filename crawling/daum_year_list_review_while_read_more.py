import time, re, csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import InvalidSelectorException
import pandas as pd

# 크롬창(웹드라이버) 열기
driver = webdriver.Chrome('C:/Users/sooyeon/Downloads/chromedriver.exe')

# 연도별 페이지 접속링크
driver.get("https://movie.daum.net/ranking/boxoffice/yearly?date=2020")

time.sleep(2)

# 영화 리스트 불러오기
boxes = driver.find_elements_by_css_selector('#mainContent > div > div.box_boxoffice > ol > li')
link = []
for box in boxes:
    link.append(box.find_element_by_css_selector('a').get_attribute('href')) 

# 크롬창(웹드라이버) 열기
driver = webdriver.Chrome('C:/Users/sooyeon/Downloads/chromedriver.exe')
result = [] 
for i in range(0,50):
    driver.get(link[i]) 

    time.sleep(2)

    # 영화 제목  
    title = driver.find_element_by_css_selector("#mainContent > div > div.box_basic > div.info_detail > div.detail_tit > h3 > span.txt_tit").text

    # print(title)

    # 리뷰 클릭 
    driver.find_element_by_xpath('//*[@id="mainContent"]/div/div[2]/div[1]/ul/li[4]/a/span').click()
    time.sleep(3)



    # 반복문을 통해 리뷰 더보기 클릭 
    while True : 
        try:
            driver.find_element_by_xpath('''//*[@id="alex-area"]/div/div/div/div[3]/div[1]/button''').click()
            time.sleep(1.5) 

        except:
            break
            #continue
            
    boxes = driver.find_elements_by_css_selector("#alex-area > div > div > div > div.cmt_box > ul.list_comment > li")  

    # 리뷰 박스들
    #print(boxes)
    score = [] # 평점
    review = [] # 리뷰 
    date = [] # 작성일   

    # 박스를 돌면서 평점, 리뷰, 작성일을 수집합니다. 
    for box in boxes:
        try:
            score.append(box.find_element_by_css_selector("li > div > div.ratings").text)
            date.append(box.find_element_by_css_selector("li > div > strong > span > span.txt_date").text)
            reviewpre = box.find_element_by_css_selector("li > div > p").text
            reviewpre = reviewpre.replace('\n','')
            review.append(reviewpre)
            
        except NoSuchElementException:
            continue
        except IndexError:
            continue
        except AttributeError:
            continue
        except ValueError:
            continue
        except InvalidSelectorException:
            continue
                    
            # print(score)
            # print(date)
            # print(review)
            
            # df = pd.DataFrame.from_dict({'score': score, 'date':date,'review':review},orient='index').T 
            # df['title'] = title 
            # df.head()
            # result.append(df)


            
    df = pd.DataFrame.from_dict({'score': score, 'date':date,'review':review},orient='index').T 

    df['title'] = title  
    # df.head()
    result.append(df)
    