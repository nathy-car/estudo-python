import os 

def jogo():
    while True:
        os.system('cls')
        print("Operações")

        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        operação = input("Digite a operação que você deseja (+ , - , x , /)")

        if operação == "+":
            soma = n1 + n2
            print (f"O resultado é: {soma}")

        elif operação == "-":
            subtração = n1 - n2
            print (f"O resultado é: {subtração}")

        elif operação == "x":
            multiplicação = n1 * n2
            print (f"O resultado é: {multiplicação}")

        elif operação == "/":
            divisão = n1 / n2
            print (f"O resultado é: {divisão}")

        else: 
            print("Não existe essa operação")
            voltar = input("Aperte uma tecla para voltar no começo")

os.system('cls')
jogo()