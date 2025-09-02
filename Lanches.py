import os


def jogo():
    os.system('cls')
    print("Máquina de lanches")

    lanches = {
        "Hamburguer" : 10.00,
        "Coxinha" : 7.00,
        "Enroladinho" : 6.00,
        "Refrigerante" : 9.00
    }

    total = 0

    while True:
        print(lanches)
        lanche_escolhido = input("Quais lanches você quer ('sair' para finalizar): ").capitalize()

        if lanche_escolhido.lower() == "sair":
            break
        elif lanche_escolhido in lanches:
            total += lanches[lanche_escolhido]
            print(f"O total é R${total}")
        else:
            print("Não tem esse lanche")

    print(f"O total é R${total}")

jogo()
