'''idade = int(input("Digite sua idade: "))
if idade >=18:
    print("Voçê é maior de idade")
else :
    print("Voçê é menor de idade")

--------------------------------------------------------

altura = float(input("Digite sua altura: "))
gene = int(input("1. Feminino 2.Masculino"))

if gene == 1: 
    pesoIdeal = 62.1 * altura - 44.7

if gene == 2 : 
    pesoIdeal = 72.7 * altura - 58

if gene!=1 and gene!=2 : 
    print("Invalido")
    pesoIdeal=0

print("Seu peso ideal é: ", pesoIdeal)    

---------------------------------------------------

hrInicial = int(input("Informe a hora inicial do jogo: "))
mtInicial = int(input("Informe o minuto inicial do jogo: "))

hrFinal = int(input("Informe a hora final do jogo: "))
mtFinal = int(input("Informe o minuto final do jogo: "))

horarioInicial = hrInicial * 60 + mtInicial
horarioFinal = hrFinal * 60 + mtFinal

if horarioInicial < horarioFinal: 
    duracao = horarioFinal - horarioInicial
else: duracao = 24*60 - horarioInicial + horarioFinal

print("Horas: ", duracao//60)
print("Minutos", duracao%60) 

-------------------------------------------------------
'''

num = int(input("Informe um número com 4 dígitos: "))

if num >= 1111 and num<=9999:
    milhar = num//1000
    resto = num%1000
    centena = resto//100
    resto = resto%100
    dezena = resto//10
    unidade = resto%10
    verificar = unidade*1000 + dezena*100 + centena*10 + milhar
    if num == verificar:
        print("Seu número é capicua")
    else: 
        print("Seu número não é capicua")

else :
    print("Número inválido, digite 4 dígitos: ")