import os
os.system('cls')

vetor_idade = []
quantidade = 5
maior_numero = 0
menor_numero = 0
quant_maior = 0
quant_inva = 0

for i in range(quantidade):
    idade = int(input('Digite sua idade: '))
    if idade > 0 and idade < 120:
        vetor_idade.append(idade)
        if idade >= 18:
            quant_maior += 1
    else:
        quant_inva += 1

print()

maior_numero = max(vetor_idade)
menor_numero = min(vetor_idade)


print(f'Valores invalidos: {quant_inva}')
print(f'A maior idade: {maior_numero}')
print(f'A menor idade: {menor_numero}')
print(f'A quantidade de maiores de idade: {quant_maior}')

