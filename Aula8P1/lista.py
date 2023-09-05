import random

lista = []
for i in range (0,30):
    lista.append(random.randint(1,500))
print(lista)

maior = lista [0]
pares = 0
for num in lista:
   if num>maior: maior = num
   if num%2==0: pares = pares +1

print(f"Maior: {maior}")
print(f"Pares: {pares}")