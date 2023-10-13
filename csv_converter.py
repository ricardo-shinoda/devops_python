import pandas as pd
import json

# Carregue o arquivo .csv em um DataFrame do pandas
# Substitua 'input.csv' pelo nome do seu arquivo CSV
df = pd.read_csv('invoice.csv', delimiter=';')

# Criar uma função para serializar as datas, se necessário


def date_converter(o):
    if isinstance(o, pd.Timestamp):
        return o.strftime('%Y-%m-%d')
    return str(o)


# Converta o DataFrame para uma lista de dicionários
data = df.to_dict(orient='records')

# Escreva o dicionário em um arquivo JSON com a função de conversão de data, se necessário
with open('saida.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4,
              default=date_converter, ensure_ascii=False)

print("Conversão concluída. Os dados foram salvos em 'saida.json'.")

soma_valores = sum(item["Valor (em R$)"] for item in data)
print(f'Soma dos valores: {soma_valores}')
