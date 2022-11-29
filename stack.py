from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='/Users/mac/ChromeDriver/chromedriver')
driver.get('https://www.libertymutual.com/get-a-quote')
driver.maximize_window()
driver.find_element(By.XPATH,
    '//*[@id="1555468516747"]/section/div[2]/section/form/div[1]/div[3]/div/div[1]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="zipcode-1555468516747-1555468516747"]').click()
driver.find_element(By.XPATH, '//*[@id="zipcode-1555468516747-1555468516747"]').send_keys('03878')
time.sleep(1)
driver.find_element(By.XPATH,
    '//*[@id="1555468516747"]/section/div[2]/section/form/div[2]/div[5]/div/div/button').submit()
time.sleep(5)
x=driver.find_element(By.XPATH, '//*[@id="discount-marketing-modal"]/header/button/svg').click()
driver.refresh()
