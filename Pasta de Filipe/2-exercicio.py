import os
os.system('cls')

vetor_dia = []
vetor_temp = []
maior_temperatura = 0
menor_temperatura = 0
dia_da_semana = 3


for i in range(dia_da_semana):
    dia = str(input('\nDigite o dia da semana: '))
    temp = float(input('Digite a temperatura: '))
    vetor_dia.append(dia)
    vetor_temp.append(temp)

media = sum(vetor_temp) / dia_da_semana

maior_temperatura = max(vetor_temp)
menor_temperatura = min(vetor_temp)


for i in range(dia_da_semana):
    print(f'\nDia da semana: {vetor_dia[i]} Temperatura: {vetor_temp[i]}')
print(f'\nA média da semana é: {media}')
print(f'A maior temperatura: {maior_temperatura}')
print(f'A menor temperatura: {menor_temperatura}')
