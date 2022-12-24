import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains


amazon = webdriver.Chrome(executable_path='/Users/mac/ChromeDriver/chromedriver')
amazon.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
'''
to fill in details 
'''
login = amazon.find_element(By.ID, "ap_email")
login.send_keys('08133751234')
time.sleep(2)
amazon.find_element(By.ID, "continue").click()

'''
click the forgot password button
'''
forgot = amazon.find_element(By.XPATH, "(//a[normalize-space()='Forgot your password?'])[1]").click()
amazon.find_element(By.ID, "continue").click()

time.sleep(2)
amazon.quit()