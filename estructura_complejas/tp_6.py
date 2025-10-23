#1) Dado el diccionario precios_frutas 
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
#1450} 
#Añadir las siguientes frutas con sus respectivos precios: 
#● Naranja = 1200 
#● Manzana = 1500 
#● Pera = 2300 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

print(precios_frutas)

precios_frutas ['Naranja'] = 1200
precios_frutas ['Manzana'] = 1500
precios_frutas ['Pera'] = 2300

print(precios_frutas)


#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
#● Banana = 1330 
#● Manzana = 1700 
#● Melón = 2800

precios_frutas ['Banana'] = 1330
precios_frutas ['Manzana'] = 1700
precios_frutas ['Melón'] = 2800

print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
#precios.

lista_frutas = list(precios_frutas.keys())

print(lista_frutas)


#4) Escribí un programa que permita almacenar y consultar números telefónicos. 
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

telefono = {}


for i in range(5):
    nombre = input("ingresa el nombre de contacto: ")
    numero = input("ingresa el numero de contacto: ")
    telefono[nombre] = numero

consulta_nombre = input("ingresa el nombre para ver si esta en la agenda: ")

if consulta_nombre in telefono:
    print(f"el usuario {consulta_nombre} esta en la agenda")

else:
    print("no se encuentra en la agenda.")

#5) Solicita al usuario una frase e imprime: 
#• Las palabras únicas (usando un set). 
#• Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("ingrese una frase: ")

dividir_frase = frase.split()

print(dividir_frase)

palabras_unicas = set(dividir_frase)

print(palabras_unicas)

conteo = {}

for i in dividir_frase:
    if i in conteo:
        conteo[i] += 1
    else:
        conteo[i] = 1

print(f"cantidad de palabras es {conteo}")

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
#Luego, mostrá el promedio de cada alumno.

alumnos = {}

for _ in range(3):
    nombres = input("ingrese el nombre del alumno: ")
    notas = []
    for i in range(3):
        nota = float(input(f"ingrese la nota: {i+1} al nombre: {nombres}: "))
        notas.append(nota)

    alumnos[nombres] = tuple(notas) 

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"el alumno {alumno} tiene promedio {promedio:.2f}")

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
#y Parcial 2: 
#• Mostrá los que aprobaron ambos parciales. 
#• Mostrá los que aprobaron solo uno de los dos. 
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 

parcial_uno = {1, 3, 4, 5, 7}
parcial_dos = {2, 5, 6, 8, 10}

ambos = parcial_uno & parcial_dos
solo_uno = parcial_uno ^ parcial_dos
almenos_uno = parcial_uno | parcial_dos

print(f"los que aprobaron ambos parciales {ambos}")
print(f"los que aprobaron un parcial {solo_uno}")
print(f"los que aprobaron al menos un parcial {almenos_uno}")


#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
#Permití al usuario: 
#• Consultar el stock de un producto ingresado. 
#• Agregar unidades al stock si el producto ya existe. 
#• Agregar un nuevo producto si no existe.

productos = {
    "yerba":3,
    "azucar":5,
    "galletitas": 6
}

producto = input("ingrese el producto que quiere consultar: ").strip().lower()

if producto in productos:
    print(f"el producto {producto} tiene un stock de {productos[producto]} unidades")
    nuevo_stock = int(input("ingrese un nuevo valor: "))
    productos[producto] += nuevo_stock
    print(f"el nuevo stock de {producto} es {productos[producto]}")
else:
    nuevo_producto = int(input("ingresa el stock del nuevo producto: "))
    productos[producto] = nuevo_producto
    print(f"el nuevo stock es: {productos}")

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

agenda = {
    ("lunes" , "13:30"): "medico",
    ("miercoles" , "14:50"): "gimnasio",
    ("viernes" , "11:00"): "reunion"
}

dia = input("ingresa el dia a consultar: ").strip().lower()
hora = input("ingresa la hora de la reunion: ")

clave = (dia, hora)

if clave in agenda:
    print(f"el dia y hora tiene el evento {agenda[clave]}")
else:
    print("no hay eventos.")


#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
#diccionario donde: 
#• Las capitales sean las claves. 
#• Los países sean los valores. 

paises_capitales = {
    "argentina":"buenos aires",
    "paraguay":"asuncion",
    "colombia":"bogota"
}


capitales_paises = {}

for paises, capitales in paises_capitales.items():
    capitales_paises[capitales] = paises
    
print(f"diccionario viejo {paises_capitales}")
print(f"diccionario nuevo {capitales_paises}")