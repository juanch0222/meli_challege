#Pemite ocupar el modulo "random" para poner las minas de manera aleatoria
import random
#Usuario indica el tamaño de la matriz
fila = int(input("Ingresa el número de filas: "))
columna = int(input("Ingresa el número de columnas: "))
minas = int(input("Ingresa el número de minas: "))
#Se evalua que las minas no sean mas que las casillas
if minas > fila*columna:
    print("Error: El número de minas es mayor que el número de casillas.")
elif minas <= 0:
    print("Error: El número de minas es menor o igual a 0.")
else:
    #Si todo, se crea la matriz
    matriz = [[0 for i in range(columna)] for j in range(fila)]

#Poner las minas de manera aleatoria, ocupando la variable minas_colocadas para controlar el numero de minas
minas_colocadas = 0
while minas_colocadas < minas:
    #Se elige una fila y una columna al azar
    f = random.randint(0, fila-1)    
    c = random.randint(0, columna-1)   
    # Solo coloca una mina si la celda está vacía
    if matriz[f][c] == 0:
        matriz[f][c] = 9
        minas_colocadas += 1


f = 0 #Variable para recorrer la matriz, para filas
c = 0 #Variable para recorrer la matriz, para columnas

#Se evalua la cantidad de minas adyacentes
for f in range(fila):      # recorre cada fila
    for c in range(columna):  # recorre cada columna
        if matriz[f][c] == 9: continue
        else:
            minas_adyacentes = 0
            if f-1 >= 0 and c-1 >= 0 and matriz[f-1][c-1] == 9: minas_adyacentes+=1 #Evalua la mina adyacente superior izquierda
            if f-1 >= 0 and c >= 0 and matriz[f-1][c] == 9: minas_adyacentes+=1 #Evalua la mina adyacente superior
            if f-1 >= 0 and c+1 < columna and matriz[f-1][c+1] == 9: minas_adyacentes+=1 #Evalua la mina adyacente superior derecha
            if f >= 0 and c-1 >= 0 and matriz[f][c-1] == 9: minas_adyacentes+=1 #Evalua la mina adyacente izquierda
            if f >= 0 and c+1 < columna and matriz[f][c+1] == 9: minas_adyacentes+=1 #Evalua la mina adyacente derecha
            if f+1 < fila and c-1 >= 0 and matriz[f+1][c-1] == 9: minas_adyacentes+=1 #Evalua la mina adyacente inferior izquierda
            if f+1 < fila and c >= 0 and matriz[f+1][c] == 9: minas_adyacentes+=1 #Evalua la mina adyacente inferior
            if f+1 < fila and c+1 < columna and matriz[f+1][c+1] == 9: minas_adyacentes+=1 #Evalua la mina adyacente inferior derecha
            matriz[f][c] = minas_adyacentes
#Se imprime la matriz
for fila in matriz:
    print(fila)


            
