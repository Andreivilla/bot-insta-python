from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class test:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path = r'C:\Users\Cliente\Documents\GitHub\bot-insta-python\geckodriver.exe')

    def open(self, page):
        driver = self.driver
        driver.get(page)
        a = driver.current_url#armazenar url
        return a


var_test = test()
a = var_test.open('https://www.instagram.com/p/B_OBO5BBPNe/')
print('a: {}'.format(a))
