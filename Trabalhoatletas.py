import random

tempos_treinos = [[random.uniform(10, 15) for _ in range(3)] for _ in range(75)] 

print("Lista de tempos dos atletas:")
for i, tempos in enumerate(tempos_treinos, 1):
    print(f"Atleta {i}: {tempos}")

dados_atletas = []
nomes = [f"Atleta_{i+1}" for i in range(75)]
idades = [random.randint(18, 35) for _ in range(75)]

for i in range(75):
    atleta = {
        "nome": nomes[i],
        "idade": idades[i],
        "tempos": tempos_treinos[i],
        "melhor_tempo": min(tempos_treinos[i]),
        "media_tempo": sum(tempos_treinos[i]) / len(tempos_treinos[i]),
    }
    dados_atletas.append(atleta)

print("\nDetalhes dos 75 atletas:")
for atleta in dados_atletas: 
    print(f"Nome: {atleta['nome']}, Idade: {atleta['idade']}")
    print(f"Tempos: {atleta['tempos']}")
    print(f"Melhor Tempo: {atleta['melhor_tempo']:.2f} segundos")
    print(f"Média de Tempo: {atleta['media_tempo']:.2f} segundos\n")
