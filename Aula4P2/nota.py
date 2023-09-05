p1 = float(input("Informe a nota da p1: "))
p2 = float(input("Informe a nota da p2: "))
p3 = float(input("Informe a nota da p3: "))
freq = float(input("Frequencia: "))

g1 = (p1+p2+p3)/3

print(f"Media G1: {g1}")

if freq < 75:
    print(f"Reprovado por faltas: {freq}")
else:
    if g1 >= 7:
        print(f"Aprovado por media: {g1}")
    else: 
        if g1 < 4:
            print(f"Reprovado por media: {g1}")
        else:
            #exame (g2)
            g2 = float(input("G2: "))
            final = (g1+g2)/2
            if final >=5: 
                print(f"Aprovado em g2: {final}")
            else: 
                print(f"Reprovado: {final}")