from selenium import webdriver
from selenium.webdriver.common.by import By
import time

ig = webdriver.Chrome(executable_path='/Users/mac/ChromeDriver/chromedriver')

ig.get('https://www.instagram.com')

time.sleep(3)
ig.find_element(By.CLASS_NAME, "_a9_1").click()

#ig.switch_to_alert().accept()

