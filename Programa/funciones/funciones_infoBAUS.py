import re

def mostrar_menu()->None:
    """Función encargada de mostrar el menú para InfoBaus.
    """
    print("======== Bienvenido al menu de InfoBaus. =========\n")
    print("=1= Traer datos desde archivo.\n=2= Listar cantidad por marca.")
    print("=3= Listar insumos por marca.\n=4= Buscar insumo por característica.")
    print("=5= Listar insumos ordenados.\n=6= Realizar compras.")
    print("=7= Guardar Json.\n=8= Leer Json.")
    print("=9= Actualizar precios.\n=10= Salir del programa.\n")

def volver_al_menu()->None:
    """Función encargada de pausar el código.
    Esta función está ideada para llamarse al final de un case para que luego de ser llamada, lo próximo a suceder en el código sea la función mostrar_menu().
    """
    input("\n\nPulse enter para volver al menú... ")

# Funciones ideadas para que el código del menú sea más legible y ahorrar un par de lineas. Simplemente son un copy-paste de los formateos par cáda respuesta.
# En cada parametro se debera ingresar el mismo parametro especificado en la definicion de cada funcion
def formatear_string_punto_2(marca, contar_repeticiones, lista_marcas)->None:
    print(f"{marca:^20}\t {contar_repeticiones(lista_marcas, marca)}")

def formatear_string_punto_3(insumo)->None:
    print(f"{insumo['NOMBRE']:<54} ${insumo['PRECIO']}")

def formatear_string_punto_4(insumo)->None:
    print(f"~ ID: {insumo['ID']:02} |\tNombre: {insumo['NOMBRE']:<50}| Marca: {insumo['MARCA']:<30} | Precio: ${insumo['PRECIO']}")
    print(f"  Descripcion: {insumo['DESCRIPCION']}\n")

def formatear_string_punto_5(insumo)->None:
    descripcion_resumida = re.sub(",(.+)", "", insumo['DESCRIPCION']) # creo una variable aparte que contenga la descripcion resumida por REGEX.
    print(f"~ {insumo['ID']:02}  {insumo['NOMBRE']:<54} {insumo['MARCA']:^20}  ${insumo['PRECIO']}          \t{descripcion_resumida:<50}\n")

def formatear_string_punto_6(insumo)->None:
    print(f"~ ID: {insumo['ID']:02} \tNombre: {insumo['NOMBRE']:<50} Marca: {insumo['MARCA']:<30}  Precio: ${insumo['PRECIO']}")
    print(f"  Descripcion: {insumo['DESCRIPCION']}\n")

def formatear_string_factura(lista_insumos, id_ingresado, cantidad_ingresada, precio_por_cantidad)->None:
    f"ID: {lista_insumos [id_ingresado - 1] ['ID']}, Nombre: {lista_insumos [id_ingresado - 1] ['NOMBRE']}, Cantidad: {cantidad_ingresada}\
    \nPrecio unitario: ${lista_insumos [id_ingresado - 1] ['PRECIO']}, Precio por cantidad: {precio_por_cantidad}.\n\n"