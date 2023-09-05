cont = 0 
somaSalario = 0
maiorIdade = 0
menorIdade = 120
quantMulher = 0

while True:
    print("Para encerrar o programa informe uma idade negativa")
    idade = int(input("Informe a idade: "))
    if idade< 0:
        print("Fim do programa")
        break

    while idade <= 0 or idade >= 120: 
        print("Fim do programa")
        idade = int(input("Informe a idade: "))
    
    sexo = int(input("Informe o sexo: 1.masculino / 2.feminino: "))
    while sexo!= 1 and sexo!=2:
        print("Informação inválida")
        sexo = int(input("Informe o sexo: 1.masculino / 2.feminino: "))
    
    salario = float(input("Informe o salário: "))
    while salario<0:
        print("Informação inválida")
        salario = float(input("Informe o salário: "))
    somaSalario = somaSalario + salario
    cont = cont + 1 

#Media salario
mediaSalario = somaSalario / cont

#idade mais velho
if idade > maiorIdade: maiorIdade = idade
if idade < menorIdade: menorIdade = idade

#quant mulheres
if sexo == 2 and salario <= 3500: quantMulher = quantMulher + 1

if cont == 0: print("Dados não informados")
else:
    print(f"Media de salario do grupo: {mediaSalario}")
    print(f"Maior idade: {maiorIdade} Menor idade: {menorIdade}")
    print(f"Quantidade de mulheres com salário ate 3500: {quantMulher}")



   