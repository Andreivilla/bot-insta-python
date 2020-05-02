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


#seguir por perfil
#id_perfil = str(input('Id do perfil: '))
id_perfil = 'caiobotturapro'


for i in range(10):
