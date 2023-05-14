from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get("https://www.gmail.com")

emailEl = browser.find_element(by=By.ID, value="identifierId")
emailEl.send_keys("shamsut@gmail.com")

next = browser.find_element(by=By.ID, value="identifierNext")
next.click()
