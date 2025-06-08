# Arquivo de teste interativo com entrada do usuário
from cliente_loja.cliente import Cliente  # Importa a classe Cliente

# Coleta informações básicas do cliente
nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
idade = int(input("Digite sua idade: "))
saldo = float(input("Digite seu saldo inicial: R$"))

# Cria um objeto Cliente com os dados fornecidos
cliente = Cliente(nome, email, idade, saldo)

# Pergunta quantos produtos o cliente quer comprar
qtd = int(input("Quantos produtos deseja comprar? "))

# Laço para fazer as compras
for i in range(qtd):
    print(f"\nProduto {i+1}:")                          # Indica o número do produto
    item = input("Nome do produto: ")                   # Nome do item
    preco = float(input("Preço do produto: R$"))        # Preço do item
    cliente.adicionar_compra(item, preco)               # Tenta fazer a compra

# Exibe todas as compras feitas
print("\nResumo de compras:")
cliente.exibir_compras()

# Mostra saldo final
print(f"Saldo final: R${cliente.saldo:.2f}")

# Mostra nome e email do cliente usando __str__()
print(f"Cliente: {cliente}")
