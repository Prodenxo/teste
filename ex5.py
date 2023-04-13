listapar = []
lista = []
listaimpar = []

for contadora in range(0, 100):
    if (contadora % 2 == 1):  ####IMPAR####
        listaimpar.append(contadora)
print(f" A soma de todos os valores dessa lista é:{sum(listaimpar)}\n ")

print(f"{listaimpar}")

print("================================================================================================================================================================================================================================================")

for contadora in range(0, 100):
    if (contadora % 2 == 0):  ####PAR####
        listapar.append(contadora)

print(f" A soma de todos os valores dessa lista é:{sum(listapar)}\n ")

print(f"{listapar}")