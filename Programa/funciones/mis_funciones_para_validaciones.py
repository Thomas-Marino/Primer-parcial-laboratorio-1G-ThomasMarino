import re

def validacion_entre_strings(mensaje:str, parametro_1:str, parametro_2= None, parametro_3= None, parametro_4= None, parametro_5= None, parametro_6= None, parametro_7= None)->str:
    """
    Función utilizada con el propósito de validar un ingreso
    entre un máximo de 7 strings\n
    Args:
        mensaje (str): Será el mensaje que se mostrará dentró del input para capturar la respuesta ingresada.\n
        parametro_1 (str): condición que debe cumplir la respuesta ingresada\n
        parametro_2 (str, optional): condición que debe cumplir la respuesta ingresada. Este parametro viene seteado en None por deffault así que si no se ingresa nada en este parametro, la función cumple su propósito igualmente.\n
        parametro_3 (str, optional): condición que debe cumplir la respuesta ingresada. Este parametro viene seteado en None por deffault así que si no se ingresa nada en este parametro, la función cumple su propósito igualmente.\n
        parametro_4 (str, optional): condición que debe cumplir la respuesta ingresada. Este parametro viene seteado en None por deffault así que si no se ingresa nada en este parametro, la función cumple su propósito igualmente.\n
        parametro_5 (str, optional): condición que debe cumplir la respuesta ingresada. Este parametro viene seteado en None por deffault así que si no se ingresa nada en este parametro, la función cumple su propósito igualmente.\n
        parametro_6 (str, optional): condición que debe cumplir la respuesta ingresada. Este parametro viene seteado en None por deffault así que si no se ingresa nada en este parametro, la función cumple su propósito igualmente.\n
        parametro_7 (str, optional): condición que debe cumplir la respuesta ingresada. Este parametro viene seteado en None por deffault así que si no se ingresa nada en este parametro, la función cumple su propósito igualmente.\n

    Return:
        str: La función retorna la respuesta ingresada luego de qué esta haya cumplido con todos los parámetros ingresados.
    """
    validado = False
    while validado != True:
        entrada = input(mensaje)
        if (parametro_1 and not parametro_2 and
            not parametro_3 and not parametro_4 and
            not parametro_5 and not parametro_6 and
            not parametro_7):
            while entrada != parametro_1:
                entrada = input(mensaje)
            validado = True
        elif (parametro_2 and not parametro_3 and not parametro_4 and
            not parametro_5 and not parametro_6 and
            not parametro_7):
            while (entrada != parametro_1 and
                    entrada != parametro_2):
                entrada = input(mensaje)
            validado = True
        elif (parametro_3 and not parametro_4 and
            not parametro_5 and not parametro_6 and
            not parametro_7):
            while (entrada != parametro_1 and
                    entrada != parametro_2 and
                    entrada != parametro_3):
                entrada = input(mensaje)
            validado = True
        elif (parametro_4 and not parametro_5 and not parametro_6 and
            not parametro_7):
            while (entrada != parametro_1 and
                    entrada != parametro_2 and
                    entrada != parametro_3 and
                    entrada != parametro_4):
                entrada = input(mensaje)
            validado = True
        elif (parametro_5 and not parametro_6 and
            not parametro_7):
            while (entrada != parametro_1 and
                    entrada != parametro_2 and
                    entrada != parametro_3 and
                    entrada != parametro_4 and
                    entrada != parametro_5):
                entrada = input(mensaje)
            validado = True
        elif parametro_6 and not parametro_7:
            while (entrada != parametro_1 and
                    entrada != parametro_2 and
                    entrada != parametro_3 and
                    entrada != parametro_4 and
                    entrada != parametro_5 and
                    entrada != parametro_6):
                entrada = input(mensaje)
            validado = True
        elif parametro_7:
            while (entrada != parametro_1 and
                    entrada != parametro_2 and
                    entrada != parametro_3 and
                    entrada != parametro_4 and
                    entrada != parametro_5 and
                    entrada != parametro_6 and
                    entrada != parametro_7):
                entrada = input(mensaje)
            validado = True
        return entrada

