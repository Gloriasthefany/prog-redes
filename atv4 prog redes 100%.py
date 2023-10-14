import os
from datetime import datetime

diretorio_destino = "dados_estatisticos"
if not os.path.exists(diretorio_destino):
    os.makedirs(diretorio_destino)


def processar_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        informacoes = []
# ignorar o cabeçalho
        for linha in linhas[1:]:  
            dados = linha.strip().split(';')
            regiao_sigla = dados[0]
            estado_sigla = dados[1]
            produto = dados[2]
            data_coleta = datetime.strptime(dados[3], '%Y-%m-%d')
            valor_venda = float(dados[4].replace(',', '.'))
            bandeira = dados[5]

            informacoes.append({
                'Regiao': regiao_sigla,
                'Estado': estado_sigla,
                'Produto': produto,
                'Data da Coleta': data_coleta,
                'Valor de Venda': valor_venda,
                'Bandeira': bandeira
            })

    return informacoes

diretorio_origem = os.path.dirname(os.path.realpath(__file__))
arquivos = [f for f in os.listdir(diretorio_origem) if f.startswith('serie_historica_anp')]


lista_completa = []
for arquivo in arquivos:
    caminho_arquivo = os.path.join(diretorio_origem, arquivo)
    lista_completa.extend(processar_arquivo(caminho_arquivo))

arquivo_saida = os.path.join(diretorio_destino, 'serie_historica_anp.txt')
with open(arquivo_saida, 'w') as arquivo_saida:
    for item in lista_completa:
        valores_formatados = [str(valor) for valor in item.values()]
        linha = ';'.join(valores_formatados) + '\n'
        arquivo_saida.write(linha)


media_bandeira = {}
for item in lista_completa:
    chave = (item['Bandeira'], item['Produto'], item['Data da Coleta'].year)
    if chave not in media_bandeira:
        media_bandeira[chave] = {'valor_total': 0, 'quantidade_postos': 0}

    media_bandeira[chave]['valor_total'] += item['Valor de Venda']
    media_bandeira[chave]['quantidade_postos'] += 1

arquivo_media_bandeira = os.path.join(diretorio_destino, 'media_bandeira.txt')
with open(arquivo_media_bandeira, 'w') as arquivo_saida:
    for chave, valores in media_bandeira.items():
        bandeira, produto, ano = chave
        valor_medio_venda = valores['valor_total'] / valores['quantidade_postos']
        linha = f"{bandeira};{produto};{ano};{valor_medio_venda:.2f};{valores['quantidade_postos']}\n"
        arquivo_saida.write(linha)

media_produto_regiao = {}
for item in lista_completa:
    chave = (item['Produto'], item['Regiao'], item['Data da Coleta'].year)
    if chave not in media_produto_regiao:
        media_produto_regiao[chave] = {'valor_total': 0, 'quantidade_postos': 0}

    media_produto_regiao[chave]['valor_total'] += item['Valor de Venda']
    media_produto_regiao[chave]['quantidade_postos'] += 1

arquivo_media_produto_regiao = os.path.join(diretorio_destino, 'media_produto_regiao.txt')
with open(arquivo_media_produto_regiao, 'w') as arquivo_saida:
    for chave, valores in media_produto_regiao.items():
        produto, regiao, ano = chave
        valor_medio = valores['valor_total'] / valores['quantidade_postos']
        linha = f"{produto};{regiao};{ano};{valor_medio:.2f};{valores['quantidade_postos']}\n"
        arquivo_saida.write(linha)

print("Processamento concluído.")
