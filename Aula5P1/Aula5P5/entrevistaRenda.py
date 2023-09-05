
import random

somaRenda = 0
SomaIdade = 0
qtdMais3Filhos = 0
qtdHomensMenor30 = 0
SomaFilhos = 0
rendaMaisVelho = 0
idadeHomenMaisVelho = 0
idadeMaiorRendaMulher = 0
MulhermaiorRenda =0

habitantes = 2000

for cont in range(2000):
    idade = random.randint(18,50)
    renda = random.randint(1200, 12000)
    genero = random.choices(["m", "f"])
    filhos = random.randint(0,5)

    #Media renda
    somaRenda += renda
    #Media de idade com +3 fihos
    if filhos > 3:
        SomaIdade += idade
        qtdMais3Filhos += 1
    #Quantidade de hom com menos de 30
    if genero == "m" and idade<30:
        qtdHomensMenor30 +=1

    #Media no num de filhos
    SomaFilhos += filhos

    #renda do homem mais velho
    if genero == "m" and idade > idadeHomenMaisVelho:
        idadeHomenMaisVelho = idade
        rendaMaisVelho = renda

    #Idade da mulher com maior renda
    if genero == "f" and renda> MulhermaiorRenda:
        idadeMaiorRendaMulher = idade
        MulhermaiorRenda = renda

    #resultados
mediaRenda = somaRenda / habitantes
mediaMais3Filhos = SomaIdade // qtdMais3Filhos
mediaFilhos = SomaFilhos //habitantes
print(f"Media de renda: {mediaRenda}")

print(f"Media de idade com mais de 3 filhos: {mediaMais3Filhos}")
print(f"Total de homens com menos de 30 anos: {qtdHomensMenor30}")
print(f"Media do num de filhos: {mediaFilhos}")
print(f"Renda do homen mais velho: {rendaMaisVelho}")
print(f"Idade da mulher com maior renda: {idadeMaiorRendaMulher}")

