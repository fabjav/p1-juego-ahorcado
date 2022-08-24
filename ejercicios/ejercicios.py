
"""
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c>
y un resto <r> donde <n> y <m> son los números introducidos por el usuario,
y <c> y <r> son el cociente y el resto de la división entera respectivamente.

num1 = int(input("> "))
num2 = int(input("> "))
division = num1/num2
resto = num1%num2
print(f"resultado {division}, resto {resto}")
"""

def interMenAnu(capital,años):
    interes = capital * 0.1
    anual = interes*12
    gananciasEnAños = anual * años
    print(f"ganancias mensuales > ${interes}.")
    print(f"ganancian anuales > ${anual}")
    print(f"en {años} años > ${gananciasEnAños}")
    total = capital+gananciasEnAños
    print(f"Total con inversión inicial > ${total}")



capital = float(input("capital > $"))
años = int(input("años > "))
interMenAnu(capital,años)

