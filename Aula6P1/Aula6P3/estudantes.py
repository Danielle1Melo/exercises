cont = 0 
somaIdade = 0
somaAlt = 0
meninas = 0
mais20 = 0
maiorIdade = 0
maiorAltura = 0

while True:
    print("Para encerrar, informe uma idade negativa")
    idade = int(input("Informe a idade: "))
    if idade < 0: 
        print("Fim de programa")
        break
    alt = int(input("Informe a altura: "))
    genero = int(input("1.Feminino 2.Masculino"))
    somaIdade = somaIdade + idade
    
    cont = cont + 1

    if idade<=0 or alt <=0 or genero<=0:
        print("Informações inválidas") 

#media
mediaIdade = somaIdade / cont 
print(f"Média de idade dos estudantes: {mediaIdade}")

while genero == 1:
   somaAlt = somaAlt + alt
   meninas = meninas + 1 
   mediaAltura = somaAlt / meninas
   
   if meninas == 0 : print("Não tem meninas")
   else: print(f"Média de altura das meninas: {mediaAltura}")

if idade > 20: 
    mais20 = mais20 + 1
    somaMais20 = mais20 * 100/cont
    print(f"Percentual de alunos com mais de 20 anos: {somaMais20} ")
 
if idade > maiorIdade :
    maiorIdade = idade
    maiorAltura = alt
    print(f"Altura do mais velho: {maiorAltura}")
    print(f"idade do mais velho: {maiorIdade}")

if cont == 0:
    print("Dados não informados")
