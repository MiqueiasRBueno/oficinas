# aula01_notas.py - Versão 2.0 (Entrada dinâmica e Média Ponderada)

class CalculadoraNotas:
    # O __init__ recebe os dados e o self guarda dentro de cada objeto
    def __init__(self, nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_soma(self):
        return self.nota1 + self.nota2

    def calcular_media(self):
        soma_notas = self.calcular_soma()
        return soma_notas / 2

    def calcular_media_ponderada(self, peso1, peso2):
        soma_ponderada = (self.nota1 * peso1) + (self.nota2 * peso2)
        soma_pesos = peso1 + peso2
        return soma_ponderada / soma_pesos


    
# Entrada de dados dinâmica via teclado
nome_aluno = str(input("Digite o nome do aluno: ")).title()
nota_1 = float(input("Digite a 1ª nota do aluno: "))
nota_2 = float(input("Digite a 2ª nota do aluno: "))
peso_1 = int(input("Insira o peso da 1ª nota: "))
peso_2 = int(input("Insira o peso da 2ª nota: "))

# Processamento lógico
boletim_aluno = CalculadoraNotas(nota_1, nota_2)

# Saída de dados
print("---------------------------------------------")
print(f"Boletim do Aluno: {nome_aluno}")
print(f"Nota 1 (Peso {peso_1}):", nota_1)
print(f"Nota 2 (Peso {peso_2}):", nota_2)
print(f"Média Simples: {boletim_aluno.calcular_media():.1f}")
print(f"Média Ponderada: {boletim_aluno.calcular_media_ponderada(peso_1, peso_2):.1f}")