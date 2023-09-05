quant = int(input("Informe a quant de valores pares:"))
while quant <=0: 
    print("Valor deve ser positivo")
    quant = int(input("Informe a quant de valores pares:"))
num = 4
contPares = 1
while contPares<=quant:
    print(f"Número: {num}")
    parte1 = num//2
    parte2 = parte1

    while parte2 <= parte1:
        contParte1 = 0
        d = 1
        while d<=parte1:
            if parte1 % d == 0: contParte1 = contParte1 + 1
            d = d + 1

        if contParte1 == 2:
            d = 1
            contParte2 = 0
            while d<=parte2:
                if parte2 %d == 0 : contParte2 = contParte2 + 1 
                d = d +1 
            if contParte2 == 2:
                print(f"Primo 1: {parte1} Primo 2: {parte2}")
                contPares = contPares + 1
                break
        parte1 = parte1 + 1
        parte2 = parte2 - 1
    num = num + 2


    