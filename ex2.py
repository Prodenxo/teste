"""
1 - pedir o nome, altura e o peso de 1 pessoa
2- pedir o nome, altura e o peso de outra pessoa.
4- apresente o nome da pessoa mais pesada
5- apresente o nome da pessoa mais alta.
"""
nome1 = input("Digite o nome da primeira pessoa: ")
altura1 = float(input("Digite a altura da primeira pessoa: "))
peso1 = float(input("Digite o peso da primeira pessoa: "))
nome2 = input("Digite o nome da segunda pessoa: ")
altura2 = float(input("Digite a altura da segunda pessoa: "))
peso2 = float(input("Digite o peso da segunda pessoa: "))

if(altura1 > altura2):
    print(f"O {nome1} é a pessoa mais alta.")
elif(altura2 > altura1):
    print(f"O {nome2} é a pessoa mais alta.")
if(peso1 > peso2):
    print(f"O {nome1} é a pessoa mais pesada")
elif(peso2 > peso1):
    print(f"O{nome2} é a pessoa mais pesada")
