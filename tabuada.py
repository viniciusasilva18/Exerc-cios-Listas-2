senha_correta = "python123"
tentativa = ""

while tentativa != senha_correta:
    tentativa = input("Digite a senha para entrar: ")
    
    if tentativa != senha_correta:
        print("Senha errada! Tenta de novo.")

print("Acesso liberado!")