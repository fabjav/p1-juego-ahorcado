import random
import os

palabras = ['teclado', 'mouse', 'monitor','gabinete','internet']
n = random.choice(palabras) #selecciona una palabra al azar de la lista
print(n)


dibujo = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

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
    
    while True:
        if l in p: #si l ingresada está en palabra_lista
            ind = p.index(l) #tomar ese indice y guardarlo en ind
            g[ind]=l # se cambia el guión por la letra según el ind
            p[ind] = "0"
                    
        else:
            
            break
    print(g)

while True:
    fun_letra(input(">"))
    
    
