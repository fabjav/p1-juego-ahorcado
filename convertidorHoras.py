Tiempos = { }
while True:
    minutos = int(input("min > "))
    segundos = int(input("seg > "))
    if 0<minutos<60 and 0<segundos<60:
        Tiempos[minutos]=segundos
    elif minutos == 111 or segundos == 111:
        break
    else:
        print("error 506.")
print(Tiempos)


