arq = open("alturas.txt", "w")

cont = 1
while cont <=5:
    nome = input("Informe o nome: ") 
    altura = float(input("Informe a altura: "))
    arq.write(nome + ' - ' + str(altura) + "\n")
    cont = cont + 1
arq.close()

lista = []
soma = 0
nomeAlto = ""
alturaAlto = 0
arq = open("alturas.txt", "r")
for linha in arq:
    saida = linha[:-1].split('-')#-1 tirando o \n
    altura=float(saida[1])
    nome = saida[0]
    dados = (nome, altura) #tupla
    soma = soma + altura

    if altura > alturaAlto:
        alturaAlto = altura
        nomeAlto = nome
    lista.append(dados)
arq.close()
print(lista)
print(f"Media: {soma/len(lista)}")
print(f"Nome do mais alto: {nomeAlto}")