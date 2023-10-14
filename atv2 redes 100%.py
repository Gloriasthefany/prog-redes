import os
import sys

try:
    nome_arquivo = input('Informe o nome do arquivo a ser lido: ')
    if not os.path.exists(nome_arquivo):
        print('Arquivo não encontrado.')
        sys.exit()
except Exception as e:
    print(f'Erro ao ler o nome do arquivo: {e}')
    sys.exit()

try:
    with open(nome_arquivo, 'r') as arq_input:
        lista_lida = [int(line.strip()) for line in arq_input]
    print('Arquivo lido com sucesso.')
except FileNotFoundError:
    print('Arquivo não encontrado.')
    sys.exit()
except Exception as e:
    print(f'Erro ao ler o arquivo: {e}')
    sys.exit()

print('Métodos de ordenação disponíveis: BUBBLE, INSERTION, SELECTION, QUICK')
metodo_ordena = input('Informe o método de ordenação desejado: ').upper()

if metodo_ordena not in ['BUBBLE', 'INSERTION', 'SELECTION', 'QUICK']:
    print('Método de ordenação inválido.')
    sys.exit()

if metodo_ordena == 'BUBBLE':
    n = len(lista_lida)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista_lida[j] > lista_lida[j+1]:
                lista_lida[j], lista_lida[j+1] = lista_lida[j+1], lista_lida[j]
elif metodo_ordena == 'INSERTION':
    for i in range(1, len(lista_lida)):
        chave = lista_lida[i]
        j = i - 1
        while j >= 0 and chave < lista_lida[j]:
            lista_lida[j + 1] = lista_lida[j]
            j -= 1
        lista_lida[j + 1] = chave
elif metodo_ordena == 'SELECTION':
    for i in range(len(lista_lida)):
        min_index = i
        for j in range(i+1, len(lista_lida)):
            if lista_lida[j] < lista_lida[min_index]:
                min_index = j
        lista_lida[i], lista_lida[min_index] = lista_lida[min_index], lista_lida[i]
elif metodo_ordena == 'QUICK':
    def quick_sort(lista):
        if len(lista) <= 1:
            return lista  
        elemento_pivo = lista[len(lista) // 2]  
        left = [x for x in lista if x < elemento_pivo]  
        middle = [x for x in lista if x == elemento_pivo]  
        right = [x for x in lista if x > elemento_pivo]  

        
        return quick_sort(left) + middle + quick_sort(right)

    lista_lida = quick_sort(lista_lida)

nome_arquivo_saida = f"ordenado_{nome_arquivo}"

try:
    with open(nome_arquivo_saida, 'w') as arq_output:
        for elemento in lista_lida:
            arq_output.write(f"{elemento}\n")
    print(f'Lista ordenada com sucesso. Resultado salvo em {nome_arquivo_saida}')
except Exception as e:
    print(f'Erro ao escrever no arquivo de saída: {e}')
