# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. preço = preço - (preço *5/100)

preco = float(input("Informe o preço do produto: "))
desconto = 5 / 100
novo_preco = preco * desconto

print(f"O valor com desconto é R${novo_preco}")