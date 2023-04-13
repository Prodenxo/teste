'''
1- Receber 20 numeros inteiros
2- determinar qual é o menor número
3- determinar qual é o maior número
4- mostrar os dois.

'''
import random
aux = 0
lista = []


for cont in range (0,400):
    aux = int(random.randint(15,400))
    lista.append(aux)

print ('O maior número da lista é: ',max(lista))
print ('O maior número da lista é: ',min(lista))
print(lista)

