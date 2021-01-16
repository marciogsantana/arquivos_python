"""
# numeros pares/impares ou zero

numero = input("informe um numero")
numero = int(numero)

if (numero <0):
    print("informe um valor maior igual a zero")
elif(numero == 0):
    print("o valor informado é zero")
else:
    numero2 = numero%2
    if(numero2 == 0):
        print("o numero é par")
    else:
        print("o numero é impar")


numero = input("informe um numero")
numero = int (numero)
if (numero < 0):
    print("o numero é negativo")
elif (numero == 0):
    print("o numero é zero")
else:
    print("o numero é positivo")



# maior numero

numero1 = input("insira o primeiro numero")
numero1 = int(numero1)
numero2 = input("insira o segundo numero")
numero2 = int(numero2)
if (numero1 > numero2):
    print("o maior numero é ",(numero1))
elif(numero1 < numero2):
    print("o maior numero é ",(numero2))
else:
    print("os numeros sao iguais")



#idade

idade = input("informe a idade")
idade = int(idade)
if (idade <=0 or idade >=120):
    print("informe uma idade valida")
elif(idade >= 18):
    print("maior de idade")
else:
    print("menor de idade")



# idade mae

idadem = input("informe a idade da mae")
idadem = int(idadem)
idadef = input("informe a idade do filho")
idadef = int (idadef)
total = idadem - idadef
print("idade da mae é " + str (idadem) + " " + "a idade do filho e" + " "+ str (idadef) + " " + "ano" + " " + str (total))



i = 10
a =  10
if(type(i) == type(a)):
    print(" e inteiro")
else:
    print("e falso")

j = "j"
l = "1"
if(type(j) == type(l)):
    print(" e string")
else:
    print("e falso")

j1 = 12.5
l1 = 20.555
if(type(j1) == type(l1)):
    print(" e double")
else:
    print("e falso")

# maior

numero1 = input("informe o primeiro numero")
numero1 = int(numero1)
numero2 = input("informe o segundo numero")
numero2 = int(numero2)
numero3 = input("informe o terceiro numero")
numero3 = int(numero3)

if (numero1 > numero2 and numero1 > numero3):
    print("o maior numero é ", (numero1))
elif(numero2 > numero1 and numero2 > numero3):
    print("o maior numero é ", (numero2))
elif (numero3 > numero1 and numero3 > numero1):
    print("o maior numero é ", (numero3))
else:
    print("os numeros sao iguais")

#ordem crescente

numero1 = input("informe o primeiro numero")
numero1 = int(numero1)
numero2 = input("informe o segundo numero")
numero2 = int(numero2)
numero3 = input("informe o terceiro numero")
numero3 = int(numero3)

if (numero1 >= numero2 and numero1 >= numero3 and numero2 >= numero3):
    maior = numero1
    medio = numero2
    menor = numero3
    print(menor)
    print(medio)
    print(maior)
elif(numero2 >= numero1 and numero2 >= numero3 and numero1 >= numero3):
    maior = numero2
    medio = numero1
    menor = numero3
    print(menor)
    print(medio)
    print(maior)

elif (numero3 >= numero1 and numero3 >= numero2 and numero2 >= numero1):
    maior = numero3
    medio = numero2
    menor = numero1
    print(menor)
    print(medio)
    print(maior)
elif (numero3 >= numero1 and numero3 >= numero2 and numero2 <= numero1):
    maior = numero3
    medio = numero1
    menor = numero2
    print(menor)
    print(medio)
    print(maior)

else:
    print("os numeros sao iguais")



#vogal

v = "s"
if(v == "a" or v == "e" or v == "i" or v == "o" or v == "u"):
    print("vogal")
else:
    print("consoante")



#mes

mes = input("informe o mes")
mes = int(mes)
if (mes <0 or mes >12):
    print("informe uma data valida")
else:
    if(mes == 1):
        print("janeiro")
    elif(mes == 2):
        print("fevereiro")
    elif (mes == 3):
        print("marco")
    elif (mes == 4):
        print("abril")
    elif (mes == 5):
        print("maio")
    elif (mes == 6):
        print("junho")
    elif (mes == 7):
        print("julho")
    elif (mes == 8):
        print("agosto")
    elif (mes == 9):
        print("setembro")
    elif (mes == 10):
        print("outubro")
    elif (mes == 11):
        print("novembro")
    elif (mes == 12):
        print("dezembro")



#validar data

dia = input("informe o dia")
dia = int(dia)
mes = input("infrme o mes")
mes = int(mes)
ano = input("informe o ano")
ano = int(ano)

if(dia <= 0 or dia >31 or mes <=0 or mes >12 or ano <= 0):
    print("data invalida")
else:
    print(str(dia)+"/"+str(mes)+"/"+str(ano))


"""

a = 10
b = 20
a,b = b,a
print (a)
print (b)
a,b = b,a
print(a)
print(b)

x,y,z = 100,200,300
print(x)
print(y)
print(z)

nome,sobrenome = "marcio","santana"
print(nome)
print(sobrenome)

# atribuicao condicional

x = 10
texto = ("sim") if x==10 else("nao")
print(texto)

x = 11
texto = ("sim") if x==10 else("nao")
print(texto)
