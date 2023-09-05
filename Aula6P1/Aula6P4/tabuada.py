#Tabuada com for
'''for num in range (1,11):
    for valor in range (1,11):
        mult = num * valor
        print(f"{num} X {valor} = {mult}")
    print()

-----------------------------------------
'''
#Tabuada com While
num = 1
while num <=10:
    valor=1
    while valor<=10:
        mult = num * valor
        print(f"{num} X {valor} = {mult}")
        valor = valor + 1
    print()
    num = num + 1
