venda = [250, 330, 440, 540, 350, 250, 368, 40, 250, 30, 30]
vendedores = ['maria', 'mara', 'joão', 'silva', 'santos', 'mario', 'carlos', 'marly', 'xuxa', 'chica', 'zinha']

meta = 50

# Inicializa o contador de índice
i = 0

# O loop roda enquanto 'i' for menor que o número total de vendedores
while i < len(vendedores):
    # Verifica se a venda do vendedor atual é maior ou igual à meta
    if venda[i] >= meta:
        print(vendedores[i])
    
    # Incrementa o contador para não dar loop infinito
    i += 1