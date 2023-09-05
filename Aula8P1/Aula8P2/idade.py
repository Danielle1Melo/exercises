import random

idade = []
for i in range(0,20):
    idade.append(random.randint(1,100))
print(f"Idades: {idade}")

#media 
media = sum(idade)/len(idade)
print(f"Média de idades: {media:3f}")
print(f"Maior idade: {max(idade)}")
print(f"Menor idade: {min(idade)}")