"""

# exercicio 1 lista iteração

for i in range(1,101,1):
    print(i)

# exercicio 2

y = input("informe o intervalo para a lista de 0 a 100")
y =  int(y)
for i in range(1,101,y):
    print(i)


# exercicio 3

for i in range(10,0,-1):
    print(i)



#exercicio 4

for i in range(101):
    if (i%2 == 0):
       print(i)




#exercicio 5

soma = 0
for i in range(101):
    if (i%2 == 0):
       soma = soma + i
print(soma)


# exercicio 6

for i in range(101):
    if (i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0 and i%9 !=0 or i == 3 or i == 5 or i == 7):
       print(i)



# exercicio 7

r = input("informe o numero")
r = int (r)

for i in range(r):
    if (i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0 and i%9 !=0 or i == 3 or i == 5 or i == 7):
       print(i)



# exercicio 8

i = input("informe o primeiro numero")
i = int (i)
f = input("informe o ultimo numero")
f = int(f)
es = input("informe o intervalo entre os numeros")
es = int (es)

primeiro = input("informe o primeiro numero para exclusao")
primeiro = int (primeiro)
segundo = input("informe o segundo numero para exclusao")
segundo = int(segundo)
terceiro = input("informe o terceiro numero para exclusao")
terceiro = int(terceiro)

for s in range(i,f,es):
    if (s == primeiro or s == segundo or s == terceiro):
        continue

    else:
        print(s)


"""

# exercicio 9

p = 0
while(p == 0):
    print("estou em looping")
    t = input("informe uma letra para parar o loping")
    if (t == "q"):
        p = 1
        print("muito bem voce saiu do lopping")