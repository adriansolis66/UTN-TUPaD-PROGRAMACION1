#1) Crear una lista con las notas de 10 estudiantes. 
#• Mostrar la lista completa. 
#• Calcular y mostrar el promedio. 
#• Indicar la nota más alta y la más baja.
notas = [8,7,8,9,6,10,3,5,7,10]
print(f"las notas de los estudiantes son {notas}")

suma = 0

for i in notas:
  suma = suma + i
   
promedio = suma/len(notas)

print(f"el promedio es: {promedio}")

mayor = notas [0]
menor = notas[0]

for i in notas:
    if i > mayor:
      i = mayor
      if i < menor:
       menor = i

print(f"el numero mayor es: {mayor}")
print(f"el numero menor es: {menor}")


#2) Pedir al usuario que cargue 5 productos en una lista. 
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = ["","","","",""]
productos[0] = input("ingrese un producto: ")
productos[1] = input("ingrese un producto: ")
productos[2] = input("ingrese un producto: ")
productos[3] = input("ingrese un producto: ")
productos[4] = input("ingrese un producto: ")



print(f"los produtos son: {productos}")

productos_ordenados = sorted(productos)

print(f"los productos ordenados alfabeticamente: {productos_ordenados}")

remover_producto = input("que producto desea eliminar: ")

if remover_producto in productos:
   productos.remove(remover_producto)
   print(f"la lista de productos actualizada es: {productos}")

#3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
#• Crear una lista con los pares y otra con los impares. 
#• Mostrar cuántos números tiene cada lista.

from random import randint

numeros = [randint(1,100) for i in range(1,16)]

print(numeros)

pares = []

for i in numeros:
   if i % 2 == 0:
    pares.append(i)

print(len(pares))

impares = []

for i in numeros:
   if i % 2 != 0:
     impares.append(i)

print(len(impares))

#4) Dada una lista con valores repetidos: 
#datos = [1,3,5,3,7,1,9,5,3]
#• Crear una nueva lista sin elementos repetidos. 
#• Mostrar el resultado. 

datos = [1,3,5,3,7,1,9,5,3]

repetidos = []

for i in datos:
  if i not in repetidos:
    repetidos.append(i)

print(f"lista original: {datos}")    
print(f"los datos sin numeros repetidos es: {repetidos}")


#5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
#• Mostrar la lista final actualizada. 

lista_nombres = ["juan","mariano","pedro","martin","ariel"]

print(f"esta es la lista de estudiantes: {lista_nombres}")

actualizar = input("deseas eliminar o agregar a alguien: ")

if actualizar == "agregar":
  lista_nombres.append(input("ingresa el nuevo estudiante: "))
  print(lista_nombres)
elif actualizar == "eliminar":
  lista_nombres.remove(input("elije el estudiante que quieres eliminar: "))
  print(lista_nombres)
else:
  print("la opcion no es valida")

#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
#último pasa a ser el primero).

lista = [1,2,3,4,5,6,7]

rotacion = lista [-1:] + lista [:-1]

print(rotacion)


#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
#semana. 
#• Calcular el promedio de las mínimas y el de las máximas. 
#• Mostrar en qué día se registró la mayor amplitud térmica.

matriz = [
    [13, 24], #lunes
    [15, 24], #martes    
    [19, 26], #miercoles  
    [17, 28], #jueves  
    [9, 21],  #viernes 
    [8, 18],  #sabado
    [11, 22] #domingo    
                            
          ]

print(matriz)

minima = 0
maxima = 0

for dias in matriz:
    minima += dias[0]
    maxima += dias[1]

calc_minima = int(minima / len(matriz))
cal_maxima = int(maxima / len(matriz))

print(f"el promedio de las temperaturas minimas es: {calc_minima}")
print(f"el promedio de las temperaturas maxima es: {cal_maxima}")

amplitud_dia = 0
mayor_dia = 0

for i in range(len(matriz)):
    min = matriz [i] [0]
    max = matriz [i] [1]
    amplitud = max - min
    if amplitud > amplitud_dia:
        amplitud_dia = amplitud
        mayor_dia = i + 1

print(f"el dia que mas amplitud tuvo fue el dia {mayor_dia} con amplitud {amplitud_dia}")



#8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
#• Mostrar el promedio de cada estudiante. 
#• Mostrar el promedio de cada materia. 

notas = [
         
         [5, 6, 8],
         [10, 5, 9],
         [7, 2, 7],
         [4, 9, 6],
         [3, 7, 9]

         ]


for i in range(len(notas)):
    suma = 0
    for j in range(len(notas[i])):
        suma += notas[i][j]
    promedio = suma / len(notas[i])
    print(f"los promedio son estudiante: {i+1} : {promedio:.2f}")


estudiantes = len(notas)
num_materias = len(notas[0])

for i in range(num_materias):
    suma = 0
    for j in range(estudiantes):
        suma += notas [j][i]
    promedio = suma / estudiantes
    print(f"materia {i+1} promedio: {promedio:.2f}")
  

#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
#• Inicializarlo con guiones "-" representando casillas vacías. 
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
#• Mostrar el tablero después de cada jugada. 






#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
#• Mostrar el total vendido por cada producto. 
#• Mostrar el día con mayores ventas totales. 
#• Indicar cuál fue el producto más vendido en la semana.

ventas = [
    [5, 8, 6, 7, 3, 4, 9],   # Producto 1
    [2, 4, 3, 6, 8, 5, 7],   # Producto 2
    [9, 7, 5, 6, 4, 3, 8],   # Producto 3
    [3, 6, 2, 4, 7, 9, 5]    # Producto 4
]


print("Total por producto:")
for i in range(4):
    total = 0
    for j in range(7):
        total = total + ventas[i][j]
    print("Producto", i+1, "vendió", total, "unidades")


mayor_dia = -1
mayor_total = -1
for j in range(7):
    suma_dia = 0
    for i in range(4):
        suma_dia = suma_dia + ventas[i][j]
    if suma_dia > mayor_total:
        mayor_total = suma_dia
        mayor_dia = j
print("El día con mayores ventas fue el día", mayor_dia+1, "con", mayor_total, "unidades")

mayor_producto = -1
max_ventas = -1
for i in range(4):
    total = 0
    for j in range(7):
        total = total + ventas[i][j]
    if total > max_ventas:
        max_ventas = total
        mayor_producto = i
print("El producto más vendido en la semana fue el Producto", mayor_producto+1, "con", max_ventas, "unidades")