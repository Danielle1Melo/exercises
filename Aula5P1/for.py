import math

#for cont in range(10):
#   print(cont)

#for cont in range (1,13,2):
#   print(cont)

#for cont in range(10,0,-1):
#   print(cont)
'''
#Exbindo tabela de resultados
for num in range (1,15):               #casa com 3 digítos
    print(f"{num:2}: {math.sqrt(num) : .3f}")
--------------------------------------------------------------------

#ACumulador
soma = 0
num = int(input("Num: "))
for cont in range (1, num+1) :
    soma = soma+cont
print(f"Somátorio: {soma}")

------------------------

#Calcular aproximação de raiz quadrada
num = int(input("Valor desejado: "))
total = int(input("Quantidade de repetições: "))

aprox = 1
for cont in range (total):
    aprox = (aprox + num/aprox) /2
    print(f"{cont:3} {aprox:.5f}")

print(f"Raiz aproximada: {aprox:.5f}")
'''

#break
for cont in range(20):
    if cont > 10:
        break
    print(cont)

print("Continuando ")

#continue
for cont in range(20):
    if cont % 2 == 1:
        print(cont) # ->pula todos num pares
        continue
    #print(cont) -> pula todos num impares
print ("Continuação")