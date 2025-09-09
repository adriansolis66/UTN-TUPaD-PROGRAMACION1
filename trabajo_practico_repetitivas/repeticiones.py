#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

#utilice el ciclo for con un rango de 0 a 101 para q incluya el 0 y el 100
for i in range (0,101):
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene.

#se pide al usuario que ingrese un numero que lo va a tomar como string
numero = input("ingrese un numero\n")
#con la funcion len me devuelve la cantidad de carecteres que tiene
digito = len(numero)

print (digito)

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores.

#pido al usuario que ingrese dos valores
numero_1 = int(input("ingrese el primer numero\n"))
numero_2 = int(input("ingrese el segundo valor\n"))
#inicializo la variable total en 0
total = 0
#ingreso un condicional si numero_1 es mayor que 2
if numero_1 < numero_2:
    #utilizo el ciclo for para contar los ciclos con los numeros ingresados
    for i in range(numero_1+1,numero_2): 
        total += i

    print(total)
#si la primer condicion da false entra en la segunda condicion numero_ es mayor
elif numero_2 < numero_1:
    #utilizo otro ciclo for para contar los ciclos con los numeros ingresados 
    for i in range(numero_2+1,numero_1):
        total += i

    print(total)
    #se ejecuta else si los 2 primeros dan false
else:
    print("los numeros son iguales")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#un 0.
#inicialice la variable suma en 0
suma = 0
#con el ciclo while puse la condicion que mientras sea diferente a 0 se continue el ciclo 
while numero != 0:
    #pido que ingrese un numero
    numero = int(input("ingrese un numero y presione 0 para detenerse\n"))
    suma += numero #y numero se va sumando a suma en cada iteracion
print (suma)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

#inicializo la variable iteracion
iteracion = 0
#con el ciclo while puse la condicion que mientras sea diferente a 9 se continue el ciclo 
while numero != 9:
    ##pido que ingrese un numero
    numero = int(input("adivine el numero entre el 1 y el 9\n"))
    #iteracion va sumando en 1 lo que va a determinar la cantidad de intentos
    iteracion += 1
#imprimo iteracion para la cantidad de intentos que hizo el usuario 
print (iteracion)

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente.

#utilizo un ciclo for con rango de 100 a 0 y que se actualice en -2 para que vaya decreciendo
for i in range(100,0,-2):
    print(i)


#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario.
#inicializo suma en 0
suma = 0
#pido al usuario que ingrese un valor que queda guardado en la variable numero
numero = int(input("ingrese un numero entero\n"))
#al saber los valores utilizo un ciclo for para que vaya iterando desde el 0 hasta el numero ingresado

for i in range(0,numero):
    #y aca la variable suma guarda el valor de i en cada vuelta y se va sumando
    suma += i

print(suma)

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

#inicilizo las variables par, impar, negativo, positivo, iteracion
par = 0
impar = 0
negativo = 0
positivo = 0
iteracion = 0

#utilizo un ciclo while y con la variable iteracion tengo el fin del ciclo cuando llega a 10
#se puede utilizar la cantidad que uno quiera cambiando la condicion
while iteracion < 10:
    #pido un numero al usuario y se guarda en la variable numero
    numero = int(input("ingrese un 10 numeros\n"))
    #dependiendo que numero ingrese va a entrar al condicional if que le corresponda
    #y va a sumar en la variable correspondiente por ejemplo si es par y positivo se suma 1 a estas dos
    if numero %2 == 0 and numero > 0:
        par += 1
        positivo += 1
    if numero %2 != 0  and numero > 0:
        impar += 1
        positivo += 1
    if numero %2 == 0  and numero < 0:
        par += 1
        negativo += 1
    if numero %2 != 0  and numero < 0:
        impar += 1
        negativo += 1
    iteracion += 1 #aca iteracion se va sumando a 1 para llegar al numero de vueltas correspondientes para cortar el ciclo
print(f"hay {positivo} numeros positivos\n")
print(f"hay {negativo} numeros negativos\n")
print(f"hay {par} numeros par\n")
print(f"hay {impar} numeros impar\n")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor).

#inicialice 2 variables
numeros_total = 5
suma = 0

#como se el numero de iteracion de antemano utilice un ciclo for
for i in range(numeros_total):#cambiando numero total puedo ejecutar la cantidad de iteraciones deseada
    #pido un numero al usuario se guarda en la variable numero
    numero = float(input("ingrese 5 numeros entero\n"))
    #la variable suma contiene el valor de numero y se va sumando en cada iteracion
    suma += numero
#con la variable media hago el calculo para saber la media dividiendo suma por la cantidad de numeros
media = suma / numeros_total

print(f"la media de los numeros es {media}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
#aca importo la funcion math para utiliza la funcion math.trunc
import math
#inicializo 3 variables en 0
num = 0
num_invertido = 0
resto = 0
#pido al usuario un numero
num = int(input("ingrese un numero entero\n"))
#con el condicional determino que el ciclo se corte cuando num sea menor que cero
while num > 0:
    #a la variable resto le doy el valor de num%10
    resto = num % 10
    #a la variable num_invertido le doy el valor del resto
    num_invertido = (num_invertido * 10) + resto
    #y con la funcion de trunc saco el valor entero de num/10
    num = math.trunc(num/10)
#cuando termine el ciclo y num sea menor que 0 imprimo el valor de num_invertido
print(num_invertido)    




