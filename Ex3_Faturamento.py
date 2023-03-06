import json

# Lê o arquivo JSON com os dados do faturamento diário
with open('dados.json', 'r') as f:
    faturamento = json.load(f)

# Calcula o menor e o maior valor de faturamento diário ocorrido em um dia do mês
valores_faturamento = [dia['valor'] for dia in faturamento]
min_faturamento = min(valores_faturamento)
max_faturamento = max(valores_faturamento)

# Calcula a média mensal de faturamento diário
dias_com_faturamento = [dia for dia in faturamento if dia['valor'] > 0]
media_faturamento = sum(dia['valor'] for dia in dias_com_faturamento) / len(dias_com_faturamento)

# Calcula o número de dias no mês em que o valor de faturamento diário foi superior à média mensal
dias_acima_da_media = len([dia for dia in faturamento if dia['valor'] > media_faturamento])

# Imprime os resultados
print(f'Menor valor de faturamento diário: R$ {min_faturamento:.2f}')
print(f'Maior valor de faturamento diário: R$ {max_faturamento:.2f}')
print(f'Número de dias com faturamento acima da média: {dias_acima_da_media}')
