# Faça um programa que mostre a soma de dois valores, e depois mostre o antecessor e o sucessor do mesmo.

num1 = int(input("Informe um primeiro número: "))
num2 = int(input("Informe um segundo número: "))
soma = num1 + num2

print(f"A soma de {num1} e {num2} resulta em {soma}, seu antecessor é {soma - 1} e seu sucessor é {soma + 1}")

