#1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

#cree la funcion imprimir_hola_mundo
def imprimir_hola_mundo():
    print("hola mundo!!")
#llame a la funcion
imprimir_hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

#cree la funcion saludar_usuario
def saludar_usuario(nombre):
    return "hola "+nombre+"!!!"#retorna el nombre ingresado ppor el usuario personalizado
#pido al usuario que ingrese un nombre
nombre_usuario = input("ingrese el nombre de usuario: ")
#crep la variable saludar, con el valor de la funcion creada
saludar = saludar_usuario(nombre_usuario)
#imprimo la variable saludar
print(saludar)

#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

#creo la funcion informacion_personal con los argumentos solicitados
def informacion_personal(nombre, apellido, edad, residencia):
    print("soy " +nombre+" "+apellido+" tengo "+edad+" años y vivo en "+residencia)

#pido al usuario los datos.
nombre_usuario = input("ingrese su nombre: ")
apellido_usuario = input("ingrese su apellido: ")
edad_usuario = input("ingrese su edad: ")
residencia_usuario = input("ingrese su residencia: ")
#llamo a la funcion y le paso los parametros ingresados por el usuario
informacion_personal(nombre_usuario,apellido_usuario,edad_usuario,residencia_usuario)

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
#defino la funcion para calculor el area
def calcular_area_circulo(radio):
    pi = 3.14
    return pi * radio**2
#defino la funcion para calcular el perimetro
def calcular_perimetro_circulo(radio):
    pi = 3.14
    return 2 * pi * radio
    

#pido que el usuario ingrese el radio
radio = float(input("ingrese el radio del circulo: "))
#creo las variables area y perimetro y le asigno el valor con las funciones
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
#imprimo el area y el perimetro
print(f"el area del circulo es {area:.2f} y el perimetro es {perimetro:.2f}")

#5. Crear una función llamada segundos_a_horas(segundos) que reciba
 #una cantidad de segundos como parámetro y devuelva la cantidad
 #de horas correspondientes. Solicitar al usuario los segundos y mos
#trar el resultado usando esta función.

#creo la funcion de segundos
def segundos_a_horas(segundos):
    return segundos // 3660
#pido al usuario que ingrese los segundos
segundos_usuario = int(input("introduzca los segundos: "))
#creo la variable hora y le doy valor con la funcion segundos_a_horas y le paso el parametro ingresado por el usuario
horas = segundos_a_horas(segundos_usuario)
#imprimo la cantidad de horas
print(f"las horas correspondientes a la cantidad de segundos son {horas} horas")

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la fun
#ción.

#creo la funcion tabla_multiplicar(numero)
def tabla_multiplicar(numero):
    for i in range(1,11):
        multiplicar = numero * i
        print(f"{i} x {numero} = {multiplicar}")
#pido el numero al usuario
num = int(input("ingrese el numero que quiere multiplicar: "))
#creo la variable con valor de la funcion creada y el parametro
#con el valor ingresado por el usuario
tabla = tabla_multiplicar(num)


#7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
#sultados de forma clara

#defino la funcion operaciones_basicas(a, b): con dos argumentos
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)

#pido al usuarion ingreso los dos valores
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

#creo la variable operaciones le asigno el valor con la funcion
#y le doy los parametros con las variables num1 y num2
operaciones = operaciones_basicas(num1, num2)

#imprimo con ls posiciones correspondientes
print("\nResultados de las operaciones:")
print("Suma:", operaciones[0])
print("Resta:", operaciones[1])
print("Multiplicación:", operaciones[2])
print("División:",operaciones[3])


#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la 
#función para mostrar el resultado con dos decimales.

#defino la variable calcular_imc(peso, altura)
def calcular_imc(peso, altura):
    imc = peso / altura ** 2
    return imc

#pido al usuario el peso y la altura
peso_usuario = float(input("ingrese su peso por favor: "))
altura_usuario = float(input("ingrese su altura: "))

#creo la variables imc_corporal y le asigno valor con la funcion
imc_corporal = calcular_imc(peso_usuario, altura_usuario)

#imprimo el valor correspondiente
print(f"tu indice de masa corporal es:{imc_corporal:.2f} ")

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función

#defino la funcion con la formula correspondiente
def celsius_a_farenheit(celsius):
    farenheit = celsius * 9/5 + 32
    return farenheit

#pido al usuario que ingrese la temperatura en celsius
celsius_hoy = float(input("ingrese la temperatura de hoy: "))

#creo la variable farenheit con valor de la funcion y el parametro ingresado por el usuario
farenheit_hoy = celsius_a_farenheit(celsius_hoy)

print(f"la temperatura en celsius es: {celsius_hoy} y en farenheit es {farenheit_hoy}")

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función

#creo la funcion calcular_promedio
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

#pido al usuario que ingrese los tres valores
num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
num3 = int(input("ingrese el tercer numero: "))

#creo la variable asigno valor con la funcion y paso los 3 parametros ingresados.
promedio_numero = calcular_promedio(num1, num2, num3)

print(f"el numero 1 es: {num1}\nel numero 2 es: {num2}\nel numero 3 es: {num3}\nel promedio es: {promedio_numero}")