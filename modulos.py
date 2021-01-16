# importacao de modulos

import math   # math modulo recursos matematicos

print(math.cos(30))
e = math.e
print(e)
pi = math.pi    # boa pratica passar o valor para uma variavel para nao ficar acessando o modulo sempre
print(pi)

# comum importar apenas um simbolo, ou seja apenas uma determinada função dentra do madulo(classe)

# from (nome do madulo) import (funcao)

from math import pi

print(pi)

from  math import sqrt

print(sqrt(49))

# from modulo import * // importa todos os simbolos de um modulo  evitar esta situação

import mod_import
#print(mod_import.soma(10,15))
d = mod_import.soma(10,10)
print(d)


# nomes precedidos com _ (unterline) é apenas local não é importado na importação do modulo


