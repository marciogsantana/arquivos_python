"""
print()

def primeira(x, y):

    z = x*y
    print("o resultado da multiplicacao é",z)

primeira(25,5)

def segunda():
    print("fala marcio o vencedor")

segunda()

primeira(10,10)



def login (usuario ="marcio", senha = "123456"):      # funcao com paramentros defull
    print("usuario:",senha)
    print("senha:",usuario)

login()
login("santana","tututu")

def multi (x = 10, y = 10):
    z = x*y
    print(z)
multi()
multi(15,15)



# retorno de função

def soma(x, y):
    z = x * y
    return z

h = soma(10,10)* 100
print(h)



# retorno de valores multiplos

def mul(x,y):
    z = x * y
    k = x/y
    return z,k
print(mul(20,10))

t = mul(20,10)
print(t[0])
print(t[1])
p = (t[0] + t[1]) * 10
print(p)

a, b = mul(500,150)
print(a)
print(b)




# funcao variadica pode receber 0 ou varios parametros

def lista_arguments(*lista):   # * defini a lista defull
    print(lista)
lista_arguments(1,5,15,"tata",25.45)

def lista_argumento_dicionario(**lista1):
    print(lista1)

lista_argumento_dicionario(a=1, b=2, c=3, d=4)   # ** estrutura dicionario




# desempacotamento

lista = ["marcio","santana","diretor"]

def emp(nome,sobrenome,funcao):
    print(nome)
    print(sobrenome)
    print(funcao)

emp(*lista)


tata = [13,12,11]

def t (a,b,c):
    print(a)
    print(b)
    print(c)

tata.sort()
t(*tata)




 funcoes aninhadas funcao dentro dentro de funcao

def func():
    print("func")

    def func_interna():
        print("func_interna")

    func_interna()
func()



# função nonlocal

def func():
    va_local = 10
    def func_interna():
        nonlocal va_local
        va_local += 10
        print(va_local)
    func_interna()

func()

# observação posso informar global para falar que estou acessando uma variavel global



# blocos vazios

def func():
    pass

"""

 # instrução global

num1 = 10
print(num1)
def func():
    # num = 20
    global num1  # para alterar o valor de uma variavel global de dentro de um modulo
    num1 = 50
    print(num1)
func()
print(num1)

