minutos = []
segundos = []
while True:
    min = int(input("min > "))
    seg = int(input("seg > "))
    if 0<min<60 and 0<seg<60:
        minutos.append(min)
        segundos.append(seg)
    else:
        break

    print(minutos)
    print(segundos)

def sc_min(minutos):
    suma_mins = 0
    for i in minutos:
        suma_mins = suma_mins + i
    min_hora = suma_mins/60
    print(min_hora)

def sc_seg(segundos):
    suma_segs = 0
    for i in segundos:
        suma_segs = suma_segs + i
    seg_Min = suma_segs/60
    print(seg_Min)



opción = input("> ").lower()
if opción == "mostrar":

