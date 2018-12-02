import random

x = input("Jogo da megasena ou lotofácil? ").lower()

if x == "megasena":
    jogo = []
    
    n = int(input("Quantos jogos você quer fazer? "))

    for i in range(n):
        jogo.append(random.sample(range(1, 61), 6))
        jogo.append(" ")
    print(jogo)

    
if x == "lotofacil" or x == "lotofácil":
    jogo = []
    n = int(input("Quantos jogos você quer fazer? "))

    for i in range(n):
        jogo.append(random.sample(range(1, 26), 15))
        jogo.append(" ")
    print(jogo)