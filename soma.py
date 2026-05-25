# Inicializa a soma acumulada e o primeiro número sequencial
soma = 0
numero = 1

# O loop continua enquanto a soma NÃO ultrapassar 20
while soma <= 20:
    soma += numero
    print(f"Somando {numero}... Total atual: {soma}")
    numero += 1  # Passa para o próximo número inteiro

print("---")
print(f"Fim de jogo! A soma final foi {soma}, ultrapassando o limite de 20.")