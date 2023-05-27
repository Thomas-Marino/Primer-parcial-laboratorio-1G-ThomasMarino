import os
import re
import json
import copy
from funciones.mis_funciones import *
from funciones.mis_funciones_para_validaciones import *

def mostrar_menu()->None:
    """Función encargada de mostrar el menú para InfoBaus.
    """
    print("======== Bienvenido al menu de InfoBaus. =========\n")
    print("=1= Traer datos desde archivo.\n=2= Listar cantidad por marca.")
    print("=3= Listar insumos por marca.\n=4= Buscar insumo por característica.")
    print("=5= Listar insumos ordenados.\n=6= Realizar compras.")
    print("=7= Guardar Json.\n=8= Leer Json.")
    print("=9= Actualizar precios.\n=10= Agregar un nuevo producto a la lista.")
    print("=11= Guardar datos actualizados.\n")
    print("=12= Salir del programa.\n")

def volver_al_menu()->None:
    """Función encargada de pausar el código.
    Esta función está ideada para llamarse al final de un case para que luego de ser llamada, lo próximo a suceder en el código sea la función mostrar_menu().
    """
    input("\n\nPulse enter para volver al menú... ")

def traer_datos_desde_archivo(datos_importados, lista:list):
    os.system("cls")
    if not datos_importados:
        with open("insumos\\Insumos.csv", "r", encoding="utf-8") as insumos_file:
            insumos = insumos_file.read()
        insumos = insumos.replace("ID,NOMBRE,MARCA,PRECIO,CARACTERISTICAS", "")
        insumos = insumos.replace('"', "")
        insumos_desagrupados = insumos.split("\n")
        indice_vacio_removido = True
        while indice_vacio_removido:
            try:
                insumos_desagrupados.remove("")
            except ValueError:
                indice_vacio_removido = False
        for insumo in insumos_desagrupados:
            categoria = insumo.split(",")
            producto = {}
            producto['ID'] = int(categoria[0])
            producto['NOMBRE'] = str(categoria[1])
            producto['MARCA'] = capitalizador(str(categoria[2]))
            producto['PRECIO'] = float(categoria[3].replace("$", ""))
            producto['DESCRIPCION'] = str(categoria[4].replace("|!*|", ", "))
            lista.append(producto)
            datos_importados = True
        print("Los datos fueron importados desde el csv con exito.")
    else:
        print("Los datos ya fueron importados correctamente")
    volver_al_menu()
    return datos_importados

def listar_cantidad_por_marca(datos_importados,ingreso_opc_2, ingreso_opc_3, lista_insumos:list, lista_marcas:list, set_marcas:set):
    os.system("cls")
    if datos_importados:
        if (not ingreso_opc_3 and not ingreso_opc_2):# Si el usuario nunca ingreso a la opc 2 ni 3, realizo todas las operaciones necesarias.
            copiar_key_en_lista_y_set(lista_insumos, lista_marcas, set_marcas, "MARCA")
        else: # Si el usuario ya ingresó previamente a la opcion 2 o 3, solo printeo los datos ya obtenidos
            pass
        print("       Marca\t      Insumos\n")
        for marca in set_marcas:
            print(f"{marca:^20}\t {contar_repeticiones(lista_marcas, marca)}")
        print(f"\n===== Marcas totales: {len(set_marcas)} =====")
        ingreso_opc_2 = True
    else:
        print("Aún no trajo los datos desde el archivo csv.")
    volver_al_menu()
    return ingreso_opc_2

def listar_insumos_por_marca (datos_importados, ingreso_opc_2, ingreso_opc_3, lista_insumos, lista_marcas:list, set_marcas:set):
    os.system("cls")
    if datos_importados:
        if (not ingreso_opc_3 and not ingreso_opc_2): # Si el usuario nunca ingreso a la opc 3 ni a la opc 2, realizo todas las operaciones necesarias.
            ingreso_opc_3 = True
            copiar_key_en_lista_y_set(lista_insumos, lista_marcas, set_marcas, "MARCA")
        else: # Si el usuario ya ingresó previamente a la opc 2 o 3, simplemente imprimo lo pedido en el punto 3.
            pass
        for marca in set_marcas:
            print(f"\t\t\tInsumos de la marca {marca}:")
            for insumo in lista_insumos:
                if insumo['MARCA'] == marca:
                    print(f"{insumo['NOMBRE']:<54} ${insumo['PRECIO']}")
            print("=============================================================================")
    else:
        print("Aún no trajo los datos desde el archivo csv.")
    volver_al_menu()
    return ingreso_opc_3

