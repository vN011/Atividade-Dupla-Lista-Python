import os
os.system("cls")


notas = []
soma = 0

print("Digite as 5 notas da turma:")
for i in range(5):
    nota = float(input(f"{i + 1}ª nota: "))
    notas.append(nota)
    soma += nota

media = soma / 5

notas_acima_media = 0
for nota in notas:
    if nota > media:
        notas_acima_media += 1

print("\n--- Resultados ---")
print(f"Notas da turma: {notas}")
print(f"Média da turma: {media}")
print(f"Alunos com nota acima da média: {notas_acima_media}")