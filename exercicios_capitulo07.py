# exercicio1

print("marcio")

#exercicio2

nome = input("insira seu nome:")
print("seu nome é " + nome)

#exercicio3

nome = input("informe o nome")
idade = int (input("informe a idade:"))
print("seu nome é " + nome + "  " +  "sua idade é "  + str(idade))

#exercicio4

numero = int (input("informe o numero"))
numero = numero * 10
print("o numero informado é " , (numero))

#exercicio 5

numero = int (input("informe o numero"))
print("o numero é %i" %numero)

#exercicio 6

nu1 = float(input("informe o numero 1"))
nu2 = float(input("informe o numero 2"))
nu3 = float(input("informe o numero 3"))
soma = nu1+nu2+nu3
print("a soma é" , (soma))

#exercicio7

nu1 = float(input("informe o numero 1"))
nu2 = float(input("informe o numero 2"))
soma = nu1+nu2
print("a soma do numero" + str(nu1) + " + " + "o numero" +str(nu2) + "e iguaal a " + str(soma))

# exercicio8

nota1 = float(input("informe a nota 1"))
nota2 = float(input("informe a nota 2"))
nota3 = float(input("informe a nota 3"))
nota4 = float(input("informe a nota 4"))
media = (nota1+nota2+nota3+nota4)/4
print("a media é " , (media))

#exericio 9

m = float(input("informe em metros"))
c = m*100
print("o total em cm é " , (c))

#exercicio 10

n1 = int(input("informe o numero"))
q = n1**2
c = n1**3
print("o quadrado do numero" + str(n1) + "e" + str(q) + "e o cubo é" + str(c))

#exercicio 11

nu1 = float(input("informe o numero 1"))
nu2 = float(input("informe o numero 2"))
soma = nu1/nu2
print("o resultado é" , (soma))
print("o resultado é" , int(soma))

#exercicio12

l = int(input("informe a altura"))
a = int(input("informe a largura"))
per = l*a
print("a area é ", (per))

#exercicio 13

dia = int(input("informe quantos dias"))
horas = int(input("informe quantas horas"))
minutos = int(input("informe quantos minutos"))
tdia = (dia*24)*3600
th = horas * 3600
ts = minutos * 60
totals = tdia+th+ts
print("o total em segundos é " , (totals))

#exercicio14

valor = float(input("informe o valor da compra"))
desconto = valor * 0.1
print("o valor total da compra é " + str(valor) + "o valor do desconto e" + str(desconto))