def pedir_palabra(mensaje:str)->str:
    """
    Función que cumple con el propósito de validar el ingreso
    de una palabra a través de un input. Para que el ingreso sea validado,
    éste tiene que cumplir con la condición de estar compuesto únicamente de letras.\n
    Args:
        mensaje (str): Será el mensaje que se mostrará dentró del input para capturar la respuesta ingresada.\n
    Returns:
        str: La función retorna la respuesta ingresada luego de qué esta haya cumplido con la condición de estar compuesta solo por letras.
    """
    validado = False
    while not validado:
        entrada = input(mensaje)
        while not entrada.isalpha():
            print("Error. No se permiten numeros.")
            entrada = input(mensaje)
        validado = True
        return entrada

def encontrar_palabra(texto:str, busqueda:str)->bool:
    """Función que se encarga de buscar un valor dentro de un string.
    Args:
        texto (str): string en el cual se buscará  el valor deseado\n
        busqueda (str): Valor que se buscará dentro del texto.\n
    Returns:
        bool: Si alguna parte del texto coincide con la busqueda, la función retornará True, en el caso contrario, retornará False. 
    """
    busqueda = re.search(busqueda.casefold(), texto.casefold())
    if busqueda:
        validacion = True
    else:
        validacion = False
    return validacion

def pedir_numero(mensaje:str)->int:
    """
    Función que cumple con el propósito de validar el ingreso
    de un número a través de un input. Para que el ingreso sea validado,
    éste tiene que cumplir con la condición de ser un número.\n
    Args:
        mensaje (str): Será el mensaje que se mostrará dentró del input para capturar la respuesta ingresada.\n
    Returns:
        int: La función retorna la respuesta ingresada luego de qué ésta haya cumplido con la condición de ser un número.
    """
    validado = False
    while not validado:
        entrada = input(mensaje)
        while not entrada.isnumeric():
            print(f"Error. {entrada} no es un numero-")
            entrada = input(mensaje)
        validado = True
        return int(entrada)

def pedir_numero_entre_valores(mensaje:str, valor_menor:int, valor_mayor:int)->int:
    """
    Función que cumple con el propósito de validar el ingreso
    de un número entre dos valores a través de un input. Para que el ingreso sea validado
    éste tiene que cumplir con la condición de ser un número y estar entre ambos valores.\n
    Args:
        mensaje (str): Será el mensaje que se mostrará dentró del input para capturar la respuesta ingresada.\n
        valor_menor (int): La respuesta ingresada deberá ser mayor a éste parametro.\n
        valor_mayor (int): La respuesta ingresada deberá ser menor a éste parametro.
    Returns:
        int: La función retorna la respuesta ingresada luego de verificar que ésta se encuentre entre el rango de los dos parametros ingresados.
    """
    validado = False
    while not validado:
        entrada = input(mensaje)
        while not validado:
            while not entrada.isnumeric():
                print(f"Error. {entrada} no es un numero-")
                entrada = input(mensaje)
            if (int(entrada) >= valor_menor and int(entrada) <= valor_mayor):
                validado = True
            else:
                entrada = input(mensaje)
        return int(entrada)

def pedir_ingreso(mensaje:str)->str:
    """
    Función que cumple con el propósito de validar el ingreso de cualquier carácter.
    Args:
        mensaje (str):  Será el mensaje que se mostrará dentró del input para capturar la respuesta ingresada.\n

    Returns:
        str: La función retorna la respuesta ingresada luego de qué esta haya cumplido con la condición de no ser un espacio en blanco.
    """
    validado = False
    while not validado:
        entrada = input(mensaje)
        while re.search("^\s+", entrada) or not entrada:
            print("Error. Debe haber por lo menos una letra o número al comienzo del ingreso.")
            entrada = input(mensaje)
        validado = True
        return entrada

def contar_repeticiones(lista:list, item:str)->int:
    """
    Función que se encarga de contar cuantas veces se repite un valor dentro de una lista.
    Args:
        lista (list): Lista en la cual se contaran las repeticiones.
        item (str): Valor por el cual se compararan los elementos de la lista.  

    Returns:
        int: La función retorna la cantidad de veces que coincidió el item con los elementos dentro de la lista.
    """
    repeticiones = 0 
    for elemento in lista:
        if elemento == item:
            repeticiones += 1
    return repeticiones