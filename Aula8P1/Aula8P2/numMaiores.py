import random

lista = []
for i in range(0,30):
    lista.append(random.randint(1,31))

lista.sort()
lista.reverse()
print(lista)
indice = 0
listMaiores = []
while (indice<10):
    listMaiores.append(lista[indice])
    indice = indice + 1
print(listMaiores)