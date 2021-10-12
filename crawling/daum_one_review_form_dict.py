# 크롬창(웹드라이버) 열기
driver = webdriver.Chrome('C:/Users/sooyeon/Downloads/chromedriver.exe')
driver.get("https://movie.daum.net/moviedb/grade?movieId=126143") 

time.sleep(2)

result = [] # 

# 영화 제목 
title = driver.find_element_by_css_selector("#mainContent > div > div.box_basic > div.info_detail > div.detail_tit > h3 > span.txt_tit").text
# print(title)

# 리뷰 클릭 
driver.find_element_by_xpath('//*[@id="mainContent"]/div/div[2]/div[1]/ul/li[4]/a/span').click()

# 로딩
time.sleep(3)


for i in range(2) : 
    driver.find_element_by_xpath('''//*[@id="alex-area"]/div/div/div/div[3]/div[1]/button''').click()
    time.sleep(1.5) 
    
    try:
        # 리뷰 박스
        boxes = driver.find_elements_by_css_selector("#alex-area > div > div > div > div.cmt_box > ul.list_comment > li") # 리뷰 더보기가 끝났다면 box들을 수집해봅시다. 
        # print(boxes)   

        score = [] # 평점
        review = [] # 리뷰 
        date = [] # 작성일   
        
        # 박스를 돌면서 평점, 리뷰, 작성일 수집
        for box in boxes:
            score.append(box.find_element_by_css_selector("li > div > div.ratings").text)
            date.append(box.find_element_by_css_selector("li > div > strong > span > span.txt_date").text)
            reviewpre = box.find_element_by_css_selector("li > div > p").text
            reviewpre = reviewpre.replace('\n','')
            review.append(reviewpre)
        

        df = pd.DataFrame.from_dict({'score': score, 'date':date,'review':review},orient='index').T
        df['title'] = title
        df.head()
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