meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

# Percorre a lista de vendas extraindo o nome e o valor vendido
for vendedor, valor in vendas:
    if valor >= meta:
        print(f"O(A) vendedor(a) {vendedor} bateu a meta! Valor vendido: {valor}")