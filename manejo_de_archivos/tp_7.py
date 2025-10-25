#1. Crear archivo inicial con productos: Crear un archivo de texto llamado
#productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

with open ("productos.txt", "w") as archivo:
    archivo.write("budin,150,15\n")
    archivo.write("galletita,100,5\n")
    archivo.write("alfajor,50,10\n")

print("prodcutos del archivo 'archivo.txt' ")

#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
#formato:

with open ("productos.txt","r") as archivo:
    for linea in archivo:
        nombre,precio,cantidad = linea.strip().split(",")
        print(f"producto: {nombre} | precio: {precio} | cantidad: {cantidad}")

#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
#cantidad) y lo agregue al archivo sin borrar el contenido existente.

with open ("productos.txt","a") as archivo:
    nombre = input("ingrese el nuevo producto: ")
    precio = input("ingrese el precio: ")
    cantidad = input("ingrese la cantidad: ")
    archivo.write(f"{nombre},{precio},{cantidad}\n")
    print(f"producto: {nombre} | precio: {precio} | cantidad: {cantidad}")


with open ("productos.txt","r") as archivo:
       for linea in archivo:
         nombre, precio, cantidad = linea.strip().split(",")
         print(f"{nombre} | {precio} | {cantidad}\n")

#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en 
#una lista llamada productos, donde cada elemento sea un diccionario con claves: 
#nombre, precio, cantidad.

productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.split(",")
        producto = {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            }
        productos.append(producto)


print("Lista de productos cargados:")
for i in productos:
    print(f"Nombre: {i['nombre']} | Precio: ${i['precio']} | Cantidad: {i['cantidad']}")


#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un 
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si 
#no existe, mostrar un mensaje de error.

buscar_nombre = input("ingrese el nombre que quiere buscar: ")

encontrado = False

for i in productos:
    if i['nombre'].lower() == buscar_nombre.lower():
        print("producto encontrado")
        print(f"Nombre: {i['nombre']} | Precio: ${i['precio']} | Cantidad: {i['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("no se encontro el nombre")


#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado 
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los 
#productos actualizados desde la lista.

with open("productos.txt","w") as archivo:
    for i in productos:
        archivo.write(f"{i['nombre']},{i['precio']},{i['cantidad']}")
    
    print(productos)

    