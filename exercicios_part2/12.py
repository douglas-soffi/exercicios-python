# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados. area = larg x altura tinta = area/2

l = float(input("Informe a largura da parede: "))
h = float(input("Informe a altura da parede: "))
A = l * h
tinta = A / 2

print("Serão usados {} latas de tinta".format(tinta))