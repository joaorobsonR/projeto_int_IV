cont = 0
while cont < 10:
    cont += 1
    print(cont)

def testinhoFor(x, y):
    cont = 0
    for i in range(x, y):
        i += 1
        print(i)
        cont = (x + y) * y
    
    return cont

resultado = testinhoFor(0, 10)
print(resultado)
