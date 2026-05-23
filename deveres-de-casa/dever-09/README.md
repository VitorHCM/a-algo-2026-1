# Dever de casa: PRIM II

Supondo que desejamos interligar 6 polos tecnológicos (Cidades A, B, C, D, E e F)
com uma rede de alta velocidade de fibra óptica, o custo do cabo de fibra óptica é
extremamente alto, cobrado por quilômetro. O objetivo do projeto é garantir que
todas as cidades estejam conectadas à mesma rede com o menor custo possível
de construção.

Escreva um código em Python que implemente o Algoritmo de Prim para a
situação demonstrada acima, tendo como referência a relação de distância entre
os pólos tecnológicos a seguir: 

    A   B   C   D   E   F
A   0   4   4
B           2   5   
C               5   6
D                       4
E                       2

A-->B: 4 Km A-->C: 4Km B-->C: 2Km B-->D: 5Km
C-->D: 5Km C-->E: 6Km D-->E: 3Km D-->F: 4kM E-->F: 2Km


O programa deve imprimir a rota dos
cabos a serem instalados (em ordem) e a
quantidade total mínima de quilômetros
de cabos utilizados.
