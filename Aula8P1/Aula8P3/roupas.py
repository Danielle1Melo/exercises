
pecas = []
for i in range (0,5):
    tamanho = input("Informe o tamanho P M G: ")
    while (tamanho != "p" and tamanho != "m" and tamanho != "g"):
        tamanho = input("Informe o tamanho P M G: ")
    opcao = int(input("Informe a cor: 1.Branco 2.Preto 3.Azul: "))
    while (opcao<1 or opcao>3):
         opcao = int(input("Informe a cor: 1.Branco 2.Preto 3.Azul"))

    if opcao == 1: tupla = (tamanho, "branco")
    else:
        if opcao == 2: tupla = (tamanho, "preto")
        else: tupla = (tamanho, "azul")
    pecas.append(tupla)
print(pecas)

contP = 0
contM = 0
contG = 0
cores = []
for item in pecas:
    if item[0] == 'p': contP = contP + 1
    else:
         if item[0] == 'm': contM = contM + 1
         else:  
           contG = contG + 1
    cores.append(item[1])

totalTamanho = []
totalTamanho.append((f"Pequeno: {contP}"))
totalTamanho.append((f"Médio: {contM}"))
totalTamanho.append((f"Grande: {contG}"))
print(totalTamanho)
maior = 0
tamanho = ""
for item in totalTamanho:
    if item[1] > maior:  
        maior = item[1]
        tamanho = item[0]
print(f"Mais vendido: {tamanho, maior} peças")
print(f"Quantidade de M vendido: {totalTamanho[contM]}")
print("Peças brancas vendidas: ", cores.count("branco"))
print("Peças pretas vendidas: ", cores.count("preto"))
print("Peças azuis vendidas: ", cores.count("azul"))