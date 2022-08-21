listMin = []
listSeg = []
sumaSeg = 0
sumaMin = 0


def convMin(min):
    listMin.append(min)
    for i in listMin:
        sumaSeg = sumaSeg + i

def convSeg(seg):
     listSeg.append(seg)
     for i in listSeg:
         sumaMin = sumaMin + i

while True: #corre el programa
    min = int(input("min > "))
    if min <60 and min>0:
        convMin(min)
    elif min == 111:
        break

    else:
        print("error 404.")

    seg = int(input("seg > "))
    if seg <60 and seg>0:
        convSeg(seg)
    elif seg == 111:
        break

    else:
        print("error 404.")
    print("ingrese un 111 para terminar")