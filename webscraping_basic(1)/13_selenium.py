import time
from selenium import webdriver

browser = webdriver.Chrome() #"./chromedriver.exe"
#1. Move to naver. 
browser.get("http://naver.com")
#2. click login button
elem = browser.find_element_by_class_name("link_login")
elem.click()
#3. Input ID and pW
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

#4. click the log-in button
browser.find_element_by_id("log.login").click()

time.sleep(3)

# browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

#6. Printing html information
print(browser.page_source)
#7. quit browser
#browser.close()  #closing the present tap
browser.quit() # closing the entire browser. 