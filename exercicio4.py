faturamento_mensal_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

valores = [valores for valores in faturamento_mensal_por_estado.values()]
soma = 0
for valor in valores:
    soma += valor
print(f'O total de faturamento foi: {soma:.2f}')

for estado, valor in faturamento_mensal_por_estado.items():
    percentual = 0
    percentual = valor / soma * 100
    print(f'Percentual {estado}: {percentual:.2f}%')
