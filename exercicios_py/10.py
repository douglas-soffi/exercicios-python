#  Faça um programa que leia um valor, e mostre a sua tabuada do 1 ao 10 na tela.

num = int(input("Informe um número: "))

for x in range(1, 11):
    print(f"{num} * {x} = {num * x}")