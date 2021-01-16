"""
a = 10
if (a==11):
    print("a é igual a 10")
else:
    print("a nao é igual")

acao = int (input ("insira numero 1 para sim e numero 2 para nao"))

if acao == 1:
    print ("valor selecionado foi 1")

elif acao == 2:
    print("valor selecionado foi 2")
else:
    print("opcao invalida")


idade = int (input("informe a sua idade"))

if (idade <= 0):
    print("informe uma idade valida maior que zero")
elif (idade >= 150):
    print("idade maior que 150 invalido")
else:
    print("sua idade é ", (idade))



n1 = input("informe o primeiro numero")
n1 = int(n1)
n2 = input("informe o segundo numero")
n2 = int(n2)
n3 = input("informe o terceiro numero")
n3 = int(n3)

if(n1==n2 and n1==n3):
    print("segunda opção")
elif(n1 <= n2 or n1 >= n3):
        print("primeira opçao")

        # and  (&&)
        # or   (||)
        #not (inverte)
        # is (do mesmo tipo)
        # is not (nao é do mesmo tipo)
        # in (esta contido)
        #not in (não esta contido)

"""