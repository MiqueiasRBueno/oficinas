# triagem_v3.py - Código Refatorado com Guard Clauses e Constantes de Negócio

# Constantes de configuração (fácil manutenção e preparação para settings.py no Django)
LIMITE_ALTO_VALOR = 10000
LIMTE_MEDIO_VALOR = 2000
PESO_MAX_AUTOMATICO = 500

# Dados de entrada (mesmo cenário da v2.0 para validação de equivalência)
codigo_pedido = "PED-2026-002"
cliente_ativo = True
valor_pedido = 3200
peso_kg = 620
carga_perecivel = False

print(f'--- Processando o pedido {codigo_pedido} ---')

# Estrutura plana (Flat is better than nested - PEP 20 / Zen of Python)
if not cliente_ativo:
    categoria = "REJEITADO"
    motivo = "Cliente cadastro inativo no sistema."
elif valor_pedido <= 0 or peso_kg <= 0:
    categoria = "REJEITADO"
    motivo = "Valor financeiro ou peso inválidos (devem ser maiores que zero)."
elif carga_perecivel or valor_pedido >= LIMITE_ALTO_VALOR:
    categoria = "PRIORIDADE_ALTA"
    motivo = "Alto valor comercial ou carga perecível."
elif valor_pedido >= LIMTE_MEDIO_VALOR and peso_kg <= PESO_MAX_AUTOMATICO:
    categoria = "PRIORIDADE_MEDIA"
    motivo = "Faixa intermediária dentro do limite de 500 kg."
else:
    categoria = "REVISAO_LOGISTICA"
    motivo = "Pedido fora dos parâmetros automáticos (excesso de peso ou baixo valor)."

print(f"Status final: {categoria}")
print(f"Justificativa: {motivo}")
