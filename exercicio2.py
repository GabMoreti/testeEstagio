#Coleta a palavra ou frase escolhida pelo usuário
string = str(input("Escreva uma palavra ou frase: "))

#Contagem dos caracteres
contagem_A = 0
contagem_a = 0

#Checagem
for char in string:
    if char == "A":
        contagem_A += 1
    elif char == "a":
        contagem_a += 1

print("A letra A/a aparece", contagem_a + contagem_A, "vezes")