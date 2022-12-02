from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from igAutomationQuery import USERNAME, PASSWORD


'''
a different .py file was created to hold
the username and password of profile
we call it here
'''
user1 = '******'
user2 = '******'
user3 = '******'
'''
listing users to access account
input usernames to retrive data from
'''

ig = webdriver.Chrome(executable_path='/Users/mac/ChromeDriver/chromedriver')

ig.get('https://www.instagram.com')
'''
opens web application
'''
ig.find_element(By.CLASS_NAME, "_a9_1").click()
cookie = ig.get_cookies()
print(len(cookie))
print(cookie)


ig.maximize_window()

time.sleep(2)
username_field = ig.find_element(By.NAME, 'username')
username_field.send_keys(USERNAME)

password_field = ig.find_element(By.NAME, 'password')
password_field.send_keys(PASSWORD)
'''
inputs username and password from the find 
element syntax using by.name 
'''

login_btn = ig.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
'''
locates the log in button
'''
login_btn.submit()
time.sleep(5)
ig.get(f'https://www.instagram.com/{user1}/')
'''
for user in users:
    ig.get(f'https://www.instagram.com/{user}/')

calling user from users and goes to individual profile
'''
time.sleep(5)
post, followers, following = ig.find_elements(By.CLASS_NAME, "_ac2a")
print('Post=', post.text)
print('Followers=', followers.text)
print('Following=', following.text)
'''
prints individual information on terminal
'''
name_bio = ig.find_element(By.CLASS_NAME, "_aa_c")
print(name_bio.text)
'''
prints name and bio on terminal
'''
f = open("users.txt", "w")
f.write(f"Name/Bio\npost:{post.text}\nfollowers:{followers.text}\nfollowing:{following.text}\nbio:{name_bio.text}+\n\n")

time.sleep(5)
ig.get(f'https://www.instagram.com/{user2}/')

time.sleep(5)
post, followers, following = ig.find_elements(By.CLASS_NAME, "_ac2a")
print('Post=', post.text)
print('Followers=', followers.text)
print('Following=', following.text)

name_bio = ig.find_element(By.CLASS_NAME, "_aa_c")
print(name_bio.text)
f = open("users.txt", "a")
f.write(f"Name/Bio\npost:{post.text}\nfollowers:{followers.text}\nfollowing:{following.text}\nbio:{name_bio.text}+\n\n")


time.sleep(5)
ig.get(f'https://www.instagram.com/{user3}/')

time.sleep(5)
post, followers, following = ig.find_elements(By.CLASS_NAME, "_ac2a")
print('Post=', post.text)
print('Followers=', followers.text)
print('Following=', following.text)

name_bio = ig.find_element(By.CLASS_NAME, "_aa_c")
print(name_bio.text)
f = open("users.txt", "a")
f.write(f"Name/Bio\npost:{post.text}\nfollowers:{followers.text}\nfollowing:{following.text}\nbio:{name_bio.text}+\n\n")

'''
with open(f'{user}.txt', 'w') as file:
    file.write(f"Name/Bio\n{name_bio.text},{post.text}\n,{followers.text}\n,{following.text}\n")

creates a file and saves the gotten users information in that file
'''
time.sleep(3)
ig.quit()
