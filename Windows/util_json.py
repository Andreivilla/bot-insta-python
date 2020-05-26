import json


class util_json():

    def write_json(self, archive, lista):
        with open(archive, 'w') as f:
            json.dump(lista, f)

    def load_json(self, archive):
        with open(archive, 'r') as f:
            return json.load(f)


#minha_lista = []
#dic = {}

#for i in range(0, 10, +1):
#    minha_lista.append(input('{}'.format(i)))

#dic['a'] = minha_lista

#a = util_json()

#a.write_json('meu_arquivo.json', dic)

#print(a.load_json('meu_arquivo.json'))

#dic2 = a.load_json('meu_arquivo.json')

#dic2['b'] =  ['adawfdag', 'sgrdgr', 'dthdrh']
#del dic2['a']

#a.write_json('meu_arquivo.json', dic2)
#'meu_arquivo.json'