import os
os.system('cls')

vetor_A = []
vetor_B = []
quantidade = 5


for i in range(quantidade):
    numero = int(input(f'Digite o {i+1}ª numero do vetor A: '))
    vetor_A.append(numero)

print()
for i in range(quantidade):
    numero2 = int(input(f'Digite o {i+1}ª numero do vetor B: '))
    vetor_B.append(numero2)

soma = sum(vetor_A + vetor_B)

print()
for vetor_A, vetor_B in enumerate(vetor_B,start=1):
    print(f'Vetor A: {vetor_A} + Vetor B = {vetor_B} = Vetor C: {vetor_A + vetor_B} ')
