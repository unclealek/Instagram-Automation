import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains


navigate = webdriver.Chrome(executable_path='/Users/mac/ChromeDriver/chromedriver')
navigate.get('https://www.rcvacademy.com/')
join = navigate.find_element(By.XPATH, "(//span[contains(text(),'Join Us')])[1]").click()
time.sleep(1)



navigate.find_element(By.XPATH, "(//input[@id='name'])[1]").send_keys("Kelvin")
navigate.find_element(By.ID, 'last_name').send_keys("Aliche")
navigate.find_element(By.ID, 'email').send_keys("kelvin.aliche@gmail.com")
navigate.find_element(By.CSS_SELECTOR, '#password').send_keys("Combintion99")
navigate.find_element(By.CSS_SELECTOR, '#password_confirmation').send_keys("Combintion99")
check = navigate.find_element(By.CSS_SELECTOR, "#zen-visible-captcha")
check.click()
agree = navigate.find_element(By.CSS_SELECTOR, "div[class='form-group gdprSignupCheckbox'] label[for='gdpr']")
agree.click()
time.sleep(1)
navigate.back()
login = navigate.find_element(By.XPATH, "(//li[@id='menu-item-13329'])[1]").click()
time.sleep(1)
navigate.back()

About = navigate.find_element(By.ID, 'menu-item-11591').click()
time.sleep(2)

Contact = navigate.find_element(By.CSS_SELECTOR, '#menu-item-13847').click()

time.sleep(2)
navigate.find_element(By.XPATH, "(//th)[1]")

