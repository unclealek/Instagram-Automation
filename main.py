import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class newthing():
    def newthingbeans(self):
        browser = webdriver.Chrome('/Users/mac/ChromeDriver/chromedriver')

        browser.get('https://www.google.com')
        time.sleep(5)

        browser.title
        print(browser.title)
        '''
        prints the name of the webpage opened
        '''
        search_input = browser.find_element(By.NAME,('q'))
        '''
        gets name of html
        '<input class="gLFyf gsfi" jsaction="paste:puy29d;" maxlength="2048" name="q" type="text" aria-autocomplete="both" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" autofocus="" role="combobox" spellcheck="false" title="Search" value="" aria-label="Search" data-ved="0ahUKEwj6wuCslIv7AhWIQfEDHTk0BmQQ39UDCAU">')
        '''

        search_input.send_keys('What is Automation')
        time.sleep(2)
        '''
        inputs  search word and waits to respond
        '''
        search_button = browser.find_element(By.NAME,('btnK'))
        search_button.click()
        '''
        gets name of html
        <input class="gNO89b" value="Google Search" aria-label="Google Search" name="btnK" role="button" tabindex="0" type="submit" data-ved="0ahUKEwj6wuCslIv7AhWIQfEDHTk0BmQQ4dUDCA4">
        '''
        time.sleep(10)

newthingpee = newthing()
newthingpee.newthingbeans()
newthingpee.quit()

'''
browser waits for 10 seconds before quiting
'''