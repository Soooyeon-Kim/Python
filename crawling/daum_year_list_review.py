import time, re, csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import InvalidSelectorException
import pandas as pd

''' 2019 link 50 
# 크롬창(웹드라이버) 열기
driver = webdriver.Chrome('C:/Users/sooyeon/Downloads/chromedriver.exe')

# 2019 페이지 접속
driver.get("https://movie.daum.net/ranking/boxoffice/yearly?date=2019")

time.sleep(2)

# 영화 리스트 불러오기
boxes = driver.find_elements_by_css_selector('#mainContent > div > div.box_boxoffice > ol > li')
link = []
for box in boxes:
    link.append(box.find_element_by_css_selector('a').get_attribute('href'))
    
print(link)
'''

# 크롬창(웹드라이버) 열기
driver = webdriver.Chrome('C:/Users/sooyeon/Downloads/chromedriver.exe')
result = [] # 리뷰 
# len(link) : 50
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
    for i in range(5) : 
        driver.find_element_by_xpath('''//*[@id="alex-area"]/div/div/div/div[3]/div[1]/button''').click()
        time.sleep(1.5) 

        try:
            
            boxes = driver.find_elements_by_css_selector("#alex-area > div > div > div > div.cmt_box > ul.list_comment > li") 

            # 리뷰의 박스들을 의미합니다. 몇개나 출력되는지 확인해주세요 
            #print(boxes)
            score = [] # 평점
            review = [] # 리뷰 
            date = [] # 작성일   

            # 박스를 돌면서 평점, 리뷰, 작성일을 수집합니다. 
            for box in boxes:
                score.append(box.find_element_by_css_selector("li > div > div.ratings").text)
                date.append(box.find_element_by_css_selector("li > div > strong > span > span.txt_date").text)
                review.append(box.find_element_by_css_selector("li > div > p").text)

            # print(score)
            # print(date)
            # print(review)


            df = pd.DataFrame({'score': score, 'date':date,'review':review}) 
            df['title'] = title 

            # df.head()
            result.append(df)

            
             # 예외 처리
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
