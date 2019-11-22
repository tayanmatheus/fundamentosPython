# -*- coding: utf-8 -*-
# lacos
# repete ate ser valido
x = 1

while x < 10:
    print(x)

    x = x + 1  # somador para atribuir valor a x ou x += 1

# for

# lista

lista = [1, 2, 3, 4, 5]
lista2 = ["ola", "mundo", "!"]
lista3 = [0, "ola", "pao", 9.99, True]

# for para percorrer a lista

for i in lista:
    print(i)

for b in lista2:
    print(b)

# combinando for com range
#  range retorna uma lista

for i in range(10, 20, 2):  # contagem de 10 ate 20 imprimir de 2 em 2
    print(i)
