total = 0
cont0_25 = 0
cont26_50 = 0
cont51_75 = 0
cont76_100= 0

while True:
    print("Informe um valor negativo para encerrar o programa")
    valor = int(input("Informe um valor inteiro: "))
    if valor < 0:
        print("Fim do programa")
        break 
    if valor <= 25: cont0_25 = cont0_25 + 1
    else:
        if valor <= 50: cont26_50 = cont26_50 + 1
        else: 
            if valor <= 75: cont51_75 = cont51_75 + 1
            else:
                if valor<=100: cont76_100 = cont76_100 + 1
    total = total + 1

print(f"Total de valores: {total}")
print(f"Intervalo de [0;25]: {cont0_25}")
print(f"Intervalo de [26;50]: {cont26_50}")
print(f"Intervalo de [51;75]: {cont51_75}")
print(f"Intervalo de [76;100]: {cont76_100}")

