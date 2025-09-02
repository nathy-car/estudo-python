nomes = ["Ana", "João"]     #criar as informações
idade = [10, 20]            #criar as informações

nome_e_idade = {} #criar o dicionário para juntar as informações

adicionar = input("Qual o nome e idade que você deseja cadastrar: ")

lista = adicionar.split()

for x in lista:
    nomes.append(lista[0])
    idade.append(lista[1])

for i, nome in enumerate(nomes):  #irá buscar o índice e o nome na lista "nomes" com o enumerate
    nome_e_idade[nome] = idade[i] #no dicionário, a chave será o nome (que esta na lista "nomes") e o valor será a idade que possui o mesmo índice que o nome
    

print("O dicionário ficou assim:")
print(nome_e_idade)