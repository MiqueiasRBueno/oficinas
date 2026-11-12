# Constantes de configuração

TEMPERATURA_MAX = 60
TEMPERATURA_MIN = -50
TEMPERATURA_IDEAL = -5.0
TEMPERATURA_ATENCAO = 8.0


# Variáveis de entrada

sensor_id = "SENS_BR_09"
sensor_online = True
temperatura_celsius = 35
porta_aberta = True

# Regras de negócio

if not sensor_online or (TEMPERATURA_MIN > temperatura_celsius or temperatura_celsius > TEMPERATURA_MAX):
    condicao = "ERRO_HARDWARE"
elif temperatura_celsius > TEMPERATURA_ATENCAO and not porta_aberta:
    condicao = "ALERTA_CRITICO"
elif (temperatura_celsius > TEMPERATURA_ATENCAO and porta_aberta) or (TEMPERATURA_IDEAL <= temperatura_celsius <= TEMPERATURA_ATENCAO):
    condicao = "AVISO_OPERACIONAL"
else:
    condicao = "OPERACAO_NORMAL"

print(f"Condição apresentada: {condicao}")