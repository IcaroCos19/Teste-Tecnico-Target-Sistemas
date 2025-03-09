import json

with open("E:\Programação\Python\Algoritmo\ED2\python\Arvore\TesteTecnico\dados.json", "r") as file:
    dados = json.load(file)

faturamentos = [dia["valor"] for dia in dados if dia["valor"] > 0]

menorFaturamento = min(faturamentos)
maiorFaturamento = max(faturamentos)
mediaMensal = sum(faturamentos) / len(faturamentos)

diasAcimaMedia = sum(1 for valor in faturamentos if valor > mediaMensal)

print(f"Menor faturamento: R$ {menorFaturamento:.2f}")
print(f"Maior faturamento: R$ {maiorFaturamento:.2f}")
print(f"Dias com faturamento acima da media: {diasAcimaMedia}")
