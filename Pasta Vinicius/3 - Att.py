import os
os.system("cls")

vetor = []
soma = 0
maiores_que_dez = 0

print("Digite 10 números inteiros:")
for i in range(10):
    numero = int(input(f"{i + 1}º Número: "))
    vetor.append(numero)
    
    
    soma += numero
    
    
    if numero > 10:
        maiores_que_dez += 1

# Exibe os resultados
print("\n--- Resultados ---")
print(f"Vetor: {vetor}")
print(f"Soma de todos os Números: {soma}")
print(f"Quantidade de números maiores que 10: {maiores_que_dez}")