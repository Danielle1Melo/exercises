num = 1

while num <= 100:
    print(f"Número: {num}")
    divisores = 1
    while divisores <=num:
        if num % divisores == 0: print(f"{divisores} divide {num}")
        divisores = divisores + 1
    num = num+1
