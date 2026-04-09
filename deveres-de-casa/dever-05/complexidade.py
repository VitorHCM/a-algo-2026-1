"""
dever-05
complexidade.py

=> Apresentar o cálculo de complexidade para:

    Algoritmo de ordenação Merge Sort

    
    Multiplicação de matrizes

    
    Recorrências:

        T(n) = 2T(n/4) + sqrt(n)

        T(n) = 2T(n/4) + n

        16*T(n/4) + n^2
"""

"""
=> Teorema Mestre: T(n) = aT(n/b) + cn^d
    onde:
        a = numero de subproblemas
        b = fator de divisao do problema
        n^d = custo fora das chamadas recursivas

        depois, n^d é comparado com n^(log_b a)

=> Passos para calcular complexidade:

    1 - Levar em consideração apenas repetições do código.

    2 - Verificar a complexidade das funções/métodos proprios da linguagem (se utilizado).

    3 - Ignorar as constantes e utlizar o termo de maior grau de complexidade.
"""

"""
=> Complexidade do Merge Sort:

    Merge sort possui a seguinte recorrencia:
        a = 2, ja que ele divide o vetor em dois subproblemas
        b = 2, pois o problema é sempre dividido pela metade

        Logo:
            T(n) = 2T(n/2) + n

        Que resulta em:
            log_2 2 = 1

        Assim a complexidade do Merge Sort é:
            T(n) = O(nlog n)
"""

"""
=> Complexidade da Multiplicação de Matrizes:

    Na multipliucação tradicional de duas matrizes n * n obtem-se tres loops for aninhados.

    Exemplo:
        for i
            for j
                for k
    
    Como cada loop for atribui uma complexidade de O(n), cada aninhamento multiplica-se encima da complexidade anterior.

    Assim, obtem-se: 
        T(n) = n * n * n
        
        Logo:
        T(n) = n^3
        O(n^3)
"""

"""
=> Complexidade de Recorrencias:

    => 2T(n/4) + sqrt(n)
        Equivale a: 2T(n/4) + n^1/2
            a = 2
            b = 4
            f(n) = n^(1/2)
            
        Assim, conclui-se que: O(n^1/2 * logn)



    => 2T(n/4) + n
            a = 2
            b = 4
            f(n) = n

        Conclui-se que O(n) da recorrência é: O(n)


    => 16T(n/4) + n^2
            a = 16
            b = 4
            f(n) = n^2

        Assim: O(n^2 * log n)
"""