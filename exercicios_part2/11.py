# Faça um programa que insira um valor em reais, e faça ele converter o valor para dólar, mostrando quantos dólares podem s

real = float(input("Informe a quantia em R$ para converter em US$: "))
dolar = real / 5.30

print("R${} dá US${}".format(real, dolar))