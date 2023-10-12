import pandas as pd
import json

# Carregue o arquivo .xlsx em um DataFrame do pandas
df = pd.read_excel('september-invoice.xlsx')

# Converta a coluna "Data de Compra" para o formato de data (se necessário)
df['Data de Compra'] = pd.to_datetime(df['Data de Compra'], errors='coerce')

# Substitua 'Data de Compra' pelo nome correto da coluna de datas no seu arquivo
df['Data de Compra'] = df['Data de Compra'].dt.strftime('%Y-%m-%d')

# Criar uma função para serializar as datas


def date_converter(o):
    if isinstance(o, pd.Timestamp):
        return o.strftime('%Y-%m-%d')
    return str(o)


# Converta o DataFrame para uma lista de dicionários
data = df.to_dict(orient='records')

# Escreva o dicionário em um arquivo JSON com a função de conversão de data
with open('saida.json', 'w') as json_file:
    json.dump(data, json_file, indent=4, default=date_converter)

print("Conversão concluída. Os dados foram salvos em 'saida.json'.")

soma_valores = sum(item['Valor (em R$)'] for item in data)
print(f'Soma dos valores: {soma_valores}')
