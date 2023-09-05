nota = float(input("Informe sua nota: "))

if nota>=90:
    print(f"Conceito A {nota}")
elif nota>=80:
    print(f"Conceito B {nota}")
elif nota>=70:
    print(f"Conceito C {nota}")
elif nota>=60:
    print(f"Conceito D {nota}")
else:
    print(f"Conceito F {nota}")