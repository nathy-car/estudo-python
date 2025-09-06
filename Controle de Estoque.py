import os

def voltar(): 
    voltar = input("Precione a tecla ENTER para voltar para o Menu")
    jogo()

def jogo():
    os.system('cls')
    print("Controle de Estoque")

    estoque = {
        "Bolacha" : 3,
        "Salgadinho" : 7,
        "Refrigerante" : 2,
        "Água" : 4
    }

    print("1 - Ver estoque")
    print("2 - Adicionar produto")
    print("3 - Atualizar quantidade")
    print("4 - Remover Produto")

    escolha = int(input("Escolha o que você quer realizar (1, 2, 3, 4): "))

    if escolha == 1:
        print(estoque)
        voltar()

    elif escolha == 2:
        produto = input("Informe o produto:")
        quantidade = int(input("Informe a quantidade:"))
        estoque[produto] = quantidade
        print(estoque)
        voltar()

    elif escolha == 3:
        produto_escolhido = input("Digite qual produto você quer atualizar: ")
        nova_quantidade = int(input("Digite a quantidade que você quer mudar"))
        estoque[produto_escolhido] = nova_quantidade
        print(estoque)
        voltar()

    elif escolha == 4:
        produto_remover = input("Digite o valor que você quer remover: ")
        del estoque[produto_remover]
        print(estoque)
        voltar()

    else:
        print("Não há essa opção")
        voltar()
jogo()