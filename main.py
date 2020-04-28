from InstagramBot import InstagramBot
import time

#usuario = str(input('Usuario: '))
#senha = str(input('Senha: '))

usuario = 'Marvin_Robot63'
senha = '36461023'

Bot = InstagramBot()
Bot.login(usuario, senha)
Bot.followers('caiobotturapro', False)


#Bot.follow('https://www.instagram.com/caiobotturapro/?hl=pt-br', False)
#time.sleep(5)
#Bot.unfollow('https://www.instagram.com/caiobotturapro/?hl=pt-br', True)