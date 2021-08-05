# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit. farenheit é ((9*celsius)/5)+32

c = float(input("Informe a temperatura em C°: "))
f = ((9*c)/5)+32

print(f"A temperatura em F° é {f}")