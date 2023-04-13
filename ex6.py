'''
Inserir 100 numeros aleatório na lista
usar a função sort(lista) para ordenar
'''



import random
aux = 0
lista = []
for cont in range (0,100):
    aux = int(random.randint(0,100))
    lista.append(aux)

print(lista)
print(f" Ordenando a lista: {sorted(lista)}\n ")
