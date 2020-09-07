import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from LoginInfo import username, password, target, message


class MyBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def WebIn(self):
        self.driver.get('https://www.messenger.com')

        time.sleep(1)

        fb_login = self.driver.find_element_by_xpath('//*[@id="email"]')
        fb_login.send_keys(username)

        fb_login_password = self.driver.find_element_by_xpath('//*[@id="pass"]')
        fb_login_password.send_keys(password)

        fb_login_click = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        fb_login_click.click()

        fb_search = self.driver.find_element_by_xpath('//*[@id="js_u"]/div/div/div[1]/span[1]/label/input')
        fb_search.send_keys(target)

        time.sleep(1)

        fb_target = self.driver.find_element_by_xpath('//*[@id="js_u"]/div/div/div[1]/span[1]/div/div/div[2]/ul/li/a/div/div[2]/div/div')
        fb_target.click()

        time.sleep(1)

        fb_target_msgbox_in = self.driver.find_element_by_class_name('notranslate')
        fb_target_msgbox_in.send_keys('This is an automated messenger' + Keys.RETURN)
        while True:
            fb_target_msgbox_in.send_keys(message + Keys.RETURN)
            print(f'{message} (sent)')
            time.sleep(0.25)



bot = MyBot()
bot.WebIn()
