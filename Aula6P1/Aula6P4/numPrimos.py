quant = int(input("Informe a quantidades de num primos: "))

while quant <= 0:
    print("valor inválido") 
    quant = int(input("Informe a quantidades de num primos: "))

num = 2
contPrimo = 1
while contPrimo <= quant:
    contaDivisores = 0
    d = 1
    while d<=num:
        if num % d == 0 : contaDivisores = contaDivisores +1
        d = d + 1
    if contaDivisores == 2: 
        print(num)
        contPrimo = contPrimo + 1
    num = num + 1
