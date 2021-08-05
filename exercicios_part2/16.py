#  Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

km_percorrido = float(input("Informe a quantidade de km percorridos: "))
dia_alugado = float(input("Informe a quantidade de dias alugados: "))
preco_dia = 60
preco_km = 0.15

total_dia = dia_alugado * preco_dia
total_km = km_percorrido / preco_km

soma = total_dia + total_km

print(f"Deverá ser pago um total de R${soma}")