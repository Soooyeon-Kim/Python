import pandas as pd
# 크롬창(웹드라이버) 열기
driver = webdriver.Chrome('C:/Users/sooyeon/Downloads/chromedriver.exe')

from urllib.request import urlopen
from bs4 import BeautifulSoup

# 한 페이지당 20개 링크 
link = []
title = []
genre = []
nation = []
running = []
release = []
director = []
actor = []
grade = []
story = []  
poster = []

# 2021년 개봉영화 디렉토리는 총 37페이지(10월 기준)
for page in range(1,38):
    url = f'https://movie.naver.com/movie/sdb/browsing/bmovie.naver?open=2021&page={page}'
    html = urlopen(url)
    soup = BeautifulSoup(html,'html.parser')
    # 한 페이지마다 영화 목록의 박스 
    ul = soup.find('div').find('ul',class_='directory_list')
    # a 태그의 href 를 통해 각 영화의 상세정보 페이지에 접속
    for a in ul.find_all('a'):
        link.append(a['href'])
    
    # 2021 페이지 접속   
    driver.get(url)
    
    # 시간 지연
    #time.sleep(2)

    # 리스트 정의
    result = []

    # 영화 리스트 불러오기
    boxes = driver.find_elements_by_css_selector("#old_content > ul > li")
    link = []
    
    
    for box in boxes:
        link.append(box.find_element_by_css_selector('a').get_attribute('href'))

    # 링크 한줄 씩 반복문
    # 한 페이지당 해당하는 영화는 20개


    for i in range(0,20):
        # i번째 링크 접속하기
        driver.get(link[i])

        # 시간 지연 
        time.sleep(1)

        try:
            # 속성정보를 변수에 할당 

            # 제목
            tmp1_ = driver.find_element_by_css_selector("#content > div.article > div.mv_info_area > div.mv_info > h3 > a").text
            # 장르
            tmp2_ = driver.find_element_by_css_selector("#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1)").text
            # 국가
            tmp3_ = driver.find_element_by_css_selector("#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(2) > a").text
            # 러닝타임
            tmp4_ = driver.find_element_by_css_selector("#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(3)").text
            # 개봉일
            tmp5_ = driver.find_element_by_css_selector("#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(4)").text
            # 감독
            tmp6_ = driver.find_element_by_css_selector("#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(4)").text
            # 출연
            tmp7_ = driver.find_element_by_css_selector("#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(6) > p").text
            # 등급
            tmp8_ = driver.find_element_by_css_selector("#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(8) > p > a").text
            
            # 포스터 url
            tmp9_=driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[2]/a/img').get_attribute('src')

            # 줄거리
            storypre = driver.find_element_by_css_selector("#content > div.article > div.section_group.section_group_frst > div:nth-child(1) > div > div > p").text

            # replace 후 다시 변수 적용
            storypre = storypre.replace("\n","")

            # 할당된 변수들을 list에 append
            title.append(tmp1_)
            genre.append(tmp2_)
            nation.append(tmp3_)
            running.append(tmp4_)
            release.append(tmp5_)
            director.append(tmp6_)
            actor.append(tmp7_)
            grade.append(tmp8_)
            poster.append(tmp9_)
            story.append(storypre)


        except NoSuchElementException:
            continue
    
    # 데이터 프레임 생성
    posm21 = pd.DataFrame.from_dict({'title':title,'genre':genre,'nation':nation,'running':running, 'release':release, 'director':director, 'actor':actor, 'grade':grade, 'story':story, 'poster':poster},orient='index').transpose()
