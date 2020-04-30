import json

def escrever_json(lista):
    with open('meu_arquivo.json', 'w') as f:
        json.dump(lista, f)

def carregar_json(arquivo):
    with open('meu_arquivo.json', 'r') as f:
        return json.load(f)


#a = util_json()


#minha_lista = ['João', 'Maria', 'José']
#escrever_json(minha_lista)

#print(carregar_json('meu_arquivo.json'))  # ['João', 'Maria', 'José']