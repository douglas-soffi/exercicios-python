# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento. salario + (salario*15/100)

salario = float(input("Informe o salário: "))
aumento = salario + (15 / 100)
novo_salario = salario + aumento

print(f"Seu salário com aumento é R${novo_salario}")