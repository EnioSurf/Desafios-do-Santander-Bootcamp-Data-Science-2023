import csv
import yfinance

#Este código lê um arquivo do tipo "csv" contendo os investimentos em bolsa de valores de uma pessoa (código da ação e quantidade de ações),
#e atualiza o arquivo inserindo o valor total investido por ação (em dólares). Foi codificado utilizando o Colab/Google.

with open('meus_investimentos.txt', 'r') as arquivo_entrada:
  leitor_csv = csv.reader(arquivo_entrada)  
  investimentos = list(leitor_csv)

for linha in investimentos:
  if linha[0] != 'codigo_papel':
    preco_usd = float(yfinance.Ticker(linha[0]).info['open'])
    quantidade_papel = (int(linha[1]))
    linha.append((quantidade_papel*preco_usd))
    print(linha)
    print(quantidade_papel)
    print(preco_usd)
  else: linha.append('total_por_papel')

with open('meus_investimentos.txt', 'w', newline='') as arquivo_saida:
  escritor_csv = csv.writer(arquivo_saida)
  for linha in investimentos:
    escritor_csv.writerow(linha)
