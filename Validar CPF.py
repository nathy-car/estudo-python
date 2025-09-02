import os

def jogo(): 
    while True:
        os.system('cls')
        print("Validar CPF")
        cpf = input("Digite seu CPF (só número): ")
        cpfarrumado = cpf.strip(".", "-")

        if len(cpfarrumado) == 11:
            print("Está correto")
        else:
            print("CPF inválido")
            
        voltar = input("Aperte enter para voltar")
jogo()