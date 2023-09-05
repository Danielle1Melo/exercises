import math

#Volume 
raio = float(input("Informe o valor do raio:"))
vol = 4/3 * math.pi * math.pow(raio, 3)
2
print("Volume da esfera: ", vol)

#Area
raio = float(input("Informe o valor do raio:"))
area = 4 * math.pi * math.pow(raio,2) 
print("Area da esfera: ", area)

#Valor n
n = float(input("Informe um valor:"))
print("Quadrado do valor: ",math.pow(n,2))
print("Cubo do valor: ", math.pow(n,3))
print("Valor na valor: ", math.pow(n,4))