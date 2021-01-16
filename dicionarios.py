d1 = {}                #primeira forma de declarar dicionarios
print(d1)
d1['aaa'] = 1000
print(d1)
d1['bbb'] = 2000
d1['ccc'] = 3000
print(d1)
print(d1['ccc'])
d2 = {1.1:"chave1",1.2:"chave2"}   # outra forma de instanciar
print(d2)
print(d2[1.1])
d3 = {22221214: "marcio", 55454124: "santana", 6658877: "gomes", 1245445: "vicente"}
print(d3)
print(d3.__len__())    # funcao para contar quantos elementos
del(d3[1245445])       # funcao para deletar elemento
print(d3)
print(d3.keys())       # funcao para retornar chaves
print(d3.values())     # funcao para retornar valores
print(d3.get(22221214)) # funcao get para retornar valor
print(55454124 in d3)   # funcao para verificar se um lemento esta contido
d4 = {9999: "tata", 55555: "tete"}
print(d4)
d3.update(d4)           # funcao para mesclar dois dicionarios
print(d3)

