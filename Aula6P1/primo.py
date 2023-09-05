valor = int(input("Informe um valor: "))
d = 1
cont = 0
while d<=valor:
    if valor % d == 0: cont = cont +1
    d = d + 1
if cont == 2: print(f"{valor} é primo")
else: print(f"{valor} não é primo")

