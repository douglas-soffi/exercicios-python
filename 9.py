# Faça um programa que leia um valor em metros, mostre o valor convertido em centímetros, e milímetros.

m = float(input("Informe uma distância em metros(m): "))
cm = m / 100
mm = m / 1000

print(f'''
m: {m}
cm: {cm}
mm: {mm}
''')