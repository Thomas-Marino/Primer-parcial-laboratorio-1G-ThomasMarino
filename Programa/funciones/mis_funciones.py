# =============== STRINGS ===============
def capitalizador(cadena:str)->str:
    """Función que se encarga de convertir la primer letra de una cadena de strings en mayúscula.
    Ademas, si el primer o el último carácter de la cadena es un espacio en blanco , la función se encarga de eliminarlo
    porque sino crashea.
    Args:
        cadena (str): String a convertir.
    Returns:
        str: String modificado. La primer letra de este string será una mayúscula y el resto serán minúsculas. En el caso de ser más de una palabra, 
        aquellas que tienen un espacio adelante también son modificadasa
    """
    cadena_auxiliar = list(cadena)
    if cadena_auxiliar[0].isspace():
        cadena_auxiliar.remove(" ")
    elif cadena_auxiliar[-1].isspace():
        cadena_auxiliar.pop(-1)
    for i in range(len(cadena_auxiliar)):
        if (cadena_auxiliar[i].isupper()):
            cadena_auxiliar[i] = cadena_auxiliar[i].lower()
    cadena_auxiliar[0] = cadena_auxiliar[0].upper()
    for i in range(len(cadena_auxiliar)):
        if (cadena_auxiliar[i].isspace()):
            cadena_auxiliar[i + 1] = cadena_auxiliar[ i + 1 ].upper()
    cadena = "".join(cadena_auxiliar)
    return cadena

# =============== COPIAR ===============
def copiar_key_en_lista_y_set(lista:list, lista_nueva:list, set_nuevo:set, key:str)->None:
    """Función que cumple con el proposito de copiar el contenido de un diccionario especifico y almacenarlo en una lista y en un set.

    Args:
        lista (list): lista en la cual se encuentra el diccionario
        lista_nueva (list): lista en la cual se ingresaran los valores copiados
        set_nuevo (set): set en el cual se ingresaran los valores
        key (str): key del diccionario a copiar.
    """
    for i in lista:
        set_nuevo.add(i[key])
        lista_nueva.append(i[key])

# =============== ORDENAMIENTO ===============
def bubblesort(lista:list, ordenamiento:str, key = None)->None:
    """Función que se encarga de modificar una lista ordenandola mediante el método de 'Burbujeo'.
    Args:
        lista (list): Lista que se desea ordenar 
        ordenamiento (str): Dependiendo de que opción de ordenamiento se ingrese, la función burbujeará en torno a lo solicitado.
        key (str, optional): En caso de querer ordenar un diccionario, solo será ordenada la key ingresada.
    """
    tam = len(lista)
    if key:
        bandera = True
    else:
        bandera = False
    for i in range(0, tam-1):
        for j in range(i + 1, tam):
            if ((bandera and ordenamiento == "menor a mayor" and lista[i] [key] > lista[j] [key]) 
                or (bandera and ordenamiento == "mayor a menor" and lista[i] [key] < lista[j] [key])):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
            elif ((not bandera and ordenamiento == "menor a mayor" and lista[i] > lista[j]) 
                or (not bandera and ordenamiento == "mayor a menor" and lista[i] < lista[j])):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux

def bubblesort_doble_campo(lista:list, ordenamiento:str, key:str, ordenamiento_2:str, key_2:str)->None:
    """Función que se encarga de modificar dos campos de un diccionario ordenandolos mediante el método de 'Burbujeo'.
    Args:
        lista (list): Lista que contiene los diccionarios
        ordenamiento (str): Dependiendo de que opción de ordenamiento se ingrese, la función burbujeará en torno a lo solicitado.
        key (str): Primer key a ordenar.
        ordenamiento_2 (str): Dependiendo de que opción de ordenamiento se ingrese, la función burbujeará en torno a lo solicitado.
        key_2 (str): Segunda key a ordenar. Esta se ordenara dependiendo del ordenamiento ingresado cada vez que el valor del primer diccionario coincida con un valor 
        de ese mismo diccionario.
    """
    bubblesort(lista, ordenamiento, key)
    i = 0
    j = 0
    if ordenamiento_2 == "mayor a menor":
        while i < len(lista):
            while j < len(lista) - 1:
                if lista [j] [key] == lista [j+1] [key]:
                    if lista [j] [key_2] < lista [j+1] [key_2]:
                        elemento_auxiliar = lista [j+1]
                        lista [j+1] = lista [j]
                        lista [j] = elemento_auxiliar
                        j = 0
                j += 1
            i += 1
    elif ordenamiento_2 == "menor a mayor":
        while i < len(lista):
            while j < len(lista) - 1:
                if lista [j] [key] == lista [j+1] [key]:
                    if lista [j] [key_2] > lista [j+1] [key_2]:
                        elemento_auxiliar = lista [j+1]
                        lista [j+1] = lista [j]
                        lista [j] = elemento_auxiliar
                        j = 0
                j += 1
            i += 1
#=========== LISTAS ================
def vaciar_listas(lista_1:list, lista_2:list=[], lista_3:list=[], lista_4:list=[], lista_5:list=[]):
    """Funcion ideada para vaciar hasta 5 listas.
    Args:
        lista_1 (list): primer lista a vaciar
        lista_2 (list, optional):  Segunda lista a vaciar (Opcional)
        lista_3 (list, optional):  Tercera lista a vaciar (Opcional)
        lista_4 (list, optional):  Cuarta lista a vaciar (Opcional)
        lista_5 (list, optional):  Quinta lista a vaciar (Opcional)
    """
    lista_1.clear()
    lista_2.clear()
    lista_3.clear()
    lista_4.clear()
    lista_5.clear()

def setear_banderas(bandera_1:bool, bandera_2:bool, estado:bool)->bool:
    """Funcion ideada para setear 2 banderas a un mismo estado mas facilmente.

    Args:
        bandera_1 (bool): primer bandera a settear
        bandera_2 (bool): segunda bandera a settear
        estado (bool): estado en el que se las quiera setear (True o False).

    Returns:
        bool: ambas banderas seteadas al mismo estado.
    """
    if estado:
        bandera_1 = True
        bandera_2 = True
    if not estado:
        bandera_1 = False
        bandera_2 = False
    return bandera_1, bandera_2