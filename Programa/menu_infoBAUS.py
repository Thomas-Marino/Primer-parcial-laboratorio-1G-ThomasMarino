from funciones.funciones_infoBAUS import *

numero_ingresado = 0
numero_facturacion = 0
lista_insumos = []
lista_marcas = []
lista_nuevos_insumos = []
set_marcas = set({})
ingreso_opc_2 = False
ingreso_opc_3 = False
datos_importados = False
precios_actualizados = False
datos_actualizados_csv = False
datos_actualizados_json = False
datos_actualizados = False
json_creado = False

while numero_ingresado != 12:
    os.system("cls")
    mostrar_menu()
    numero_ingresado = pedir_numero("Ingrese un numero dependiendo la accion que desea realizar: ")
    match numero_ingresado:
        case 1:
            datos_importados = traer_datos_desde_archivo(datos_importados, lista_insumos)
        case 2:
            ingreso_opc_2 = listar_cantidad_por_marca(datos_importados, ingreso_opc_3, ingreso_opc_2, lista_insumos, lista_marcas, set_marcas)
        case 3:
            ingreso_opc_3 = listar_insumos_por_marca(datos_importados, ingreso_opc_2, ingreso_opc_3, lista_insumos, lista_marcas, set_marcas)
        case 4:
            buscar_insumo_por_caracteristica(datos_importados, lista_insumos)
        case 5:
            listar_insumos_ordenados(datos_importados, lista_insumos)
        case 6:
            realizar_compras(datos_importados, lista_insumos, numero_facturacion)
        case 7:
            guardar_json(datos_importados, lista_insumos)
        case 8:
            leer_json()
        case 9:
            precios_actualizados = aplicar_aumento(datos_importados,precios_actualizados, lista_insumos)
        case 10:
            datos_actualizados = añadir_nuevo_insumo(datos_importados, lista_insumos, lista_nuevos_insumos, datos_actualizados)
            datos_actualizados_csv = False
            datos_actualizados_json = False
        case 11:
            datos_actualizados_csv, datos_actualizados_json = \
            guardar_datos_actualizados(lista_insumos, lista_nuevos_insumos, datos_actualizados, datos_actualizados_csv, datos_actualizados_json)
            vaciar_listas(lista_marcas, set_marcas)
            ingreso_opc_2 = False
            ingreso_opc_3 = False
        case 12:
            os.system("cls")
            print("Cierre del programa realizado con éxito.")
        case _:
            os.system("cls")
            print("Esa opción no se encuentra dentro del menú")
            volver_al_menu()