# aula01_notas.py - Versão 3.0 (Múltiplas notas, Listas e Validação com try/except)

class CalculadoraNotas:
    # O __init__ recebe os dados e o self guarda dentro de cada objeto
    def __init__(self, nome):
        self.nome = nome
        self.notas = []
        self.pesos = []

    def adicionar_nota(self, nota, peso):
        self.notas.append(nota)
        self.pesos.append(peso)

    def verificar_situacao(self, media):
        if media >= 7: return "Aprovado"
        elif media >= 5: return "Recuperação"
        else: return "Reprovado"

    def calcular_media_simples(self):
        return sum(self.notas) / len(self.notas)
    
    def calcular_media_ponderada(self):
        soma_ponderada = 0
        for i in range(len(self.notas)):
            soma_ponderada += self.notas[i] * self.pesos[i]
        return soma_ponderada / sum(self.pesos)


    
# Entrada de dados dinâmica via teclado
nome_aluno = input("Digite o nome do aluno: ").title().strip()
boletim = CalculadoraNotas(nome_aluno)

# Validação da quantidade de notas
while True:
    try:
        quantidade_notas = int(input("Quantas notas deseja lançar?: "))
        if quantidade_notas > 0:
            break
        print("Digite um número maior que zero.")
    except ValueError:
        print("Erro: Digite apenas números inteiros.")

# Laço para receber cada nota e peso
for i in range(1, quantidade_notas + 1):
    while True:
        try:
            nota = float(input(f"Digite a {i}ª nota (0 a 10): "))
            peso = int(input(f"insira o peso da {i}ª nota: "))
            if 0 <= nota <= 10 and peso > 0:
                boletim.adicionar_nota(nota, peso)
                break
            print("A nota deve ser entre 0 e 10, e o peso maior que 0.")
        except ValueError:
            print("Erro: Digite apenas valores numéricos.")

# Processamento e Saída
media_s = boletim.calcular_media_simples()
media_p = boletim.calcular_media_ponderada()
situacao = boletim.verificar_situacao(media_p)

print("\n---------------------------------------------")
print(f"Boletim do Aluno: {boletim.nome}")
for i in range(len(boletim.notas)):
    print(f"Nota {i + 1} (Peso {boletim.pesos[i]}): {boletim.notas[i]}")
print("---------------------------------------------")
print(f"Média Simples: {media_s:.1f}")
print(f'Media Pondereada: {media_p:.1f}')
print(f"Situação: {situacao}")
print("\n---------------------------------------------")