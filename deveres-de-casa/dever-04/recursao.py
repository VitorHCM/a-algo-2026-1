# Considere a seguinte função recursiva:

# F(n) = 2F(n−1)+n2

# com o caso base F(1) = 2

# Tarefa:

# Implemente essa função em Python usando recursão.

# O programa deve solicitar ao usuário um valor de n e calcular
# F(n).

# Dicas:

# A função deve chamar a si mesma até atingir o caso base 𝐹
# (1) = 2

# A complexidade desse algoritmo é exponencial 𝑂(2𝑛), então
# evite testar valores muito grandes de 𝑛.

# Utilize a biblioteca math para calcular a fórmula fechada.

import math

def Funcao(n):
    if n == 1: #caso base da funcao
        return 2 #retorna 2 para o caso base finalizando a recursao
    else: 
        return 2 * Funcao(n-1) + n**2 #realiza a recursao

n = int(input('Entre o valor de n: '))
resultado = Funcao(n)

print("O resultado de F(", n, ") é igual a", resultado)
