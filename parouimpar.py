# Verificador de Par ou Ímpar
numero = int(input("Digite um número para verificar se ele é par ou ímpar: "))
verificador = numero % 2

if verificador == 0:
    print(f"O número {numero} é par!")
else:
    print(f"O número {numero} é ímpar!")
