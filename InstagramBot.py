from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path = r'C:\Users\Cliente\Documents\GitHub\bot-insta-python\geckodriver.exe')

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/?hl=pt-br')


Bot = InstagramBot('adwadwa','wdawdwf')
Bot.login()