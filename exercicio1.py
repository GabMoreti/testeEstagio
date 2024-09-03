#Array com 18 números da Sequência de Fibonacci
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]

#Variável para guardar o número que o usuário quer checar se pertence à sequência
numero = int(input ("Insira um número: "))

#Checagem
if numero in fibonacci:
    print("O número pertence a sequência de Fibonacci!")
else:
    print("O número não pertence a sequência de Fibonacci!")