import re

def validacion_entre_2_strings(mensaje:str, condicion_1:str, condicion_2:str)->str:
    """
    Función utilizada con el propósito de validar un ingreso
    entre un máximo de 7 strings\n
    Args:
        mensaje (str): Será el mensaje que se mostrará dentró del input para capturar la respuesta ingresada.\n
        condicion_1 (str): condición que debe cumplir la respuesta ingresada\n
        condicion_2 (str): 2da condición que debe cumplir la respuesta ingresada\n
    Return:
        str: La función retorna la respuesta ingresada luego de qué esta haya cumplido con todos los parámetros ingresados.
    """
    entrada = input(mensaje)
    while (entrada != condicion_1 and
            entrada != condicion_2):
        entrada = input(mensaje)
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