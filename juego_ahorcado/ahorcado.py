
from time import sleep


def main():
    
        

    import random
    import os

    palabras = ['teclado', 'mouse', 'monitor','gabinete','internet','fabio','valentina','reparadora','cuadro','jirafa']
    #n = random.choice(palabras) #selecciona una palabra al azar de la lista
    n = palabras[1]
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
    #print(dibujo[0])
    fun_guiones(n)

    #print(g)


    def letraSi(l):
        while l in p:
            ind = p.index(l) #tomar ese indice y guardarlo en ind
            g[ind]=l # se cambia el guión por la letra según el ind
            p[ind] = "0"
        #print(g)
    intentos = 0
    '''
    def letraNo(l,intentos):
        
        intentos +=1
'''
        
    def imprimirDibujo(dibujo):
        print(dibujo[intentos])
        
        print(f"fallos: {intentos}")

    def salir():
        print("""
        Programa finalizado.
        
                created by Fabio Javier Flores""")
        

    def mensajeGanador():
        print("\n\t\tFelicitaciones!")
        imprimirDibujo(dibujo)
        print(f"'{n}' es correcto!")
        print(" ")
        
        while True:
            r1 = input("¿Jugar de nuevo? si / no > ").lower()
            
            if r1 == "si":
                
                main()
                break
            elif r1 == "no":
                
                salir()
                break
            else: 
                print("error")
    def mensajePerdedor():
        print("\tGame over!")
        imprimirDibujo(dibujo)
        print(f"la palabra era: '{n}'")
        
        print(" ")  
        while True:
            r3 = input("¿Reintentar? si/ no >").lower()
            if r3 == "si":
                
                main()
                break
                
            elif r3 == "no":
                
                salir()
                break
            else: 
                print("error")
    def mensajePerdedorTotal():
        print("\tGame over!")
        
        print(f"la palabra era: '{n}'")
        
        print(" ")                               
        
        while True:
            r2 = input("¿Reintentar? si/ no >").lower()
            if r2 == "si":
                
                main()
                break
                
            elif r2 == "no":
                
                salir()
                break
            else: 
                print("error")



    #CICLO PRINCIPAL
    while True:
        imprimirDibujo(dibujo)
        print(g)
        l = input("ingrese letra > ").lower()
        os.system("cls")
        if l == "":
            print("ingrese una letra por favor")
            
        
        else: 
            aLista = list(l)
            if len(aLista) > 3:
                if aLista == c:
                    mensajeGanador()
                    break
                else:
                    os.system('cls')
                    print(dibujo[6]) 
                    print("Fallos: Totales")
                    mensajePerdedorTotal()
                    
                    break
            
                
            else:     
                if l in p:
                    letraSi(l)
                else:
                    intentos+=1
            if g == c:
                mensajeGanador()
                sleep(3)
                break
            if intentos == 6:
                mensajePerdedor()
                sleep(3)
                break
                
main()           