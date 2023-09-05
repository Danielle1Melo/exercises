valor = int(input("Digite um valor: "))
fat = 1
aux = 2
while aux <=valor:
    fat = fat * aux
    aux = aux + 1
print(f"Fatorial: {fat}")