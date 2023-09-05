mes = int(input("Informe o número de um mês: "))
ano = int(input("Informe o ano: "))

if mes == 2:
    if (ano%4==0 and ano%100!=0) or (ano%400==0):
        dias = 29
    else:
        dias = 28
elif mes == 4 or mes == 6 or mes==9 or mes==11:
    dias = 30
else:
    dias = 31
print(f"Total de dias: {dias}")