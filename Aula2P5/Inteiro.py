
valor = int(input("Digite um n° inteiro com 4 dígitos: "))
milhar = valor//1000
resto = valor%1000
centena = resto//100
resto = resto%100
dezena = resto//10
unidade= resto%10
print("Valor invertido", unidade*1000 + dezena*100 + centena*10 + milhar)