import time
import sys

# define um limite de recursão maior que 1000 para o algoritmo poder funcionar
# sem dar o erro de recursion limit do python
sys.setrecursionlimit(5000)

#funcao para alcular fatorial de n
def fatorial(n):
    # realiza o calculo fatorial de n utililzando recursao
    # n! = n*(n-1) * (n-2)* ... * 1
    # Ex: 4! = 4 * 3 * 2 * 1

    # caso valor de n = 1 ou 0
    if n == 0 or n == 1:
        return 1
    
    # caso nao, continua a recursao do fatorial
    else:
        return n * fatorial(n-1)


def medeTempo(listaValores):

    # realiza o fatorial de cada valor na lista dada como argumento
    # medindo o tempo de execução
    for n in listaValores:
        
        # marca tempo inicial
        inicio = time.time()

        #calcula fatorial do valor
        resultado = fatorial(n)

        fim = time.time()
        # marca tempo fim

        #calcula o tempo total de execução
        tempoExecução = fim - inicio

        print('Para N = ', n)
        print(f'Tempo de execução do algoritmo:\n{tempoExecução: .8f} segundos')
        print('----------------------------------------------------------')

valores = [10, 100, 500, 1000]

medeTempo(valores)
print('Complexidade O(n) pois o algoritmo é executado "n" vezes,\nde acordo com o numero de "n" definido.')