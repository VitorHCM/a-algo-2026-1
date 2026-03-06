import time
import random

def criaArray(size):
    array = [random.randint(0,100) for i in range(size)]
    # print(array)
    return array

def insertionSort(array):
    
    arrLen = len(array)
    for n in range(1, arrLen): # for i in range(start, stop, step)
        
        # print ('index [', n, '] first      ', array)

        if array[n-1] > array [n]:
            # print('-> 1: swap ', array[n], ' with ', array[n-1] )
            aux = array[n]
            array[n] = array[n-1]
            array[n-1] = aux

            # print ('index [', n, '] first swap ', array)

            for i in range(n-1, 0, -1): 
                

                if array[i] < array [i-1]: 

                    # print('-> 2: swap ', array[i], ' with ', array[i-1] )

                    aux = array[i]
                    array[i] = array[i-1]
                    array[i-1] = aux

                    # print ('index [', n, '] second swap', array)

            # print('-> finish')

        # else: continua o primeiro for 
    return array
            
def medeTime(array):

    startO2 = time.time()
    sortedArrayO2 = insertionSort(array)
    endO2 = time.time()

    startNLogN = time.time()
    sortedArrayNLogN = sorted(array)
    endNLogN = time.time()

    arraySize = len(array)
    print('\nArray de tamanho', arraySize)
    print('\nSorted com 02\ntime to run:', endO2 - startO2, 'segundos')
    print('\nSorted com n Log n\ntime to run:', endNLogN - startNLogN, 'segundos')

array1k = criaArray(1000)
array5k = criaArray(5000) 
array10k = criaArray(10000)
array20k = criaArray(20000)
array50k = criaArray(50000)

medeTime(array1k)
medeTime(array5k)
medeTime(array10k)
medeTime(array20k)
medeTime(array50k)


