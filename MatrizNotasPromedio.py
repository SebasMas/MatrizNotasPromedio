import numpy as np

#Determinamos el tamaño de la matriz
t=4

#Creamos la matriz <notas> vacía
notas = np.empty((t), dtype = float)

#Creamos un ciclo que se ejecute tantas veces como posiciones tenga la matriz <notas>
for i in range(len(notas)):
    #Establecemos que cada posición en notas[i] sea igual a la nota  que ingrese el usuario
    notas[i] = float(input(f"Ingrese la nota {i+1} :"))

print("Listado de notas")

#Establemos que el promedio empiece en 0
prom=0

#Creamos un ciclo que recorra cada índice
for i in range(len(notas)):
   print("Nota",(i+1),": ", notas[i])
   prom+= notas[i]
prom= prom/t

if prom > 3:
    print(f"Su promedio es {prom}, felicidades!")
else:
    print(f"Su promedio es {prom}, suerte la próxima!")

