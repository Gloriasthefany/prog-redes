def ler_arquivo_cartola(ano):
    try:
        arquivo = f'cartola_fc_{ano}.txt'
        with open(arquivo, 'r') as file:
            dados_cartola = []
            for linha in file.readlines():
                jogador = linha.strip().split(';')
                dados_cartola.append({
                    'posicao': jogador[0],
                    'nome': jogador[1],
                    'url_foto': jogador[2],
                    'pontuacao': jogador[3],
                    'time': jogador[4],
                    'url_escudo_time': jogador[5]
                })
        return dados_cartola
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return None


def selecionar_jogadores(esquema_tatico, dados_cartola):
    posicoes = {
        '4-3-3': {'Goleiro': 1, 'Zagueiro': 4, 'Lateral': 3, 'Meia': 3, 'Atacante': 3, 'Técnico': 1},
        '3-4-3': {'Goleiro': 1, 'Zagueiro': 3, 'Lateral': 4, 'Meia': 3, 'Atacante': 3, 'Técnico': 1},
        '4-4-2': {'Goleiro': 1, 'Zagueiro': 4, 'Lateral': 4, 'Meia': 4, 'Atacante': 2, 'Técnico': 1}
    }

    esquema = posicoes.get(esquema_tatico)

    if esquema is None:
        print("Esquema tático inválido.")
        return None

    selecao = []

    for posicao, quantidade in esquema.items():
        jogadores_posicao = sorted(dados_cartola, key=lambda x: str(float(x['pontuacao']) if x['pontuacao'].replace('.', '').replace(',', '').isdigit() else 0, reverse=True))
        selecao.extend(jogadores_posicao[:quantidade])

    return selecao



def exibir_e_salvar_selecao(selecao, ano):
    print("Posição;Nome;URL_Foto;Pontuação;Time;URL_Escudo_Time")
    for jogador in selecao:
        print(f"{jogador['posicao']};{jogador['nome']};{jogador['url_foto']};{jogador['pontuacao']};{jogador['time']};{jogador['url_escudo_time']}")

    nome_arquivo = f"selecao_cartola_fc_{ano}.txt"
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write("posição;nome;url_foto_atleta;pontuação;time;url_escudo_time\n")
        for jogador in selecao:
            linha = f"{jogador['posicao']};{jogador['nome']};{jogador['url_foto']};{jogador['pontuacao']};{jogador['time']};{jogador['url_escudo_time']}\n"
            arquivo.write(linha)


if __name__ == "__main__":
    ano = input("Informe o ano desejado: ")

    dados_cartola = ler_arquivo_cartola(ano)

    if dados_cartola is not None:
        esquema_tatico = input("Escolha um esquema tático (4-3-3, 3-4-3, 4-4-2): ")

        selecao = selecionar_jogadores(esquema_tatico, dados_cartola)

        if selecao:
            exibir_e_salvar_selecao(selecao, ano)
