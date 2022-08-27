
def main():
    def salir():
        print("""
        Programa finalizado.
        
                created by Fabio Javier Flores""")
        

    import random
    import os

    palabras = ['teclado', 'mouse', 'monitor','gabinete','internet','fabio','valentina','reparadora','cuadro','jirafa']
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
        
        print(dibujo[intentos])
        
        print(f"fallos: {intentos}")
        print(g)
        '''
    def imprimirDibujo(dibujo):
        print(dibujo[intentos])
        
        print(f"fallos: {intentos}")





    while True:
        imprimirDibujo(dibujo)
        print(g)
        l = input("ingrese letra > ").lower()
        os.system("cls")
        if l == "":
            print("ingrese una letra por favor")
        else: 
        

            if l in p:
                letraSi(l)
                if g == c:
                    print("\n\t\tFelicitaciones!")
                    imprimirDibujo(dibujo)
                    print(f"'{n}' es correcto!")
                    print(" ")
                    
                    while True:
                        r1 = input("¿Jugar de nuevo? si / no > ")
                        if r1 == "si":
                            
                            main()
                        elif r1 == "no":
                            salir()
                            break
                        else: 
                            print("error")
                    
                    break


            else:
                intentos += 1
            if intentos == 6:
                print("\tGame over!")
                imprimirDibujo(dibujo)
                print(f"la palabra era: {n}")
                
                print(" ")                                
                
                while True:
                    r2 = input("¿Reintentar? si/ no >")
                    if r2 == "si":
                        
                        main()
                        
                    elif r2 == "no":
                        salir()
                        break
                    else: 
                        print("error")
                
                break
          
main()           