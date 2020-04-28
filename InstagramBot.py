from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path = r'C:\Users\Cliente\Documents\GitHub\bot-insta-python\geckodriver.exe')

    def login(self, username, password):# a função lloguiun deve receber loguin e senha
        driver = self.driver
        driver.get('https://www.instagram.com/?hl=pt-br')
        time.sleep(5)
        
        #entrada do nome do perfil
        user = driver.find_element_by_xpath("//input[@name='username']")# Passa o caminho do usuario
        user.clear()
        user.send_keys(username)#preenche o campo do usuario com o nome passado pelo usuario
        
        #entrada da senha do perfil
        password_item = driver.find_element_by_xpath("//input[@type='password']")# Passa o caminho da senha
        password_item.clear()
        password_item.send_keys(password)#preenche o campo do usuario com a senha passada pelo usuario
        password_item.send_keys(Keys.RETURN)
        time.sleep(5)

    def follow(self, page):
        driver = self.driver
        
        driver.get(page)

        driver.find_element_by_xpath('//a[@href="/python.bot/followers/"]').click()

        #//a[@href="/python.bot/followers/"]
        #<a class="-nal3 " href="/python.bot/followers/"><span class="g47SY " title="64">64</span> seguidores</a>