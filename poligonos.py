#JOSE MARTINEZ HERNANDEZ 31/05/2021
import math
import matplotlib
import matplotlib.pyplot as plt
from bresenham import bresenham
matriz = []
fig = plt.figure()
ax = fig.add_subplot(111)

def llenadoMatriz(aristas, centro, punto0):  
    agr=0
    mayor=0
    menor=7
    x1, y1 = centro
    x2, y2 = punto0 
    for i in range(aristas):
        matriz.append([])
        print(math.degrees(agr))
        for j in range(2): 
            if j == 0:
                valor = round((x1+math.cos(agr)*(x2 - x1)-math.sin(agr) * (y2 - y1)))
                matriz[i].append(valor)
            else: 
                valor = round((y1 + math.sin(agr) * (x2 - y1) + math.cos(agr)  * (y2 - y1)))
                matriz[i].append(valor)
        agr += math.radians(360/aristas)

def llenadoMatriz2():  
    mayor=0
    menor=7
    for i in range(aristas):  
        matriz.append([])
        for j in range(2):
            valor = int(input("Ingresa coordenadas del punto {}: ".format(i+1)))
            if valor > mayor:
                mayor= valor+2
            if valor < menor:
                menor= valor-2
            matriz[i].append(valor)
            print(i,"   ", j) 
    plt.xlim([menor, mayor])
    plt.ylim([menor, mayor])

def rotacion_punto(origen, punto, angulo):
    x1, y1 = origen
    x2, y2 = punto
    xr = round((x1 + math.cos(angulo) * (x2 - x1) - math.sin(angulo) * (y2 - y1)), 2)
    yr = round((y1 + math.sin(angulo) * (x2 - y1) + math.cos(angulo) * (y2 - y1)) ,2)
    
    return xr, yr

def graficacion(aristas):
    resultado=[]
    for f in range(aristas):
        if f == aristas-1:
            valores = list(bresenham(matriz[f][0], matriz[f][1], matriz[0][0], matriz[0][1]))
            resultado+=valores

        else:
            valores = list(bresenham(matriz[f][0], matriz[f][1], matriz[f+1][0], matriz[f+1][1]))
            resultado+=valores
            
    for i in resultado:
        rect1 = matplotlib.patches.Rectangle((i),1, 1,linewidth=1, edgecolor='b', facecolor='none')
        ax.add_patch(rect1)


if __name__ == "__main__": 
    aristas = int(input("Ingresa los lados de tu figura: "))
    x1 = int(input("Ingresa x1 del centro de tu figura: "))
    y1 = int(input("Ingresa y1 del centro de tu figura: "))
    l = int(input("Ingresa el tamaño de tus lados: "))
    punto0= (x1+l, y1)
    origen = (x1, y1)
    llenadoMatriz(aristas, origen, punto0)
    graficacion(aristas)
    #rotacion_punto(origen, punto, math.radians(270
    print(matriz)
    plt.xlim([-10, 10])
    plt.ylim([-10, 10])
    plt.show()
