import random
import sys
import os

dir_atual = os.path.dirname(os.path.abspath(__file__))
nomearquivo = dir_atual + '\\valores_nao_ordenados.txt'

def gerar_lista(quantidade, valor_min, valor_max):
    try:
        if valor_min > valor_max:
            raise ValueError("O valor mínimo não pode ser maior que o valor máximo.")
        lstValores = [random.randint(valor_min, valor_max) for _ in range(quantidade)]
        return True, lstValores
    except ValueError as ve:
        return False, str(ve)
    except Exception as e:
        return False, str(e)

def salvar_lista(nome_lista, nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as arq_output:
            for valor in nome_lista:
                arq_output.write(f'{valor}\n')
        return True
    except FileNotFoundError:
        return False, "O arquivo não foi encontrado."
    except Exception as e:
        return False, str(e)

def main():
    try:
        n = int(input('Informe a quantidade de elementos da lista: '))
        valor_minimo = int(input('Informe o valor mínimo: '))
        valor_maximo = int(input('Informe o valor máximo: '))
    except ValueError:
        print('\nERRO: O valor informado não é um inteiro\n')
        sys.exit()

    if n <= 0:
        print(f'\nInforme um valor inteiro positivo para a quantidade de elementos da lista\n')
        sys.exit()

    lista_gerada, lstValores = gerar_lista(n, valor_minimo, valor_maximo)
    
    if lista_gerada:
        nome_arquivo = 'valores_nao_ordenados.txt'
        resultado, mensagem = salvar_lista(lstValores, nome_arquivo)
        if resultado:
            print(f'Lista gerada e salva com sucesso no arquivo {nome_arquivo}')
        else:
            print(f'Erro ao salvar a lista no arquivo: {mensagem}')

if __name__ == "__main__":
    main()
