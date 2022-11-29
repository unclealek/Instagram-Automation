import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from falseID import username, password

rcv = webdriver.Chrome(executable_path='/Users/mac/ChromeDriver/chromedriver')
rcv.get('https://www.rcvacademy.com/')
rcv.maximize_window()
time.sleep(5)
rcv.fullscreen_window()
class author():
    def auth(self):
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, = rcv.find_elements(By.CLASS_NAME, 'textwidget')
        print(a.text, b.text, c.text, d.text, e.text, f.text, g.text, h.text, i.text)
        print(j.text, k.text, l.text, m.text, n.text, o.text, p.text)
writer = author()
writer.auth()

with open(f'rcvv_doc.txt', 'w') as file:
    file.write(author())
time.sleep(5)
'''
rcv_doc = rcv.find_elements(By.CLASS_NAME, "elementor-column-wrap elementor-element-populated")

with open(f'{rcv_doc}.txt', 'w') as file:
    file.write(f"Name/Bio\n{'rcv_doc.pdf'}\n")

rcv.back()
time.sleep(2)
login_page = rcv.find_element(By.ID, ('menu-item-13329'))
email = rcv.find_element(By.NAME, ('email'))
email.send_keys(username)

passwords = rcv.find_element(By.NAME, 'password')
passwords.send_keys(password)

login_btn = rcv.find_element(By.CLASS_NAME, 'btn btn-default btn-block btn-md dynamic-button')
login_btn.submit()
time.sleep(5)

rcv.refresh()

al_Courses = rcv.find_element(By.LINK_TEXT, '/courses')

home = rcv.find_element(By.LINK_TEXT, '/')
time.sleep(5)

rcv.minimize_window()
time.sleep(2)

rcv.quit()

'''