def buscar_insumo_por_caracteristica(datos_importados, lista_insumos):
    os.system("cls")
    if datos_importados:
        contador = 0
        caracteristica_ingresada = pedir_ingreso("Ingrese la caracteristica por la que desea filtrar los insumos: ")
        os.system("cls")
        print(f"Insumos que coinciden con la caracteristica '{caracteristica_ingresada}':")
        for insumo in lista_insumos:
            if encontrar_palabra(insumo['DESCRIPCION'], caracteristica_ingresada):
                contador += 1 
                print(f"~ ID: {insumo['ID']:02} |\tNombre: {insumo['NOMBRE']:<50}| Marca: {insumo['MARCA']:<30} | Precio: ${insumo['PRECIO']}")
                print(f"  Descripcion: {insumo['DESCRIPCION']}\n")
        if contador == 0:
            print("No se encontraron coincidencias.")
    else:
        print("Aún no trajo los datos desde el archivo csv.")
    volver_al_menu()

def listar_insumos_ordenados (datos_importados, lista_insumos:list):
    os.system("cls")
    if datos_importados:
        lista_ordenada = copy.deepcopy(lista_insumos) # Creo una deepcopy para que no se modifiquen los datos originales.
        bubblesort_doble_campo(lista_ordenada, "menor a mayor", "MARCA", "mayor a menor", "PRECIO")
        print("  ID  Nombre\t                                                    Marca\t   Precio         \tDescripcion\n")
        for insumo in lista_ordenada:
            descripcion_resumida = re.sub(",(.+)", "", insumo['DESCRIPCION']) # creo una variable aparte que contenga la descripcion resumida por REGEX.
            print(f"~ {insumo['ID']:02}  {insumo['NOMBRE']:<54} {insumo['MARCA']:^20}  ${insumo['PRECIO']}          \t{descripcion_resumida:<50}\n")
    else:
        print("Aún no trajo los datos desde el archivo csv.")
    volver_al_menu()

def realizar_compras(datos_importados, lista_insumos:list, numero_facturacion):
    os.system("cls")
    if datos_importados:
        carrito = []
        precio_total = 0
        id_ingresado = 1
        añadir_al_carrito = "si"
        while añadir_al_carrito == "si": # Añado elementos al carrito
            os.system("cls")
            contador = 0
            ids_insumos_filtrados = []
            id_validado = False
            while contador == 0: 
                busqueda_marcas = pedir_palabra("Ingrese la marca por la que desea filtrar los insumos: ")
                os.system("cls")
                print(f"Marcas de insumos que coinciden con los carácteres '{busqueda_marcas}':")
                for insumo in lista_insumos: 
                    if encontrar_palabra(insumo['MARCA'], busqueda_marcas):
                        contador += 1 
                        ids_insumos_filtrados.append(insumo['ID'])
                        print(f"~ ID: {insumo['ID']:02} \tNombre: {insumo['NOMBRE']:<50} Marca: {insumo['MARCA']:<30}  Precio: ${insumo['PRECIO']}")
                        print(f"  Descripcion: {insumo['DESCRIPCION']}\n")
                if contador == 0:
                    input("No se encontraron coincidencias. Pulse enter para volver a filtrar...")
            id_ingresado = pedir_numero_entre_valores("Ingrese el ID del producto que desee añadir al carrito (1 - 50): ", 1, len(lista_insumos))
            while not id_validado:
                for i in range(len(ids_insumos_filtrados)):
                    if id_ingresado == ids_insumos_filtrados[i]:
                        id_validado = True
                if not id_validado:
                    id_ingresado = pedir_numero_entre_valores("Ingrese el ID del producto que desee añadir al carrito (1 - 50): ", 1, len(lista_insumos))
            cantidad_ingresada = pedir_numero_entre_valores("Ingrese cuantas unidades desea comprar, max 99: ", 1, 99)
            precio_por_cantidad = lista_insumos [id_ingresado - 1] ['PRECIO'] * cantidad_ingresada
            carrito.append(f"ID: {lista_insumos [id_ingresado - 1] ['ID']}, Nombre: {lista_insumos [id_ingresado - 1] ['NOMBRE']}, Cantidad: {cantidad_ingresada}\
                            \nPrecio unitario: ${lista_insumos [id_ingresado - 1] ['PRECIO']}, Precio por cantidad: ${precio_por_cantidad:5.2f}.\n")
            añadir_al_carrito = validacion_entre_strings("Producto añadido al carrito, desea añadir otro elemento? si/no: "
                                                                , "si", "no") # Validacion de seguir añadiendo elementos al carrito.
            precio_total += precio_por_cantidad
        os.system("cls") # Una vez termino de agregar elementos al carrito, proceso la compra.
        for elemento in carrito:
            print(elemento)
        print(f"Precio total: ${precio_total:5.2f}.")
        va_a_comprar = validacion_entre_strings("Desea confirmar la compra? s/n: ", "s", "n")
        if va_a_comprar == "s":
            numero_facturacion += 1
            try:
                file_existente = True
                while file_existente:
                    with open(f"facturas\\factura{numero_facturacion}.txt", "r"):
                        file_existente = True
                    numero_facturacion += 1
            except FileNotFoundError:
                with open(f"facturas\\factura{numero_facturacion}.txt", "w", encoding="utf-8") as escritura:
                    escritura.write(f"================== Compra procesada con éxito ==================")
                    escritura.write(f"\n\n- Productos comprados: \n")
                    for elemento in carrito:
                        escritura.write(elemento)
                    escritura.write(f"\nSubtotal: ${precio_total:5.2f}")
                    escritura.write("\n\nMuchas gracias por su compra en InfoBaus electronics.\nAlcoyana alcoyana 555, Roma.")
        else:
            pass
    else:
        print("Aún no trajo los datos desde el archivo csv.")
    volver_al_menu()

