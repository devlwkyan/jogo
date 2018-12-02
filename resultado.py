

class Jogo():

    def megasena():
        jogo = []
        print("Pressione ENTER a cada número digitado")
        print("\n PRIMEIRO ENTRE OS NÚMEROS QUE VOCÊ JOGOU\n")
        for i in range(6):
            jogo.append(int(input("Digite número: ")))

        print("Confira os números, se estiveres correto digite: S, caso contrário digite: N, e iremos recomeçar: \n")
        print(jogo)
        test = input(
            "Está certo? Se sim, digite S, caso contrário, digite N: ").lower()

        while test != "s":
            print("Pressione ENTER a cada número digitado")
            jogo1 = []
            for i in range(6):
                jogo1.append(int(input("Digite número: ")))
            print(jogo1)
            test = input(
                "Está certo? Se sim, digite S, caso contrário, digite N: ").lower()

        """Números da megase"""

        print("\n AGORA ENTRE O RESULTADO DA MEGASENA\n")
        megasena = []
        for j in range(6):
            megasena.append(int(input("Digite número:")))

        print("Confira os números, se estiveres correto digite: S, caso contrário digite: não, e iremos recomeçar: \n")
        print(megasena)
        test = input(
            "Está certo? Se sim, digite S, caso contrário, digite N: ").lower()

        while test != "s":
            print("Pressionel ENTER a cada número digitado")
            megasena1 = []
            for i in range(6):
                megasena1.append(int(input("Digite número: ")))
            print(megasena1)
            test = input(
                "\n\nEstá certo? Se sim, digite OK, caso contrário, digite N: ").lower()

        """RESULTADO"""

        result = []
        for num in megasena:
            if num in jogo:
                result.append(num)

        print("\n\nVocê acertou: {}, números. \nOs números que você acertou foram:{}\n".format(
            len(result), result))



        """*********************** LOTOFÁCIL **************************"""

    def lotofacil():
            """Entrada dos números jogados"""

            jogo = []
            print("Pressione ENTER a cada número digitado")
            print("\n PRIMEIRO ENTRE OS NÚMEROS QUE VOCÊ JOGOU\n")
            for i in range(15):
                jogo.append(int(input("Digite número: ")))

            print("Confira os números, se estiveres correto digite: S, caso contrário digite: N, e iremos recomeçar: \n")
            print(jogo)
            test = input(
                "Está certo? Se sim, digite S, caso contrário, digite N: ").lower()

            while test != "s":
                print("Pressione ENTER a cada número digitado")
                jogo = []
                for i in range(15):
                    jogo.append(int(input("Digite número: ")))
                print(jogo)
                test = input(
                    "Está certo? Se sim, digite S, caso contrário, digite N: ").lower()

            """Números da lotofácil"""

            print("\n AGORA ENTRE O RESULTADO DA LOTOFÁCIL\n")
            lotofacil = []
            for j in range(15):
                lotofacil.append(int(input("Digite número:")))

            print("Confira os números, se estiveres correto digite: S, caso contrário digite: não, e iremos recomeçar: \n")
            print(lotofacil)
            test = input(
                "Está certo? Se sim, digite S, caso contrário, digite N: ").lower()

            while test != "s":
                print("Pressionel ENTER a cada número digitado")
                lotofacil = []
                for i in range(15):
                    lotofacil.append(int(input("Digite número: ")))
                print(lotofacil)
                test = input(
                    "\n\nEstá certo? Se sim, digite OK, caso contrário, digite N: ").lower()

            """RESULTADO"""

            result = []
            for num in lotofacil:
                if num in jogo:
                    result.append(num)

            print("\n\nVocê acertou: {}, números. \nOs números que você acertou foram:{}\n".format(
                len(result), result))

    x = str(input("Megasena ou Lotofácil? "))
    if x == "megasena" or x == "Mega Sena":
        megasena()
    if x == "lotofacil" or x == "lotofácil":
        lotofacil()
