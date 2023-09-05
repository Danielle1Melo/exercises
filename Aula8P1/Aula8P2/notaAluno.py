import random

notas = []
for i in range (0, 15):
    notas.append(random.randint(1, 100)/10)
print(f"Notas: {notas}")
media = sum(notas)/len(notas)
print(f"Media: {media}")

AcimaMedia = 0
abaixoMedia = 0
for num in notas:
    if num > 6: AcimaMedia = AcimaMedia + 1
    if num < 6: abaixoMedia = abaixoMedia + 1

print(f"Acima de média: {AcimaMedia}")
print(f"Na média: {notas.count(media)}")
print(f"Abaixo da média: {abaixoMedia}")
print(f"Maior nota: {max(notas)}")
print(f"Menor nota: {min(notas)}")