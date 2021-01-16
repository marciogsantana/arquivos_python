"""
1- lista de dados apenas de um determinado tipo ou varios tipos
2- pilha ultimo a entrar primeiro sair
3- fila primeiro a entrar primeiro a sair
4- tupla é uma lista somente leitura, não pode remover, adicionar, alterar
5- set conjunto não aceita itens com mesmo valor (itens repetidos) ex: 2,2
6- dicionario  como uma lista porem temos que informar uma chave e um valor não aceita chaves repetidas
7- arvore  raiz- no- filho



# declarar lista tipo 1

tata = [1,2,8,9,8,10]
print(tata)
print(tata[1] + tata[5])
tete = ["marcio",1,"t",12.45]
print(tete)
print(tete[3])
t =["m","a","r","c","i","o"]
print(t[0]+t[1]+t[2]+t[3]+t[4]+t[5])

# outra maneira de declarar lista

li = list("marcio")
print(li)

li2 = list(("santana","gomes"))
print(li2)

li1 = list((1110,1.5,2,))
print(li1)

a = (5,)
print(type(a))



# lista dentro de lista // muito doido este python

lista = [["a","b","c"],[1,2,3],[12.45,1.5,"c"]]
print(lista)
print(lista[2])
print(lista[0][1])
print(lista[1][1])
print(lista.__len__())
print(len(lista))



# metodos lista

lista = [1,2,3,4,5]
print(lista)
lista = [0] + lista  # adicionar inicio
print(lista)
lista = lista + [6,7,8,9,10]  #adicionar final
print(lista)
lista.append(11)              #adicionar usando metodo
print(lista)
del(lista[0])                 # remover elementos
print(lista)
del(lista[2])
print(lista)
del(lista[9])
print(lista)
print(50*"-")                 #muito doido
print(10*[0])



# iterando lista

lista = [1,100,200,50,30,40]
for i in lista:
    c = i
    c = c + 1000
    print(c)

lista1 = [1, 100, 200, 50, 30, 40,50,800]  # função len para iterar uma lista
for d in range(len(lista1)):
    lista1[d] += 1000
print(lista1)




# fatiando lista

lista = list("marcio")
print(lista)
lista1 = lista[::-1]
print(lista1)
lista2 = lista[1:3:1]     # 1 primeiro elemento 3 ultimo elemento 1 intervalo
print(lista2)




# incluindo,alterando,excluindo elementos da lista

l = ["aa","bb","cc"]
print(l)
l.append("dd")
print(l)
l.insert(0,"tt")          # metodo insert informe o indice depois o elemento
print(l)
l.insert(1,"ooo")
print(l)
l[1] = "vvvvvv"          # alterar elemento dentro da lista
print(l)
l.clear()                 # apaga toda lista
print(l)
l = ["aa","bb","cc"]
print(l)
del l[2]
print(l)
l.pop(1)                  #pagar elemento
print(l)
l = ["aa","bb","cc","dd","ee","ff"]
print(l)
del(l[1:4])                # apagar um intervalo de elementos 1 elemento inicio 4 elemento final
print(l)



l = [1,50,100,2,3,6,1001,58,6]
print(l)
l.sort()                       # metodo para ordenar lista
print(l)
L1 =["A","B","Z","U","C"]
print(L1)
L1.sort()
print(L1)
l2 =["marcio","antonio","marcelo","laura","luiza"]
print(l2)
l2.sort()
print(l2)
l2.sort(reverse=True)
print(l2)
print(l2)
l2.insert(2,"marcelo")
print(l2)
l2.append("marcelo")
print(l2)
print(l2.count("marcelo"))        # quantos vezes o elemento esta na lista
print(l2.index("marcelo"))        # retorna o indice do elemento



# tuplas (lista imutavel, lista heterogenia)

# primeira forma de definir tupla

t = tuple("abc")
t1 = tuple((1,2,3))
print(t)
print(t1)

# segunda forme de definir tupla

x = "ttt",12,12.5, True
print(x)
print(type(x))
y = ("tyty",12.45,25)
print(y)
print(type(y))

# in localizar um valor dentro de uma lista

print(25 in (y))
print(26 in (y))
print(25 not in (y))
print(26 not in (y))
print(25 in [0,25,100,2])

# operadores and or e in

l = [12,0,45,6,89,3,5,16,]
print(12 and 100 in (l))
print((450 or 100) in (l))

"""






