# 1. Pergunta a quantidade de pessoas no quarto
quantidade_pessoas = int(input("Quantas pessoas vão ficar no quarto (1 a 4)? "))

quarto = []

# 2. Roda o for para cadastrar cada uma
for i in range(quantidade_pessoas):
    print(f"\n--- Cadastro da {i + 1}ª pessoa ---")
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    
    # 3. Adiciona a sublista com nome e cpf na lista do quarto
    quarto.append([nome, f"cpf:{cpf}"])

# Exibe o resultado final
print("\nQuarto registrado com sucesso:")
print(quarto)