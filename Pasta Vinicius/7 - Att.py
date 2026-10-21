import os
os.system("cls")

numeros = []
positivos = []
quantidade_positivos = 0

print("Digite 10 números inteiros:")
for i in range(10):
    numero = int(input(f"{i + 1}º número: "))
    numeros.append(numero)
    
    
    if numero > 0:
        positivos.append(numero)
        quantidade_positivos += 1


print("\n--- Resultados ---")
print(f"Vetor com os positivos: {positivos}")
print(f"Total de números copiados: {quantidade_positivos}")