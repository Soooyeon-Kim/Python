import time, re, csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:/Users/sooyeon/Downloads/chromedriver.exe')
driver.get(
    "https://movie.naver.com/movie/bi/mi/point.naver?code=99702"
)
time.sleep(2)

# 영화 제목
driver.find_element_by_css_selector("#content > div.article > div.mv_info_area > div.mv_info > h3 > a").text

# 출연진
driver.find_element_by_css_selector("#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(6)").text

driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[4])
result = []

# pagination 
for i in range(1,11):

    boxes = driver.find_elements_by_css_selector("body > div > div > div.score_result > ul > li")

    scores = []
    reviews= []
    ids = []
    dates = []
    for box in boxes:
        scores.append(box.find_element_by_css_selector("div.star_score > em").text)
        reviews.append(box.find_element_by_css_selector("div.score_reple > p").text)
        ids.append(box.find_element_by_css_selector("div.score_reple > dl > dt > em:nth-child(1)").text)
        dates.append(box.find_element_by_css_selector("div.score_reple > dl > dt > em:nth-child(2)").text)

    import pandas as pd

    df = pd.DataFrame({'id':ids,'score':scores,'date':dates,'review':reviews})
    # 영화 제목 입력
    df['movie_name'] = '007 노 타임 투 다이'
    result.append(df)
    driver.find_element_by_xpath('''//*[@id="pagerTagAnchor{}"]'''.format(str(i))).click()

# 데이터 프레임
naver_m = pd.concat(result).reset_index(drop=True)
# csv 변환
naver_m.to_csv('tmp_naver_movie.csv',index=False)

