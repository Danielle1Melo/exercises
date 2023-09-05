# matriz randomica

import random

matriz = []
for linha in range(0,3):
    linha = []
    for coluna in range(0,3):
        linha.append(random.randint(0,10))
    matriz.append(linha)
print(matriz)
