import os
os.system("cls")

vetor_numeros = []

for i in range(5):
    numero = int(input(f"Informe o {i+1}° Número: "))
    vetor_numeros.append(numero)
os.system("cls")

for i in range(5):
    print(f"{vetor_numeros[i]}")

print()

for i in range(numero,0,-1):
    print(f"{i}")
print(f"\nFim!")