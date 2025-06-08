# Arquivo de teste com dados fixos
from cliente_loja.cliente import Cliente  # Importa a classe Cliente do pacote

# Cria um objeto Cliente com valores definidos
cliente1 = Cliente("João", "joao@email.com", 35, 150.00)

# Exibe o cliente usando o método __str__()
print(cliente1)

# Cliente tenta comprar uma camisa por R$50
cliente1.adicionar_compra("Camisa", 50)

# Cliente tenta comprar um tênis por R$120 (não vai conseguir, pois saldo restante será R$100)
cliente1.adicionar_compra("Tênis", 120)

# Exibe todas as compras feitas
cliente1.exibir_compras()

# Mostra o saldo final do cliente
print(f"Saldo restante: R${cliente1.saldo:.2f}")
