import os 

def jogo ():
    while True:
        os.system('cls')
        print ("Palíndromo")

        palavra = input("Digite uma palavra: ").lower()

        if palavra == palavra[::-1]:
            print ("É um palindromo")
        else: 
            print("Não é um palindromo")
        voltar = input("Aperte qualquer tecla para voltar")

jogo()
