
try:
     num1 = float( input("informe o primeiro numero"))
     num2 = float( input("informe o segundo numero"))
     print(num1/num2)

except ValueError:

       print("valor informado errado")

print("marcio") # executa os blocos de codigos do except e quando termina continua executando o programa


# excessoes multiplas

print(eval("10+10"))   # funcao eval executa comandos python

def erro(x):

    eval(x)
    # type erro

try:
    erro("a")

except TypeError:

    print("nao é possivel somar duas instacias")
except NameError:
    print("nome invalido")


