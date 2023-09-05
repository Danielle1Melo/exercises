import string
'''
text = input("Digite uma frase: ")
print(f"Invertida: {text[::-1]}")

if text != text[::-1]:
    print("A frase não é um palínfromo")
else:
    print("A frase é um palíndromo")

    ---------------------------


text = input("Digite uma frase: ")

vogais = "aeiouAEIOU"
totalVogais = 0

for letra in text:
    if letra in vogais:
        totalVogais +=1

print(f"Total de vogais: {totalVogais}")
 
-------------------------------------
    

print(string.ascii_uppercase)
senha = input("Senha: ")

maiuscula = False
digito = False
pontuacao = False

if len(senha) < 8 :
    print("Error: senha curta")
    
else :
    for letra in senha:
        if letra in string.ascii_uppercase:
            maiuscula = True
        if letra in string.digits:
            digito=True
        if letra in string.punctuation:
            pontuacao=True
    if maiuscula == False or digito== False or pontuacao==False:
        if maiuscula == False:
            print("Não tem maisucula")
        if digito == False:
            print("Não tem digito")
        if pontuacao == False:
            print("Não tem pontuação")
    else:
        print("Senha válida")
 
        ---------------------------------
'''

nome = input("DIgite o nome completo: ")

inicio = True
for letra in nome: 
    if inicio:
        print(f"{letra}. ", end="")
        inicio = False
    elif letra == " ":
        inicio = True
