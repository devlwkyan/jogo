class Jogo():
    

    def megasena():
        import random
        jogo = []

        n = int(input("Quantos jogos você quer fazer? "))

        for i in range(n):
            jogo.append(random.sample(range(1, 61), 6))
            jogo.append(" ")
        print(jogo)

    def lotofacil():
        import random
        jogo = []

        n = int(input("Quantos jogos você quer fazer? "))

        for i in range(n):
            jogo.append(random.sample(range(1, 61), 6))
            jogo.append(" ")
        print(jogo)

    x = input("Jogo da megasena ou lotofácil? ").lower()
    if x == "megasena" or x == "mega sena":
        megasena()
    if x == "lotofacil" or x == "lotofácil":
        lotofacil()
