import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://www.w3schools.com/')

browser.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[1]/a[1]').click()

browser.find_element_by_xpath('//*[@id="topnav"]/div/div/a[10]').click()

browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[117]').click()

first_name = browser.find_element_by_xpath('//*[@id="fname"]')
first_name.click()
first_name.send_keys("나도")

last_name = browser.find_element_by_xpath('//*[@id="lname"]')
last_name.click()
last_name.send_keys("코딩")

country = browser.find_element_by_xpath('//*[@id="country"]/option[text()="Canada"]')
country.click()

subject = browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea')
subject.click()
subject.send_keys("퀴즈 완료하였습니다.")

time.sleep(5)

submit = browser.find_element_by_xpath('//*[@id="main"]/div[3]/a')
submit.click()

time.sleep(5)

browser.quit()