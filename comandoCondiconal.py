# -*- coding: utf-8 -*-

x = 1
y = 11111111

if x > y:
    print("x e maior que y")
else:
    print("x nao e maior que y")

# comando com mais de uma condicao o comando elif

b = 1
c = 2
# sempre executa a primeira condicao verdadeira
if b == c:
    print("numeros iguais")
elif c > b:  # primeira condicao verdadeira
    print("c maior que b")
else:
    print("numeros diferentes")
