from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class test:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path = r'C:\Users\Cliente\Documents\GitHub\bot-insta-python\geckodriver.exe')

    def open(self, page):
        driver = self.driver
        driver.get(page)
        #a = driver.current_url#armazenar url
        a = driver.find_elements_by_xpath('//h2[@class="rkEop"]')
        
        if len(a) == 0:
            return 0
        else:
            return 1

    def verify_private_account(self, page):
        driver = self.driver
        driver.get(page)
        time.sleep(3)
        a = driver.find_elements_by_xpath('//h2[@class="rkEop"]')
        if len(a) == 0:
            return False
        else:
            return True

var_test = test()
#https://www.instagram.com/alanedrica1/
a = var_test.verify_private_account('https://www.instagram.com/alanedrica1/')
print('privada: {}'.format(a))
a = var_test.verify_private_account('https://www.instagram.com/caiobotturapro/')
print('caio: {}'.format(a))
