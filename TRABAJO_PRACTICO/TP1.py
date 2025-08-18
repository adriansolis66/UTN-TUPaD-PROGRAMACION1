#1)	Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  

print("hola mundo")

#2)	Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”,   el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
nombre = input("ingrese su nombre ")
print(f"hola {nombre}!")

#3)	Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
nombre = input("ingrese su nombre ")
apellido = input("ingrese su apellido ")
edad = input("ingrese su edad ")
residencia = input("ingrese su residencia actual ")
print(f"mi nombre es {nombre} {apellido} tengo {edad} años y soy de {residencia}")

#4)	Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
radio = input("ingrese el radio del circulo: ")

area = 3.14 * float (radio) ** 2
perimetro = 2 * 3.14 * float (radio)

print(f"el radio es {radio} y su area es {area} y su perimetro es {perimetro}")

#5)	Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos = input("ingrese los segundos: ")

horas = float (segundos) / 3600
print(f"los segundos corresponden a {horas} horas")



#6)	Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.  
num = int(input("ingrese un numero "))

for i in range (1, 11):

   print(f"{num} x {i} = {num*i} ") 

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))

suma = num1 + num2
resta = num1 - num2
division = num1 / num2
multiplicacion = num1 * num2

print(f"la suma de {num1} y {num2} es = {suma}")
print(f"la resta de {num1} y {num2} es = {resta}")
print(f"la division de {num1} y {num2} es = {division}")
print(f"la multiplicacion de {num1} y {num2} es = {multiplicacion}")

#8)	Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: I𝑀𝐶 =  𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2
peso = float(input("ingrese su peso: ")) 
altura = float(input("ingrese su altura: "))
imc = peso / (altura ** 2) 
print  (f"su masa corporal es = {imc}")

#9)	) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: T𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/ 5 * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
celsius = float(input("ingrese la temperatura: "))

fahrenheit = (celsius*(9/5)) + 32
print (f"la temperatura en fahrenheit es: {fahrenheit}")

#10)	Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))
num3 = float(input("ingrese el tercer numero: "))
promedio = float((num1 + num2 + num3)) / 3
print(f"el numero promedio es: {promedio}")


