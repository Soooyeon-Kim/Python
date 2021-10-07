# Watchapedia review / scrolling X
# Selenium / Chromedriver

# 크롬창(웹드라이버) 열기
driver = webdriver.Chrome('C:/Users/sooyeon/Downloads/chromedriver.exe')
# 영화 페이지 접속
driver.get("https://pedia.watcha.com/ko-KR/contents/m5GXz42")

result = []

# 제목
title = driver.find_element_by_css_selector("#root > div > div.css-1fgu4u8 > section > div > div > div > section > div.css-p3jnjc-Pane.e1svyhwg12 > div > div > div > div > h1").text



# 리뷰 더보기 클릭
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/section/div/div/div/div/div/div[1]/div[1]/div/div/section[5]/div[1]/div/header/div/div/a').click()

score = []
content= []

boxes = driver.find_elements_by_css_selector("#root > div > div.css-1fgu4u8 > section > section > div > div > div > ul")

for i in range(1,28):
    try:
        for box in boxes:
            score.append(box.find_element_by_css_selector(f"div:nth-child({i}) > div.css-4obf01 > div.css-yqs4xl > span").text)
            content.append(box.find_element_by_css_selector(f"div:nth-child({i}) > div.css-4tkoly > div > span").text)
    except:
        continue
        
df = pd.DataFrame({'title':title,'score':score,'content':content})
result.append(df)