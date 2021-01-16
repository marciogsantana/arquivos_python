"""
x = 10
while(x >= 0):
    print(x)
    x -= 1



for c in "marcio":
    print(c)

for i in (0,1,2,3,4,5):
    print(i)


print(list (range(0,10,2)))    # 0 inicio 10 final 2 intervalo
print(list(range(10)))

y = 0

list (range(0,10,1))
y += 1
print(y)
for i in (0,1,2,3,4,5):
    y += 1
    print(y)



print(list(range(100,0,-3)))

z = 0

for i in range(10):
    z += 1
    print(z)

for i in range(-10,0,1):
    print(i)

"""
# break para o laço
print("antes de entrar no laço")

for item in range(10):
    print(item)
    if (item == 6):
        break
print("depois do laço")


# continue  para umm laço  e vai para outro

print("antes do laço continue")
for i in range(20):
    print(i)
    if i == 11:
        print("o valor encontrado foi",(i))
        continue
        for i in range(10):
            print(i)
print("encerrando segundo laço")