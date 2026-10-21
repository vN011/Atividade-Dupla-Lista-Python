import os
os.system('cls')

vetor_nome = []
vetor_salario = []
quantidade = 5
quant_sala = 0


for i in range(quantidade):
    nome = str(input('Digite seu nome: '))
    salario = float(input('\nDigite seu salario: '))
    vetor_nome.append(nome)
    vetor_salario.append(salario)
    if salario > 2000:
        quant_sala += 1

maior_salario = max(vetor_salario)

