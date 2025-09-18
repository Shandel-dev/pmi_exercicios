print("Programa que calcula o desconto de um produto")
preco = float(input("Informe o preço de um produto: R$"))
desconto = int(input("Qual será o desconto desse produto?(%): "))
print("Preço do produto após desconto: R${:.2f}".format(preco - (preco * desconto / 100)))