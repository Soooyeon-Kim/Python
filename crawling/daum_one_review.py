# 크롬창(웹드라이버) 열기
driver = webdriver.Chrome('C:/Users/sooyeon/Downloads/chromedriver.exe')
driver.get("https://movie.daum.net/moviedb/main?movieId=147452") 

time.sleep(2)

result = [] # 각 영화에 포함된 모든 리뷰
score = [] # 평점
review = [] # 리뷰 
date = [] # 작성일 

# 영화 제목 (수집할 데이터는 get에서 받은 영화 제목 단 하나이기 때문에 굳이 리스트로 받을 필요가 없이 문자열로 받아도 충분하다.)
title = driver.find_element_by_css_selector("#mainContent > div > div.box_basic > div.info_detail > div.detail_tit > h3 > span.txt_tit").text

# 출력되는 값이 있는지?
print(title)

# 리뷰 클릭 
driver.find_element_by_xpath('//*[@id="mainContent"]/div/div[2]/div[1]/ul/li[4]/a/span').click()
time.sleep(3)



# 반복문을 통해 리뷰 더보기 클릭 
# 무한루프를 돌다가 더보기를 클릭할 수 없을때 멈춤
# for문으로 수집되는 리뷰 수 수정 가능 
while True : 
    try:
        driver.find_element_by_xpath('''//*[@id="alex-area"]/div/div/div/div[3]/div[1]/button''').click()
        time.sleep(1.5) # sleep 시간 조정
    except:
        break
        # continue

boxes = driver.find_elements_by_css_selector("#alex-area > div > div > div > div.cmt_box > ul.list_comment > li") # 리뷰 더보기가 끝났다면 box들을 수집해봅시다. 

# 리뷰의 박스들
# print(boxes)


# 박스를 돌면서 평점, 리뷰, 작성일을 수집
for box in boxes:
    score.append(box.find_element_by_css_selector("li > div > div.ratings").text)
    date.append(box.find_element_by_css_selector("li > div > strong > span > span.txt_date").text)
    review.append(box.find_element_by_css_selector("li > div > p").text)

# print(score)
# print(date)
# print(review)

# title은 오직 한 개이며, 평점과 일자 리뷰는 box의 개수만큼 생기기 때문에 길이가 맞지않는다.
df = pd.DataFrame({'score': score, 'date':date,'review':review}) # 반복문을 통해 리뷰의 개수만큼 row수가 생성됨

df['title'] = title # 따로 추가해주어야 함
df.head()
