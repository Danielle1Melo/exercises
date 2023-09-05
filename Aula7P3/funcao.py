''' def potencia (num):
    return num ** 2

def somaPotencia (a, b, c):
    return potencia(a) + potencia(b) + potencia(c)

val1 = int(input("Informe um n°: "))
val2 = int(input("Informe um n°: "))
val3 = int(input("Informe um n°: "))
result = somaPotencia(val1, val2, val3)

print(f"Soma das Potencias: {result}")

---------------------------------------------------
'''

def calcula (base, taxa, duracao):
    final = base * (1+taxa) ** duracao
    return final

b = float(input("Valor inicial: "))
t= float(input("Taxa de juros mensal: "))
d = float(input("Duração (meses): "))

res = calcula(b,t,d)
print(f"Valor no final do período {res:.2f}")




