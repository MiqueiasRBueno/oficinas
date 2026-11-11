# aula01_notas.py - Versão 1.0 (Modelo Inicial)

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

# Entrada de dados fixa (hardcoded) para testar o fluxo
nome_aluno = "Carlos Silva"
nota_1 = 8.5
nota_2 = 7.5

# Processamento lógico sequencial
boletim_aluno = CalculadoraNotas(nota_1, nota_2)
media = boletim_aluno.calcular_media()

print(f"Nota média do aluno: {nome_aluno} é de: {media}")