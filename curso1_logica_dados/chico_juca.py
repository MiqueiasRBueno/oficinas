# 1. Chico tem 1,50m e cresce 2 centímetros por ano, enquanto Juca tem 
# 1,10m e cresce 3 centímetros por ano. Construir um algoritmo que calcule
# e imprima quantos anos serão necessários para que Juca seja maior que
# Chico. 

TAXA_CHICO = 2
TAXA_JUCA = 3

chico = 150
juca = 110
anos = 0
while chico >= juca:
    chico += TAXA_CHICO
    juca += TAXA_JUCA
    anos +=1

print(f"Total de anos para Juca ser maior que Chico: {anos}.")