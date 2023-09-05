import math

tempo = int(input("Informe o tempo em segundos: "))
horas = tempo//3600
resto = tempo%3600
min = resto//60
seg = resto % 60
print ("Horas:" , horas, "Minutos:", min, "Segundos:", seg)
