import random
import matplotlib.pyplot as plt

#Función que simulara la caida de las canicas
def simular_canicas(numero_canicas, numero_niveles):
#Se creara una lista para contar la cantidad de canicas en cada contenedor
    resultados = [0] * (numero_niveles + 1)
    for _ in range(numero_canicas):
        posicion = 0 
# Se simulara la caida de cada canica mediante los niveles
        for _ in range(numero_niveles):
# Decidir aleatoriamente si la canica cae a la izquierda o derecha
            if random.random() < 0.5:
                posicion += 1
#Incrementar el conteo en la posición final de la canica
        resultados[posicion] += 1
    return resultados

#Función para graficar el histograma de los resultados
def graficar_histograma(resultados):
    plt.bar(range(len(resultados)),resultados, color="#89CFF0") 
    plt.xlabel("Distibución de canicas") #Nombre del eje x
    plt.ylabel("Cantidad de canicas") #Nombre del eje y
    plt.title("Simulacion de Maquina Galton") #Titulo del grafico
    plt.show() #Mostrar el grafico

#Simulación de 3000 canicas en 12 niveles
numero_canicas = 3000
numero_niveles = 12
resultados = simular_canicas(numero_canicas, numero_niveles)
graficar_histograma(resultados)