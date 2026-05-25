import random

# O computador escolhe um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# Inicializa o contador de tentativas e a variável do palpite
tentativas = 0
palpite = 0

print(" Bem-vindo ao jogo de adivinhação!")
print("Pensei em um número entre 1 e 100. Tente adivinhar!")
print("--------------------------------------------------")

# O loop continua até que o palpite seja igual ao número secreto
while palpite != numero_secreto:
    # Recebe o palpite do jogador
    palpite = int(input("Digite o seu palpite: "))
    tentativas += 1  # Conta a tentativa atual
    
    # Dá as dicas ao jogador
    if palpite < numero_secreto:
        print("MUITO BAIXO! Tente um número maior. ")
    elif palpite > numero_secreto:
        print("MUITO ALTO! Tente um número menor. ")

print("--------------------------------------------------")
print(f" PARABÉNS! Você acertou! O número era {numero_secreto}.")
print(f" Você precisou de {tentativas} tentativas para vencer.")