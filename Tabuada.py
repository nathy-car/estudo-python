import os 

def jogo():
    while True:
        os.system('cls')
        print("Tabuada")
        numero = int(input("Digite o número que você deseja saber a tabuada: "))
        final = int(input("Até onde você quer saber a tabuada do númrero: "))

        NumeroTabuada = 0

        while NumeroTabuada <= final:
            resultado = numero * NumeroTabuada
            print(f"{numero} x {NumeroTabuada} = {resultado}")
            NumeroTabuada += 1
        voltar = input("Aperte uma tecla para voltar: ")
jogo()