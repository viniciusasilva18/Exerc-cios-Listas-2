numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma_total = 0

# Primeiro for entra em cada lista interna
for lista in numeros:
    # Segundo for entra nos números de cada lista
    for numero in lista:
        print(f"Número: {numero}")
        soma_total += numero

print("-" * 20)
print(f"Soma total: {soma_total}")