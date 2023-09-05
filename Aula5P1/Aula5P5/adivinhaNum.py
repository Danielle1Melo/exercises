import random

for cont in range (10):
    jogadorNum = int(input("Adivinhe o número:"))
    compNum = random.randint(1,100)
    if jogadorNum > compNum:
        print("O número é menor")
    elif jogadorNum < compNum :
        print("O número é maior")
    elif jogadorNum == compNum :
        print(f"Voçê acertou {compNum}")
        break
else:
    print(f"Acabou as chances o num era {compNum}")
