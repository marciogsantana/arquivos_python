#1
def estudo():
    print("estamos estudando as funções")
estudo()

#2

def estudo(x):

    print("funcao invocada com sucesso",x )
estudo(15)

#3

def soma(x,y):
    z = x+y
    print(z)
soma(50,50)

def medio(x,y,z):
    print(x)
    print(y)
    print(z)
    media = (x+y+z)/3
    print(media)
medio(5,15,25)

# 5

def login(usuario = "master",senha="12345"):
    usuario = usuario
    senha = senha
    print(usuario)
    print(senha)
login("marcio")

#6

def func1():
    def func2(x,y):
        resultado = x + y
        print("soma dos dois numeros é",resultado)
        return resultado
    return (func2(5,5))

print(func1())

#7

def lista1(*lista):
    print(lista)
lista1(1,2,3,4,5,"tata")

#8

def lista2(**lis):
    print(lis)
    print(lis.keys())
    print(lis.values())

lista2(a=1, b=2, c=3)

#9

l = [5,5,5,5]
def tata (a,b,c,d):
    s = a+b+c+d
    print(s)
tata(*l)

#10

def func_maior(a,b,c):
    maior = a
    if(b > maior):
        maior = b
        if(c > maior):
            maior = c
            return maior
        else:
            return maior
    elif(c > maior):
        maior = c

        return (maior)
    else:
        return maior

print(func_maior(24,12,9))

# 11

lista12 = [1,2,3,4,5]

def soma12(a,b,c,d,e):
    soma = a+b+c+d+e
    print(soma)
soma12(*lista12)

#12

def mul12(a,b,c,d,e):
    mul = a*b*c*d*e
    print(mul)
mul12(*lista12)

#13

lista13 = [1,2,3,4,"a","b","c","d"]

def func13(a,b,c,d,e,f,g,h):
    print(h)
    print(g)
    print(f)
    print(e)
    print(d)
    print(c)
    print(b)
    print(a)
func13(*lista13)

# 14

def fatorial(a):
    if (a == 0 or a == 1):
        return 1
    else:
        return a *  fatorial(a -1)

print(fatorial(4))

#15

lista15 = [1,2,3,4,5,6,7,8,9,10]


def func15(*a):
    numero = a
    if (numero == 6):
        print("numero encontrado foi",numero)
    else:
        print("numero nao encontrado")
func15(*lista15)
