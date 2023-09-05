
num1 = int(input("Informe um número: "))
num2 = int(input("Informe um número: "))
num3 = int(input("Informe um número: "))
num4 = int(input("Informe um número: "))
'''
#Para 3 valores
maior = num1
if num2>maior : maior=num2
if num3>maior : maior=num3

menor = num1
if num2<menor : menor=num2
if num3<menor : menor=num3

meio = num1+num2+num3 - maior - menor

print("Ordem crescente: ", menor, meio, maior)
print("Ordem decrescente: ", maior, meio, menor)

---------------------------------------------------------
'''
#Para 4 valores
if num2<num1:
    aux = num1
    num1= num2
    num2=aux

if num3<num1:
    aux = num1
    num1 = num3
    num3 = aux

if num4<num1:
    aux = num1
    num1 = num4
    num4 = aux

if num3<num2:
    aux = num2
    num2= num3
    num3= aux

if num4<num2:
    aux = num2
    num2= num4
    num4= aux

if num4<num3:
    aux = num3
    num3 = num4
    num4=aux

print("Ordem crescrente: ", num1, num2, num3, num4)
print("Ordem decrescente: ", num4, num3, num2, num1)

