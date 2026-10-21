import os
os.system("cls")

vetor = []

for i in range(6):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(numero)

print(f"\nVetor antes: {vetor}")

for i in range(6):
    if vetor[i] % 2 == 0:
        vetor[i] = 0
    else:
        vetor[i] = 1

print(f"Vetor depois: {vetor}")