num = 0
while num <= 99:
    fat = 1
    aux = 2 
    while aux <= num:
        fat = fat * aux 
        aux = aux + 1
    print(f"Fatorial de: {num} é {fat}")
    num = num + 1