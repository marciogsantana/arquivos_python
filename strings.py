# aspas simples e duplas
# """ ou ''' declarar texto

#
 #   si = """
 #        mamamamamama
 #        bnbbnbnbnbnbn
 #        uiuiuiuuiuiui7
 #        opopooppopoooh
 #        hjhjhjhjhjhhj
 #        hjkkkkklklkklkk
 #         """
          
 # print(si)

"""          
          
si2 = '''
         mamamamamama
         bnbbnbnbnbnbn
         uiuiuiuuiuiui7
         opopooppopooo
         '''
print(si2)
         
"""

# fatiando strings

lista = "marcio gomes santana"
print(lista)
listaf = lista[13::1]
print(listaf)

#iterando

for c in lista:
    print(c)

listai = lista[::-1]
print(listai)

# comparando strings compara usando tabela ascII

a = "y"
b = "a"

if a==b:
    print("iguais")
else:
    print("não sao iguais")


print(ord(a))      # funcao ord retorna codigo asc


s = "lista de caracteres"
print(len(s))
si = s[6]
print(si)
print(s.count("e"))   # listas quantas vezes um elemento esta na lista