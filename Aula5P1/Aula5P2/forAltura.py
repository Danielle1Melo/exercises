import random
''' 
soma = 0 
maior = 0
for cont in range(10):
    #Gera um num float entre 1.5 e 2.1
    alt = random.uniform(1.5, 2.10) 
    soma = soma + alt
    if alt > maior:
        maior = alt

media = soma/10
print(f"Média: {media:.3f}")
print(f"Maior altura: {maior}")

---------------------------
'''

somaIdade = 0
cursoMaisVelho = ""
idadeMaisVelho = 0
qtdAlunas5 = 0

for cont in range (50):
    #Sorteio
    idade = random.randint(18, 60)
    curso = random.choice(["Eng.Civil", "Eng. Mec", "Eng.Química", "Eng. Produção"])
    semestre = random.randint(1,10)
    #Media de idades
    somaIdade += idade
    #curso do mais velho
    if idade > idadeMaisVelho:
        idadeMaisVelho = idade
        cursoMaisVelho = curso
    #Total de alunos 5 semestre
    if semestre == 5:
        qtdAlunas5 +=1

    mediaIdade = somaIdade//50
    print(f"Media de idades: {mediaIdade}")
    print(f"Media aluno mais velho: ({idadeMaisVelho} anos) : {cursoMaisVelho}")
    print(f"Total de alunos 5 semestre: {qtdAlunas5}")