# triagem_v2.py - Inclusão de Validação de Dados e Regras de Peso/Status

# Dados simulados de entrada (simulando um registro vindo de um formulário ou CSV)
codigo_pedido = "PED-2026-002"
cliente_ativo = True
valor_pedido = 3200.00
peso_kg = 620.0
carga_perecivel = False

print(f"--- Processando pedido {codigo_pedido} ---")

# Camada 1: Validação de integridade e elegibilidade do registro
if not cliente_ativo:
    categoria = "REJEITADO"
    motivo = "Cliente com cadastro inativo no sistema."
else:
    if valor_pedido <= 0 or peso_kg <= 0:
        categoria = "REJEITADO"
        motivo = "Valor financeiro ou peso inválidos. (Devem ser maior que zero)"
    else:
        # Camada 2: Classificação operacional para registros válidos
        if valor_pedido >= 10000 or carga_perecivel:
            categoria = "PRIORIDADE ALTA"
            motivo = "Alto valor comercial ou carga perecível."
        elif valor_pedido >= 2000:
            categoria = "PRIORIDADE_MEDIA"
            motivo = "Faixa intermediária dentro do limite de 500 kg."
        else:
            categoria = "REVISÃO_LOGISTICA"
            motivo = "Pedido fora dos parâmentros automáticos (Excesso de peso ou baixo valor)."
print(f"Status final: {categoria}")
print(f"Justificativa: {motivo}")