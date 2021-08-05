# Faça um programa que receba um valor, e traga informações sobre esse valor, dizendo se é alfanumérico, numérico e etc.

num = input("Informe um valor: ")

if num.isalpha() and num.isupper():
    msg = "é letra do alfabeto e está em maiúsculo"

elif num.isalpha() and num.islower():
    msg = "é letra do alfabeto e está em minúsculo"

elif num.isalnum():
    msg = "alfanumérico"

elif num.isnumeric():
    msg = "número"

print(f"Status: {msg}")