palavra = input("Digite uma palavra: ").lower()
vogais = "aeiou"

i = 0
total_vogais = 0

while i < len(palavra):
    if palavra[i] in vogais:
        total_vogais += 1
    i += 1

print(f"Número de vogais: {total_vogais}")