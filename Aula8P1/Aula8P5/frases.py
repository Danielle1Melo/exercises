'''frases = ["Minha cachorra fugio", 
          "Não quero ir embora", 
          "Eu estudo na puc"]

for sentence in frases:
    print(sentence)

tokens = []
for sentence in frases:
    tokens.append(sentence.split())

for setence in tokens:
    print(f"Palavra da setença: {sentence}")
    for palavra in setence:
        print(palavra)'''

lista1 = [ 1,2,3]
lista2 = []
for num in lista1:
    temp = []
    while num>0:
        num = num -1
        temp.append('a')
    lista2.append(temp)
print(lista2)