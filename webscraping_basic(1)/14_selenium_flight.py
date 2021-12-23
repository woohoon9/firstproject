from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

url = "https://flight.naver.com/"
browser.get(url)

browser.find_element_by_link_text("가는 날").click()
# selecting 27th and 28th this month. 
# browser.find_elements_by_link_text("27")[0].click()
# browser.find_elements_by_link_text("28")[0].click()


# selecting 27th and 28th next month. 
browser.find_elements_by_link_text("27")[1].click()
browser.find_elements_by_link_text("28")[1].click()