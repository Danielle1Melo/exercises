import math


val1 = int(input("Informe o primeiro valor: "))
val2 = int(input("Informe o segundo valor: "))
#Soma
result = val1+val2
print("Soma: ", result)

#Diferença
resultDiferent = val1-val2
print("Diferença: ", resultDiferent)

#Media
resultMedia = result/2
print("Média: ", resultMedia)

#Distancia
resultDistancia = math.fabs(val1-val2)
print("Distância: ", resultMedia)
 
#Maior
resultMaior = ((val1+val2 + math.fabs(val1-val2))/2)
print("Maior dos dois: ", resultMaior)

#Menor
resultMenor = ((val1+val2 - math.fabs(val1-val2))/2)
print("Menor dos dois: ", resultMenor)