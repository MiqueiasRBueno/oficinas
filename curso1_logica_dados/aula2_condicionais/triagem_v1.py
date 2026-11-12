# triagem_v1.py - Modelo Base de Classificação de Pedidos

# Dados simulados de entrada (simulando um registro vindo de um formulário ou CSV)
codigo_pedido = "PED-2026-001"
valor_pedido = 4500.00
carga_percivel = True

print(f"--- Iniciando a triagem do pedido {codigo_pedido} ---")

# Estrutura condicional encadeada (if/ elif/ else)
if valor_pedido >= 10000.00 or carga_percivel: categoria = "PRIORIDADE_ALTA"
elif valor_pedido >= 2000.00: categoria = "PRIORIDADE_MÉDIA"
else: categoria = "PADRÃO"

print(f"Valor: R$ {valor_pedido:.2f} | Perecível: {carga_percivel}")
print(f"Classificação atribuída: {categoria}")
