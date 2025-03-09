import json

with open("E:\Programação\Python\Algoritmo\ED2\python\Arvore\TesteTecnico\dados.json", "r") as file:
    dados = json.load(file)

faturamentos = [dia["valor"] for dia in dados if dia["valor"] > 0]

menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)
media_mensal = sum(faturamentos) / len(faturamentos)

dias_acima_media = sum(1 for valor in faturamentos if valor > media_mensal)

print(f"Menor faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento: R$ {maior_faturamento:.2f}")
print(f"Dias com faturamento acima da media: {dias_acima_media}")
