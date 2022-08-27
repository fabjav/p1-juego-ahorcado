import random
import os

palabras = ['teclado', 'mouse', 'monitor','gabinete','internet']
n = random.choice(palabras) #selecciona una palabra al azar de la lista
print(n)


def fun_guiones(n):
    palabra_lista = []
    guiones = []
    for i in n:
        guiones.append("_")
    for i in n:
        palabra_lista.append(i)
    return guiones,palabra_lista

g,p = fun_guiones(n)

fun_guiones(n)
print(g)

def fun_letra(l): #se pide una letra al usuario
    if l in p:
        ind = p.index(l)
        g[ind]=l
        print(g)
        p.remove(l)
        print(p)
    else:
        print("no")
while True:
    fun_letra(input(">"))
    fun_guiones(n)
    
