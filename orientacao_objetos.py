"""

class Pessoa:
    pass

p1 = Pessoa()   # instanciando a classe ou seja criando objetos
p2 = Pessoa()

print(id(p1))  # ids diferentes
print(id(p2))

# exemplo de implementação de classe.

class Retangulo():
    def __init__(self):   # construtor
        self.a = 0        # atributos
        self.l = 0        # atributos
    def area(self):       # metodos
        return self.a * self.l


r1 = Retangulo()
r2 = Retangulo()

r1.a = 10
r1.l = 10
print(r1.area())

class Ret():                     # construtor utizando parametro
    def __init__(self, x, y):
        self.a = x
        self.l = y
    def ar(self):
        return self.a * self.l

r = Ret(7,5)
print(r.ar())



#FUNCAO isinstance  VERIFICA SE UM OBJETO É DO TIPO INTEIRO EX:

if ((isinstance(4,int))):
    print("é um numero inteiro")
else:
    print("não é um numero inteiro")



class retangulo:
    def __init__(self, largura, altura ):
        self.__largura = 0                # _ (UNDERLINE NA FRENTE DO ATRIBUTO DEFINE ELA COMO PRIVADA
        self.__altura = 0                 # __ (DOIS UNDERLINE EVITA COLISAO DE NOMES OU SEJA EVITA DO ARTIBUTO SER ACESSADO A FORÇA
        self.set_altura(altura)
        self.set_largura(largura)
    def set_altura(self, num):
        if (not (isinstance(num,int) and (num > 0))):
            raise ValueError("altura é invalida: {}".format(num))  # metodo set e get deve ser precedido com _ (underline)
        self._altura = num
    def set_largura(self, num):
         if (not (isinstance(num, int) and (num > 0))):
            raise ValueError("altura é invalida: {}".format(num))
         self._largura = num
    def get_altura(self):
        return self._altura
    def get_largura(self):
        return self._largura
    def get_area(self):
        return self._largura * self._altura
    altura = property(fget=get_altura, fset=set_altura)  # propriedade var para simplificar o codigo
    largura = property(fget= get_largura, fset=get_largura)
t = retangulo(5,50)
print(t.get_largura())
t.set_largura(100)
t.set_altura(1000)
print(t.get_largura())
print(t.get_altura())
t.__largura = 1500
print(t.get_largura())
print(t.__largura)



# funcao decorators



# metodo de classe metodo no scopo da classe bem semelhante ao metodos privados java ,
# ou seja sera executado sendo que o objeto for criado

# parametro obrigatorio cls

class Bichos:
    quant_bichos = 0
    def __init__(self):    # construtor
        self.ad_bicho()    # chama metodo para adicionar bichos
    def __del__(self):
        self.del_bicho()   # chama metodo para deletar bichos
        if(self.quant_bichos == 0):
            print("todos os bichos mortos")

    @classmethod           # outra maneira de declarar metodo estatico mais elegante e facil inclusive
    def ad_bicho(cls):     # parametro metodo da classe == estatico
        cls.quant_bichos += 1
    @classmethod
    def del_bicho(cls):
        cls.quant_bichos -= 1

    # ad_bicho = classmethod(ad_bicho)     # informar ao python que o metodo ad_bicho recebe um metodo de classe
    # del_bicho = classmethod(del_bicho)   # informar ao python que o metodo del_bicho recebe um metodo de classe

    def get_quantidade(self):
        return self.quant_bichos

b1 = Bichos()
b2 = Bichos()
b3 = Bichos()

print(b3.get_quantidade())

del b1
del b2
del b3
print(Bichos.quant_bichos)


"""

# metodo estatico podemos acessar o metodo a qualquer momento semelhante a função no java ou seja apenas um metodo

class Metodoestatico:
      def func1():
          print("imprimindo função")
      func1 = staticmethod(func1)

      def func2(x,y):
          print("funcao '{}' invocada. \nparametros= ({},{})".format("func2",x,y))

me = Metodoestatico()     # pode invocar o metodo atraves de uma instancia
me.func1()
Metodoestatico.func1()    # pode invocar o metodo atraves da classe  esta maneira é mais interressante


mi = Metodoestatico           # pode receber parametros
mi.func2(10,20)
Metodoestatico.func2(10,20)