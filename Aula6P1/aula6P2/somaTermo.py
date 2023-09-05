'''numTermo = int(input('Informe a quant de termos: '))
if numTermo <=0:print("Número inválido")
else:
    soma = 0
    cont = 1
    while cont <= numTermo:
        soma = soma + 1/cont
        cont = cont + 1
    print(f"Soma dos termos: {soma}")

----------------------------------------------------------

numTermo = int(input('Informe a quant de termos: '))
if numTermo <=0:print("Número inválido")
else:
    soma = 0
    cont = 1
    numerador = 2
    denominador = 1
    while cont <= numTermo:
        soma = soma + numerador/denominador
        cont = cont + 1
        numerador = numerador + 2
        denominador = denominador + 2
    print(f"Soma dos termos: {soma}")

-----------------------------------------------------------

val1 = int(input("Informe um valor: "))
val2 = int(input("Informe um valor: "))

while val1<0 or val2<0:
    print("Número inválido, apenas inteiros") 
    val1 = int(input("Informe um valor: "))
    val2 = int(input("Informe um valor: "))
   
if val1 > val2:
    aux = val1
    val1 = val2
    val2 = aux
if val1%2==0: val1 = val1 + 1
soma = 0
print("Valores impares do intervalo: ")
while val1<=val2:
    print(val1)
    soma = soma + val1
    val1 = val1 + 2
print(f"Soma dos impares do intervalo: {soma}")
-------------------------------------------------------
'''

#SOMA DOS DIVISORES - N° PERFEITOS
num = int(input("Informe um número inteiro e positivo:"))
while num<=0:
    print("Número inválido")
    num = int(input("Informe um número inteiro e positivo:"))

soma = 0
d= 1
while d<=num/2:
    if num % d ==0 : soma =soma +d
    d =d +1

if soma == num: print(f"{num} é perfeito")
else: print(f"{num} não é perfeito")    