def guardar_json(datos_importados, lista_insumos:list):
    os.system("cls")
    if datos_importados:
        with open("insumos\\Insumos.json", "w", encoding="utf-8") as escritura:
            insumos = {}
            insumos ['producto'] = []
            for insumo in lista_insumos:
                insumos ["producto"].append(insumo)
            json.dump(insumos, escritura, indent=4, ensure_ascii=False)
        print("Datos pasados a formato .json correctamente")
    else:
        print("Aún no trajo los datos desde el archivo csv.")
    volver_al_menu()

def leer_json():
    os.system("cls")
    try:
        with open("insumos\\Insumos.json", encoding="utf-8") as archivojson:
            lectura = json.load(archivojson)
        print(lectura)
    except FileNotFoundError:
        print("No hay ningun archivo json para leer.")
    volver_al_menu()

def aplicar_aumento(datos_importados, precios_actualizados, lista_insumos:list):
    os.system("cls")
    if datos_importados:
        if not precios_actualizados:
            lista_precios = []
            precios_actualizados = True
            for elemento in lista_insumos:
                lista_precios.append(elemento['PRECIO'])
            precios_con_impuesto = list(map(lambda a : a + ((a * 8.6)/100), lista_precios))
            for i in range(len(precios_con_impuesto)):
                precios_con_impuesto [i] = float(f"{precios_con_impuesto[i]:5.2f}") 
                lista_insumos [i] ['PRECIO'] = precios_con_impuesto [i]
            with open("insumos\\insumos.csv", "r" ,encoding="utf-8") as archivo:
                copia = archivo.read()
            with open("insumos\\insumos.csv", "w" ,encoding="utf-8") as modificacion:
                texto = copia.split("\n ,")
                texto = str(texto[0])
                i = 0
                for linea in texto.split("\n"):
                    if i == len(lista_insumos):
                        i = len(lista_insumos) - 1 
                    else:
                        reemplazo = str(lista_insumos[i-1]['PRECIO'])
                        linea = re.sub("\$+\d+\.+\d+", f"${reemplazo}", linea)
                        modificacion.write(f"{linea}\n")
                    i+= 1
            print("Precios actualizados con exito.")
        else:
            print("Los precios ya han sido actualizados.")
    else:
        print("Aun no trajo los datos desde el archivo .csv.")
    volver_al_menu()
    return precios_actualizados 


