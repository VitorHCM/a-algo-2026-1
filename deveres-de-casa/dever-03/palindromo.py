import os

def checkPalindromo (lista):
    sizeLista = len(lista) # pega tamanho da lista

    if (lista[0] == lista[sizeLista - 1]): # caso primeira e ultima sejao iguais
        nextLista = lista[1:-1] # faz slice nas extremidades da lista
        if (len(nextLista) <= 2): # ponto de parada e conclusão positiva do palindromo
             return 1 # retorna 1 para a proxima funcao
        
        else: # continua recursao
            return checkPalindromo(nextLista)
        
    else: # caso as letras nao sejam iguais a palavra nao sera um palindromo
        return -1 # retorna -1 para a main

def main (lista):
    if (len(lista) <= 1): # caso lista muito pequena ( <= 1)
        print('A palavra', lista, 'possui apenas uma letra!\n')
        return
    else:
        resultado = checkPalindromo(lista)
        if(resultado == 1):
            print('A palavra', lista, 'é um palindromo!\n')
        else:
            print('A palavra', lista, 'não é um palindromo!\n')

lista = ['a','b','c','b','a'] # palindromo impar
lista1 = ['a','b','c','c','b','a'] # palindromo par
lista2 = ['a','z','c','c','b','a'] # nao palindromo par
lista12 = ['a','c','c','b','a'] # palindromo impar
lista3 = ['a'] # palavra de uma letra

os.system('clear')

main(lista)
main(lista1)
main(lista2)
main(lista12)
main(lista3)