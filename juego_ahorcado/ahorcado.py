

import random
import os

palabras = ['teclado', 'mouse', 'monitor','gabinete','internet']
n = random.choice(palabras) #selecciona una palabra al azar de la lista
#print(n)


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
    comparacion = []
    for i in n:
        guiones.append("_")
    for i in n:
        palabra_lista.append(i)
    for i in n:
        comparacion.append(i)
        

    
    return guiones,palabra_lista,comparacion
    

g,p,c = fun_guiones(n)

os.system("cls")
fun_guiones(n)

print(g)


def letraSi(l):
    while l in p:
        ind = p.index(l) #tomar ese indice y guardarlo en ind
        g[ind]=l # se cambia el guión por la letra según el ind
        p[ind] = "0"
    print(g)
intentos = 1
def letraNo(l,intentos):
    
    print(dibujo[intentos])
    
    print(f"fallos: {intentos}")
    print(g)




while True:
    
    l = input("ingrese letra > ").lower()
    os.system("cls")
    if l in p:
        letraSi(l)
        if g == c:
            print("Felicitaciones!")
            break
    else:
        letraNo(l,intentos)
        intentos += 1
    if intentos == 7:
        print("\tGame over!")
        print(" ")
        respuesta = input("reintentar? si/no > ")
        if respuesta == "no":
            print("""
            programa finalizado

            
            \t\tby Fabio Javier Flores""")
            break
        elif respuesta == "si":
            
            
                
                

    
    