def añadir_nuevo_insumo(datos_importados, lista_insumos:list, lista_nuevos_insumos:list, datos_actualizados):
    os.system("cls")
    if datos_importados:
        primer_descripcion = True
        marca_validada = False
        respuesta = "si"
        contador = 0
        lista_marcas = []
        nuevo_producto = {} 
        nuevo_producto['ID'] = int(lista_insumos[-1] ["ID"] + 1)
        nuevo_producto['NOMBRE'] = str(pedir_ingreso("Ingrese el nombre del nuevo producto: "))
        print("Marcas disponibles: ")
        with open("insumos\\marcas.txt", "r") as archivo_marcas:
            marcas = archivo_marcas.read()
            for marca in marcas.split("\n"):
                lista_marcas.append(marca)
        print(marcas)
        nuevo_producto['MARCA'] = pedir_ingreso("Ingrese que marca desea agregar: ")
        while not marca_validada:
            for i in range(len(lista_marcas)):
                if nuevo_producto['MARCA'] == lista_marcas[i]:
                    marca_validada = True
            if not marca_validada:
                nuevo_producto['MARCA'] = pedir_ingreso("Ingrese que marca desea agregar: ")
        nuevo_producto['PRECIO'] = float(pedir_numero('Ingrese el precio que desea asignarle al producto: '))
        while respuesta != "no":
            contador += 1
            if primer_descripcion:
                nuevo_producto['DESCRIPCION'] = pedir_ingreso("Ingrese una descripcion para el producto: ")
                primer_descripcion = False
            else:
                nuevo_producto['DESCRIPCION'] = nuevo_producto['DESCRIPCION'] + f"|!*|{pedir_ingreso('Ingrese otra descripcion para el producto: ')}"
            if contador == 3:
                respuesta = "no"
            else:
                respuesta = validacion_entre_strings("Desea ingresar otra descripción? si/no: ", "si", "no")
        lista_nuevos_insumos.append(nuevo_producto)
        lista_insumos.append(nuevo_producto)
        datos_actualizados = True
        return datos_actualizados
    else:
        print("Aún no trajo los datos desde el archivo csv.")
    volver_al_menu()

def actualizar_csv(lista_nuevos_insumos:list):
    with open("insumos\\insumos.csv", "r", encoding="utf-8") as archivo_insumos:
        copia = archivo_insumos.read()
    with open("insumos\\insumos.csv", "w", encoding="utf-8") as archivo_insumos:
        archivo_insumos.write(f"{copia}")
        for elemento in lista_nuevos_insumos:
            string_elemento = f"{elemento ['ID']},{elemento['NOMBRE']},{elemento['MARCA']},${elemento['PRECIO']},{elemento['DESCRIPCION']}"
            archivo_insumos.write(f'\n"{string_elemento}"')
        lista_nuevos_insumos.clear()
    print("Datos pasados a formato .csv correctamente")

def actualizar_json(lista_insumos:list):
    with open("insumos\\Insumos.json", "w", encoding="utf-8") as escritura:
        insumos = {}
        insumos ['producto'] = []
        for insumo in lista_insumos:
            insumos ["producto"].append(insumo)
        json.dump(insumos, escritura, indent=4, ensure_ascii=False)
        print("Datos pasados a formato .json correctamente")

def guardar_datos_actualizados(lista_insumos:list,lista_nuevos_insumos:list, datos_actualizados, datos_actualizados_csv, datos_actualizados_json):
    os.system("cls")
    if datos_actualizados:
        if datos_actualizados:
            print("En que formato de archivo desea actualizar los datos?")
            print("=1= Actualizar los datos en el archivo .csv")
            print("=2= Actualizar los datos en el archivo .json.")
            opcion_ingresada = pedir_numero_entre_valores("Ingrese que accion desea realizar: ", 1, 2) 
            match opcion_ingresada:
                case 1:
                    os.system("cls")
                    if not datos_actualizados_csv:
                        actualizar_csv(lista_nuevos_insumos)
                        datos_actualizados_csv = True
                    else:
                        print("Ya actualizo los datos en el archivo .csv.")
                case 2:
                    os.system("cls")
                    if not datos_actualizados_json:
                        actualizar_json(lista_insumos)
                        datos_actualizados_json = True
                    else:
                        print("Ya actualizo los datos en el archivo .json.")
    else:
        os.system("cls")
        print("Aun no realizo ningun cambio.")
    volver_al_menu()
    return datos_actualizados_csv, datos_actualizados_json