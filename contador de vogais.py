import os 

def jogo():
    while True:
        os.system('cls')
        print("Contador de vogais")

        palavra = input("Digite uma palavra: ").lower()
        vogais = ["a", "e", "i", "o", "u"]
        VogaisPresentes = []

        for x in palavra:
            if x in vogais and x not in VogaisPresentes:
                VogaisPresentes.append(x)

        print(f"As vogais são {VogaisPresentes} e há o total de {len(VogaisPresentes)} vogais")
        voltar = input("Aperte qualquer tecla para voltar")

jogo()