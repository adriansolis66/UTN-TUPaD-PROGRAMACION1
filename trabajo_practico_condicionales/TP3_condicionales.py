#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("ingrese su edad:\n"))

if edad > 18:
    print("es mayor de edad")



#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
# mensaje “Desaprobado”.

nota = int(input("ingrese la nota recibida:\n"))

if nota >= 6:
    print("aprobado")
else:
    print("desaprobado")


#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
# operador de módulo (%) en Python para evaluar si un número es par o impar. 

numero = int(input("ingrese un numero:\n"))

if numero % 2 == 0: #el numero ingresado se divide por 2 si el resto es 0 es par
    print("ha ingresado un numero par")
else: #sino da false y pide que ingrese un numero par
    print("por favor, ingrese un numero par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
#siguientes categorías pertenece: 
#● Niño/a: menor de 12 años. 
#● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#● Adulto/a: mayor o igual que 30 años.

#pido al usuario que ingrese su edad y se guarda en la variable edad
edad = int(input("ingrese su edad:\n"))
#con el dato guardado en la variable edad ejecuto la condicion
if edad < 12:
    print("niño")
elif edad >= 12  and edad < 18:
    print("adolescente")
elif edad >= 18 and edad < 30:
    print("adulto/a joven")
else:
    print("adulto/a")


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
# como una lista o un string.

#se pide al usuario que ingrese una contraseña y se guarda en contrasena_usuario
contrasena_usuario = input("ingrese una contraseña:\n")
#en contraseña_correcta guardo la cantidad de string de la contrasena_usuario con la funcion len
contrasena_correcta = len(contrasena_usuario)
#con estos valores ejecuto la condicion
if contrasena_correcta >= 8 and contrasena_correcta <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 

import statistics 
import random 

# Generar la lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# se calcula la media, mediana y moda
media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)


# Imprimir los valores calculados
print(f"Números: {numeros_aleatorios}")
print(f"media: {media}")
print(f"Mediana: {mediana}")
print(f"moda: {moda:.2f}")

#se imprime dependiendo el sesgo
if media > mediana > moda:
    print("hay sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("no hay sesgo")
else:
    print("no cumple con las definiciones")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
#pantalla.

#se pide al usuario que ingrese una palabra
palabra = input("ingrese una palabra:\n")
#en la variable ultima_letra se guarda el valor de la ultima letra de la palabra poniendo -1
ultima_letra = palabra[-1] 
#en la variable vocal dejo el valor de las vocales a e i o u
vocal = 'a' 'e' 'i' 'o' 'u'
#aca ejecuto la condicion si ultima palabra esta dentro de las vocales da True y se ejecuta el print
if ultima_letra in vocal:
    print(f"{palabra}!")
else:#sino se ejecuta el print si da false
    print("no es una palabra que termina en vocal") 


#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#lower() y title() de Python para convertir entre mayúsculas y minúsculas. 


#se pide al usuario que ingrese su nombre
nombre = input("ingrese su nombre: \n")
#se pide al usuario que ingrese la opcion deseada del 1 al 3
numero = int(input("ingrese una opcion:\n 1: \n 2: \n 3: \n --"))
#aca dependiendo la opcion se imprime el nombre de diferentes formas
if numero == 1:#opcion 1 sale todo mayuscula
    print(nombre.upper())
elif numero == 2:#sale todo minuscula
    print(nombre.lower())
elif numero == 3:#sale la primer letra mayuscula
    print(nombre.title())
else:#si ingreso algo mal pide la opcion correcta
    print("ingrese una opcion correcta")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
#por pantalla: 
#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
#generalmente no causa daños). 
#● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
#débiles). 
#● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 

#se pide que ingrese un numero de escala
escala = int(input("ingrese la magnitud del terremoto: \n"))
#dependiendo el numero utilice condicionales para imprimir el resultado
if escala < 3:
    print("Muy leve")
elif escala >= 3 and escala < 4:
    print("Leve")
elif escala >= 4 and escala < 5:
    print("moderado")
elif escala >= 5 and escala < 6:
    print("fuerte")
elif escala >= 6 and escala < 7:
    print("muy fuerte")
else:
     print("extremo")


#10 
#se pide al usuario que ingrese el hemisferio
hemisferio = input("elija un hemisferio norte o sur N/S: \n")
#se pide al usuario que ingrese un dia del 1 al 31
dia = int(input("ingrese un dia del mes del 1 al 31: \n"))
#se pide al usuario que ingrese un dia del mes del 1 al 12
mes = int (input("ingrese un mes del año 1 al 12: \n"))

#aca si hemisferio es Norte da True y se ejecuta esta parte del codigo que utilice condicionales anidados
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
        print("es invierno")
    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
        print("es primavera")
    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
        print("es verano")
    else:
        print("es otoño")
#si el hemisferio es Sur se ejecuta el elif del primer condicional y dentro de este tambien utilice condicionales anidados
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
        print("es verano")
    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
        print("es otoño")
    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
        print("es invierno")
    else:
        print("es primavera")
#si algun dato da false en el if o elif de los primeros condicionales lo cerre con un else de que algun dato no corresponde
else:
    print("ingreso un dato incorrecto")



