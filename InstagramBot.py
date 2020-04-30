from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path = r'C:\Users\Cliente\Documents\GitHub\bot-insta-python\geckodriver.exe')

#função para loguin automatico no instagram
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

#funções para seguir

#seguem pelo id dos usuarios
    def followid(self, idname, inPage = False):#função segue o perfil passado para a função
        driver = self.driver
        #verifica se o bot esta na pagina
        if inPage == False:                 
            driver.get('https://www.instagram.com/{}/'.format(idname))#se o bot não estiver na pagina ele precisa ir até a pagina
            time.sleep(5)
        driver.find_element_by_xpath('//button[@class="_5f5mN       jIbKX  _6VtSN     yZn4P   "]').click()#clica non botão "seguir"

    def unfollowid(self, idname, inPage = False):#funçãoo para deseguir o perfil passaddo para a função
        driver = self.driver
        #verifica se o bot esta na pagina
        if inPage == False:        
            driver.get('https://www.instagram.com/{}/'.format(idname))#se o bot não estiver na pagina ele precisa ir até a pagina
            time.sleep(5)
        
        driver.find_element_by_xpath('//button[@class="_5f5mN    -fzfL     _6VtSN     yZn4P   "]').click()#clica no botão "deseguir" 
        time.sleep(3)
        driver.find_element_by_xpath('//button[@class="aOOlW -Cab_   "]').click()#confirma o unfollow
        
#seguem pelo link de usuarios   
    def followlink(self, link, inPage = False):#função segue o perfil passado para a função
        driver = self.driver
        #verifica se o bot esta na pagina
        if inPage == False:                 
            driver.get(link)#se o bot não estiver na pagina ele precisa ir até a pagina
            time.sleep(5)
        driver.find_element_by_xpath('//button[@class="_5f5mN       jIbKX  _6VtSN     yZn4P   "]').click()#clica non botão "seguir"

    def unfollowlink(self, link, inPage = False):#função para deseguir o perfil passaddo para a função
        driver = self.driver
        #verifica se o bot esta na pagina
        if inPage == False:        
            driver.get(link)#se o bot não estiver na pagina ele precisa ir até a pagina
            time.sleep(5)
        
        driver.find_element_by_xpath('//button[@class="_5f5mN    -fzfL     _6VtSN     yZn4P   "]').click()#clica no botão "deseguir" 
        time.sleep(3)
        driver.find_element_by_xpath('//button[@class="aOOlW -Cab_   "]').click()#confirma o unfollow
        
    #verificar se a conta é privada    
    def verify_private_account(self, page):
        driver = self.driver
        driver.get(page)
        time.sleep(3)
        a = driver.find_elements_by_xpath('//h2[@class="rkEop"]')
        if len(a) == 0:
            return False
        else:
            return True
    
        
    def followers(self, idname, inPage):
        driver = self.driver
        if inPage == False:        
            driver.get('https://www.instagram.com/{}/'.format(idname))#recebe o perfil
            time.sleep(5)
        
        driver.find_element_by_xpath('//a[@href="/{}/followers/"]'.format(idname)).click()
        time.sleep(3)
        driver.find_element_by_xpath('//a[@class="FPmhX notranslate  _0imsa "]').click()
        #a class="-nal3 " href="/caiobotturapro/followers/"
        #