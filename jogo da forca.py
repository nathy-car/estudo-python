import os
import random

def jogo():
    print("Jogo da Forca")
    palavras = ["camelo", "python"]
    palavraEscolhida = random.choice(palavras)
    progresso = ["_"] * len(palavraEscolhida)

    while True:

        letra = input("Digite uma letra: ")
            
        if letra in palavraEscolhida:
            for i, l in enumerate (palavraEscolhida):
                if l == letra:
                    progresso[i] = letra
                print("")