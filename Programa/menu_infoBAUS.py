import os
import copy
import json
import re
from funciones.mis_funciones import *
from funciones.mis_funciones_para_validaciones import *
from funciones.funciones_infoBAUS import *

numero_ingresado = 0
numero_facturacion = 1
lista_marcas = []
lista_nuevos_insumos = []
set_marcas = set({})
ingreso_opc_2 = False
ingreso_opc_3 = False
datos_importados = False
precios_actualizados = False
json_creado = False
mensaje_datos_inexistentes = "Aún no trajo los datos desde el archivo csv."

while numero_ingresado != 10:
    os.system("cls")
    mostrar_menu()
    numero_ingresado = pedir_numero("Ingrese un numero dependiendo la accion que desea realizar: ")
    match numero_ingresado:
        case 1:
            os.system("cls")
            if not datos_importados:
                from agrupamiento_insumos import lista_insumos
                datos_importados = True
                print("Datos importados correctamente desde insumos.csv.")
            else:
                print("Los datos ya fueron importados previamente con éxito.")
            volver_al_menu()
        case 2:
            os.system("cls")
            if datos_importados:
                if (not ingreso_opc_3 and not ingreso_opc_2):# Si el usuario nunca ingreso a la opc 2 ni 3, realizo todas las operaciones necesarias.
                    ingreso_opc_2 = True
                    copiar_key_en_lista_y_set(lista_insumos, lista_marcas, set_marcas, "MARCA")
                else: # Si el usuario ya ingresó previamente a la opcion 2 o 3, solo printeo los datos ya obtenidos
                    pass
                print("       Marca\t      Insumos\n")
                for marca in set_marcas:
                    formatear_string_punto_2(marca, contar_repeticiones, lista_marcas)
                print(f"\n===== Marcas totales: {len(set_marcas)} =====")
            else:
                print(mensaje_datos_inexistentes)
            volver_al_menu()
        case 3:
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
                            formatear_string_punto_3(insumo)
                    print("=============================================================================")
            else:
                print(mensaje_datos_inexistentes)
            volver_al_menu()
        case 4:
            os.system("cls")
            if datos_importados:
                contador = 0
                caracteristica_ingresada = capitalizador(pedir_ingreso("Ingrese la caracteristica por la que desea filtrar los insumos: "))
                os.system("cls")
                print(f"Insumos que coinciden con la caracteristica '{caracteristica_ingresada}':")
                for insumo in lista_insumos:
                    if encontrar_palabra(insumo['DESCRIPCION'], caracteristica_ingresada):
                        contador += 1 
                        formatear_string_punto_4(insumo)
                if contador == 0:
                    print("No se encontraron coincidencias.")
            else:
                print(mensaje_datos_inexistentes)
            volver_al_menu()
        case 5:
            os.system("cls")
            if datos_importados:
                lista_ordenada = copy.deepcopy(lista_insumos) # Creo una deepcopy para que no se modifiquen los datos originales.
                bubblesort_doble_campo(lista_ordenada, "menor a mayor", "MARCA", "mayor a menor", "PRECIO")
                print("  ID  Nombre\t                                                    Marca\t   Precio         \tDescripcion\n")
                for insumo in lista_ordenada:
                    formatear_string_punto_5(insumo)
            else:
                print(mensaje_datos_inexistentes)
            volver_al_menu()
        case 6:
            os.system("cls")
            if datos_importados:
                carrito = []
                precio_total = 0
                id_ingresado = 1
                añadir_al_carrito = "si"
                while añadir_al_carrito == "si": # Añado elementos al carrito
                    contador = 0
                    while contador == 0: 
                        busqueda_marcas = capitalizador(pedir_palabra("Ingrese la marca por la que desea filtrar los insumos: "))
                        os.system("cls")
                        print(f"Marcas de insumos que coinciden con los carácteres '{busqueda_marcas}':")
                        for insumo in lista_insumos: 
                            if encontrar_palabra(insumo['MARCA'], busqueda_marcas):
                                contador += 1 
                                formatear_string_punto_6(insumo)
                        if contador == 0:
                            input("No se encontraron coincidencias. Pulse enter para volver a filtrar...")
                    id_ingresado = pedir_numero_entre_valores("Ingrese el ID del producto que desee añadir al carrito (1 - 50): ", 1, 51)
                    cantidad_ingresada = pedir_numero_entre_valores("Ingrese cuantas unidades desea comprar, max 99: ", 1, 100)
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
                    with open(f"facturas\\factura{numero_facturacion}.txt", "w", encoding="utf-8") as escritura:
                        escritura.write(f"================== Compra procesada con éxito ==================")
                        escritura.write(f"\n\n- Productos comprados: \n")
                        for elemento in carrito:
                            escritura.write(elemento)
                        escritura.write(f"\nSubtotal: ${precio_total:5.2f}")
                        escritura.write("\n\nMuchas gracias por su compra en InfoBaus electronics.\nAlcoyana alcoyana 555, Roma.")
                    numero_facturacion += 1
                else:
                    pass
            else:
                print(mensaje_datos_inexistentes)
            volver_al_menu()
        case 7:
            os.system("cls")
            if datos_importados:
                with open("insumos\\Insumos.json", "w", encoding="utf-8") as escritura:
                    insumos = {}
                    insumos ['producto'] = []
                    for insumo in lista_insumos:
                        insumos ["producto"].append(insumo)
                    json.dump(insumos, escritura, indent=4, ensure_ascii=False)
                print("Datos pasados a formato .json correctamente")
                json_creado = True
            else:
                print(mensaje_datos_inexistentes)
            volver_al_menu()
        case 8:
            os.system("cls")
            if datos_importados and json_creado:
                with open("insumos\\Insumos.json", encoding="utf-8") as archivojson:
                    lectura = json.load(archivojson)
                print(lectura)
            else:
                print("No hay ningun archivo json para leer.")
            volver_al_menu()
        case 9:
            os.system("cls")
            if datos_importados:
                if not precios_actualizados:
                    lista_precios = []
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
                            if i == 51:
                                i = 50
                            else:
                                reemplazo = str(lista_insumos[i-1]['PRECIO'])
                                linea = re.sub("\$+\d+\.+\d+", f"${reemplazo}", linea)
                                modificacion.write(f"{linea}\n")
                            i+= 1
                    precios_actualizados = True
                    print("Precios actualizados con exito.")
                else:
                    print("Los precios ya han sido actualizados.")
            else:
                print(mensaje_datos_inexistentes)
            volver_al_menu()
        case 10:
            os.system("cls")
            print("Cierre del programa realizado con éxito.")
        case 11:
            os.system("cls")
            if datos_importados:
                primer_descripcion = True
                respuesta = "si"
                contador = 0
                nuevo_producto = {} 
                nuevo_producto['ID'] = lista_insumos[-1] ["ID"] + 1  
                nuevo_producto['NOMBRE'] = pedir_ingreso("Ingrese el nombre del nuevo producto: ")
                print("Marcas a disponibles: ")
                with open("insumos\\marcas.txt", "r") as archivo_marcas:
                    marcas = archivo_marcas.read()
                print(marcas)
                nuevo_producto['MARCA'] = capitalizador(pedir_ingreso("Ingrese que marca desea agregar: "))
                nuevo_producto['PRECIO'] = f"${float(pedir_numero('Ingrese el precio que desea asignarle al producto: '))}"
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
                # Agrego los datos al csv
                respuesta_actualizar_csv = validacion_entre_strings("Desea cargar los datos al archivo csv? si/no: ", "si", "no")
                if respuesta_actualizar_csv == "si":
                    with open("insumos\\insumos.csv", "r", encoding="utf-8") as archivo_insumos:
                        copia = archivo_insumos.read()
                    with open("insumos\\insumos.csv", "w", encoding="utf-8") as archivo_insumos:
                        archivo_insumos.write(copia)
                        for elemento in lista_nuevos_insumos:
                            string_elemento = f"{elemento ['ID']},{elemento['NOMBRE']},{elemento['MARCA']},{elemento['PRECIO']},{elemento['DESCRIPCION']}"
                            archivo_insumos.write(f'\"{string_elemento}"\n')
                    lista_nuevos_insumos.clear() # Vacio la lista luego de cargar los elemntos.
                else:
                    pass
                respuesta_actualizar_json = validacion_entre_strings("Desea cargar los datos en formato json? si/no: ", "si", "no")
                if respuesta_actualizar_json == "si":
                    with open("insumos\\Insumos.json", "w", encoding="utf-8") as escritura:
                        insumos = {}
                        insumos ['producto'] = []
                        for insumo in lista_insumos:
                            insumos ["producto"].append(insumo)
                        json.dump(insumos, escritura, indent=4, ensure_ascii=False)
                        print("Datos pasados a formato .json correctamente")
            else:
                print(mensaje_datos_inexistentes)
            volver_al_menu()
        case _:
            os.system("cls")
            print("Esa opción no se encuentra dentro del menú")
            volver_al_menu()