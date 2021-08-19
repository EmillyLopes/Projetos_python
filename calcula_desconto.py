def calcula_desconto(preco, desconto):
    novo_preco= preco - (preco * desconto)
    return novo_preco

preco = 50
desconto = 0.1

preco_com_desconto = calcula_desconto(preco,desconto)

print("O preço do produto é: ",preco)
print("O preço do produto com desconto é: ",preco_com_desconto)