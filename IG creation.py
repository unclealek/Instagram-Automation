from selenium import webdriver
from selenium.webdriver.common.by import By
import time


ig = webdriver.Chrome(executable_path='/Users/mac/ChromeDriver/chromedriver')

ig.get('https://www.instagram.com')
'''opens web application'''

cookie = ig.find_element(By.CLASS_NAME, "_a9_1")
cookie.click()
'''
cookie = ig.get_cookies()
print(len(cookie))
print(cookie)
'''

ig.maximize_window()
'''
click the sign up button
'''
sign_up = ig.find_element(By.CLASS_NAME, "Sign up")
sign_up.click()
'''
input details from external file already imported
'''
email_field = ig.find_element(By.NAME, 'username')
email_field.send_keys(email1)

Fname_field = ig.find_element(By.NAME, 'username')
Fname_field.send_keys(Fullname)

Username_field = ig.find_element(By.NAME, 'username')
Username_field.send_keys(Username_field1)

Pword_field = ig.find_element(By.NAME, 'username')
Pword_field.send_keys(Password)

'''
click the next button once all fields are filled
'''
sign_up = ig.find_element(By.CLASS_NAME, "Sign up")
sign_up.click()

'''
DOB is a radio button
'''


'''
click the next button once completed
'''



'''
one more step- input the 6-digit code sent to email
'''