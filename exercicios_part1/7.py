# Leia um número, mostre seu dobro, triplo, e raíz quadrada.

import math

num = int(input("Informe um número: "))
dobro = num * 2
triplo = num * 3
raiz = math.sqrt(num)

print(f'''
Número: {num}
Dobro: {dobro}
Triplo: {triplo}
Raíz Quadrada: {raiz}
''')