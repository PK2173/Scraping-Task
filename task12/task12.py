# import json


# with open('/home/praveen/Desktop/web scraping tasks/task1.py/task1s.json','r') as d:
    # details=json.load(d)
# for i in details:
# //*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/h1

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# chrome_path='/home/praveen/Desktop/web scraping tasks/chromedriver'
driver=webdriver.Chrome('./chromedriver')
url='https://thegreatestbooks.org/'
driver.get(url)
print(driver)


