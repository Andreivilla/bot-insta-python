from InstagramBot import InstagramBot
from util_json import util_json
import time

#dar entrada em informaões do bot
#user = str(input('Usuario: '))
#password = str(input('Senha: '))

#perfil
#photo
user = 'Marvin_Robot63'
password = '36461023'

#login
bot_driver = InstagramBot()
bot_driver.login(user, password)

#foto alvo do bot
#page = str(input('Link da foto: '))
page = "https://www.instagram.com/p/CA36GVqnLYo/"

list = []

while len(list) < 3:
    bot_driver.likes(page, False)
    if bot_driver.verify_private_account():
        continue
    else:
        id_perfil = bot_driver.takeId()
        if id_perfil in list:
            continue
        else:
            list.append(id_perfil)
            time.sleep(5)
            bot_driver.followid(id_perfil, True)
            time.sleep(5)
            


print(list)    



