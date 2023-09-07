import random

try:
    n = int(input('digite a quantidade de números que você deseja gerar: '))
    numeros = []

    if 0 < n <= 1000000:
        for x in range(n):
            sorteio = random.randint(1, 1000000)
            numeros.append(sorteio)

        with open('lista_não_ordenada.txt', 'w') as arquivo:
            for num in numeros:
                arquivo.write(str(num) + "\n")

        print('lista foi salva no arquivo (lista_não_ordenada.txt).')

    else:
        print('digite um número inteiro válido entre 1 e 1000000.')

except ValueError:
    print('digite um número inteiro válido.')
