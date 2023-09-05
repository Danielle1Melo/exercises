valor = int(input("Informe um valor: "))
d = 1
while d<=valor:
    if valor % d == 0: print(f"{d} divide {valor}")
    d = d + 1