# Primer-parcial-laboratorio-1G
---
### [Consigna.](https://docs.google.com/document/d/1MKLTkz4yQ4sdBsssIk2zXlBUpIjJm6e-CrCIeWTSG2s/edit)
---
## Explicación del código paso por paso.  
Cada función está argumentada dentro del código.
---
![image](https://github.com/Thomas-Marino/Primer-parcial-laboratorio-1G/assets/123998550/bd4ae5e3-18d3-4ce2-b9fd-94810e02a760)
- Linea 1 a 7:  
Imports necesarios para el funcionamiento del código.
- Linea 9 a 17:  
Declaración de variables, lista, set y banderas utilizadas en el código:  
numero_ingresado -> seteada a 0 para que pueda ingresarse al while del menú  
- Linea 19 a 197:  
Una vez dentro del while, se mostrara el menú con la función "mostrar_menu()".  
Luego se pide el ingreso de ún número el cual representará la acción que el usuario desee realizar dentro del menú.  
Este número_ingresado será utilizado en un match el cual realizará las acciones dentro del menú según el número ingresado.  
**Cada case del match representa cada una de las consignas, es decir, el case 1 representa a la consigna n°1.**
- ### Case 1 (Traer datos desde archivo)  
![image](https://github.com/Thomas-Marino/Primer-parcial-laboratorio-1G/assets/123998550/ab850103-594a-4a0b-b096-f9ddadc2c7bf)
- Linea 25 a 29:  
Si es la primera vez que el usuario desea importar los datos, estos serán traidos desde el archivo "agrupamiento_insumos" a traves de una lista con la que se operará durante el resto del código.  
**Que sucede en agrupamiento_insumos?**
~~~ PY
from funciones.mis_funciones import capitalizador

with open("insumos\\Insumos.csv", "r", encoding="utf-8") as insumos_file:
    insumos = insumos_file.read()

insumos = insumos.replace("ID,NOMBRE,MARCA,PRECIO,CARACTERISTICAS", "")
insumos = insumos.replace('"', "")
insumos_desagrupados = insumos.split("\n")
lista_insumos = []

indice_vacio_removido = True
while indice_vacio_removido:
    try:
        insumos_desagrupados.remove("")
    except ValueError:
        indice_vacio_removido = False

for insumo in insumos_desagrupados:
    categoria = insumo.split(",")
    if categoria != "":
        producto = {}
        producto['ID'] = int(categoria[0])
        producto['NOMBRE'] = str(categoria[1])
        producto['MARCA'] = capitalizador(str(categoria[2]))
        producto['PRECIO'] = float(categoria[3].replace("$", ""))
        producto['DESCRIPCION'] = str(categoria[4].replace("|!*|", ", "))
        lista_insumos.append(producto)
~~~
Abro el archivo Insumos.csv que se encuentra en la carpeta insumos en modo lectura, creo una variable que guarde el contenido de este archivo y luego lo cierro.  
Reemplazo los valores "ID,NOMBRE,MARCA,PRECIO,CARACTERISTICAS" que se encuentran en la primera linea del archivo por una cadena vacía, luego reemplazo las '"' que se encuentran en el archivo por una cadena vacía.  
  
Creo la variable insumos_desagrupados a la cual le voy a asignar el valor que me devuelva la función split realizada en la cadena previamente modificada, esto va a convertir mi variable en una lista de elementos, cuyos elementos serán los valores que se encontraban separados por saltos de línea dentro del archivo.
  
Una vez obtenida la lista insumos_desagrupados, me aseguro de remover de ella los elementos que representan el carácter Nulo.  
  
Ahora por cada elemento dentro de la lista de insumos_desagrupados, crearé la variable categoría, la cual almacenará los valores dentro de un elemento como elementos de la nueva lista. Al crearse esta variable por cada elemento dentro de la lista insumos_desagrupados, esta se sobreescribirá por cada vuelta.  
Luego creo el diccionario "producto", el cual almacenará dentro de su respectiva key el valor que yo desee.  
Una vez que termino asignar el valor al diccionario, lo añado a una lista.
  
Asi es cómo obtengo una lista la cual tiene almacenados los valores con los que voy a trabajar.  
  
- Linea 30 a 32:  
Si el usuario ya ingreso previamente la opción 1, simplemente imprimo el aviso de que los datos ya fueron importados previamente para no tener que hacerlo otra vez.
---
- ### Case 2 (Listar cantidad por marca)  
![image](https://github.com/Thomas-Marino/Primer-parcial-laboratorio-1G/assets/123998550/9b2b436f-c62d-4db2-a76e-d1b4b92188d9)
- If y else de las lineas 36 y 46 sirven para verificar si los datos ya fueron importados, si los datos no fueron importados, se mostrará el mensaje informandole al usuario que no los importó.  
- If de la linea 37 a 39:  
Cumple con la función de crear la lista y el set de las marcas una sola vez durante la ejecución del código.
- Else de la linea 40: Si el usuario ya ingresó previamente a la opción 2 o 3, solo se ejecutará el print de lo solicitado en el punto 2 en las lineas 42 a 45.
---
- ### Case 3 (Listar insumos por marca)  
![image](https://github.com/Thomas-Marino/Primer-parcial-laboratorio-1G/assets/123998550/4c178257-395c-4b8f-805f-a963948b8e70)
- If y else de las lineas 51 y 63 sirven para verificar si los datos ya fueron importados, si los datos no fueron importados, se mostrará el mensaje informandole al usuario que no los importó.  
- If de la linea 52 a 54:  
Cumple con la función de crear la lista y el set de las marcas una sola vez durante la ejecución del código.
- Else de la linea 55:
Si el usuario ya ingresó previamente a la opción 2 o 3, solo se ejecutará el print de lo solicitado en el punto 3 en las lineas 57 a 62.  
---
- ### Case 4 (Buscar insumo por característica)  
![image](https://github.com/Thomas-Marino/Primer-parcial-laboratorio-1G/assets/123998550/26d05547-4700-45f2-bf37-2094ec20216c)
- If y else de las lineas 68 y 79 sirven para verificar si los datos ya fueron importados, si los datos no fueron importados, se mostrará el mensaje informandole al usuario que no los importó.
- Linea 69 a 78:
Se crea la variable "caracteristica_ingresada" la cual cumplirá con el propósito de almacenar el dato por el cual el usuario desee filtrar la lista de insumos.  
Dentro del for insumo In lista_insumos cada vez que la caracteristica ingresada esté presente en la descripcion del insumo, se printeará el insumo en el que se dé la coincidencia.  
Cada vez que se da esta coincidencia, se le suma un 1 al contador, esto se debe a que si el contador permanece en 0 durante toda las iteraciones del "for in" significa que no se encontraron coincidencias con la caracteristica ingresada.
---
- ### Case 5 (Listar insumos ordenados)  
![image](https://github.com/Thomas-Marino/Primer-parcial-laboratorio-1G/assets/123998550/73cc5240-f589-4476-9a40-9a8ea1e18b5b)
- if de la linea 84 a 89:  
Se crea una deepcopy de la lista de insumos para no modificar la lista original de los insumos. Mediante la función "bubblesort_doble_campo" Realizo el orden solicitado en el punto 5.  
Muestro la lista ordenada.
- else de la linea 90 sirve para verificar si los datos ya fueron importados, si los datos no fueron importados, se mostrará el mensaje informandole al usuario que no los importó.
---
- ### Case 6 (Realizar compras)  
![image](https://github.com/Thomas-Marino/Primer-parcial-laboratorio-1G/assets/123998550/cf0fa150-c04f-403f-89a4-1442cb825388)
- if de la linea 95 a 134:  
    - Creo el carrito y defino las variables al comienzo del case para que estos se reseteen cada vez que vuelvo a ingresar al case.
    - El while de la linea 100 a 120 se encarga de añadir a la lista "carrito" la id del elemento que desee el usuario, especificando su cantidad.  
    Cada elemento de esta lista será un string formateado especificando el Id, nombre, precio Y precio por cantidad del elemento deseado.
    - El while de la linea 103 a 112 se encarga de realizar un filtro por marca de todos los elementos de la lista_insumos. El contador especifica cuantas coincidencias se hayan con la busqueda que
    ingresa el usuario, si la busqueda realizada no coincide con ninguna marca, el programa solicitará realizar una busqueda nueva hasta encontrar una coincidencia.
    - Luego de añadir al carrito los elementos que el usuario quiera, podrá procesar su compra al especificar que no desea ingresar mas elementos al carrito.
- Linea 121 a 136:
    - El propósito del for in de la linea 122 es mostrar al usuario los elementos añadidos al carrito, especificando la cantidad de cada uno y el importe total a pagar.
    - En la linea 125 el usuario decide si va a realizar la compra.
    - Si el usuario desea realizar la compra, dentro del if que abarca de la linea 126 a 134 se abrirá un archivo en modo escritura dentro de la carpeta "facturas". 
    Este archivo representará una factura de la compra realizada. 
    - Si el usuario desea no realizar la compra no sucederá nada y volverá al menú. 
- Else de la linea 137: Cumple con el propósito de informar al usuario que aún no importo la lista de insumos del archivo csv.
--- 
- ### Case 7 (Guardar Json)  
![image](https://github.com/Thomas-Marino/Primer-parcial-laboratorio-1G/assets/123998550/0dc6d5d6-ae32-4591-8fe0-d3230d68574a)
- If de la linea 142 a 149: realizara lo solicitado si el usuario importo previamente los datos.
- Escritura del archivo: Abro el archivo insumos.json dentro de la carpeta "Insumos" en modo escritura.
    - Creo un diccionario el cual estará compuesto por el diccionario "producto".
    - El diccionario "producto" será una lista la cual tendrá como elementos a los insumos separados en sus respectivos diccionarios (ID, NOMBRE, MARCA, PRECIO Y DESCRIPCION)
- Else de la linea 150: Informará al usuario que aun no importo los datos del csv.
---
- ### Case 8 (Leer Json)  
![image](https://github.com/Thomas-Marino/Primer-parcial-laboratorio-1G/assets/123998550/c276a45d-c98e-4be9-95de-731e380010f3)
- if de la linea 155 a 158: Realizará lo solicitado solo si el usuario importó los datos del archivo csv y si el usuario Guardó los datos en formato json. 
- linea 156 a 158:
    - Abro el archivo insumos.json dentro de la carpeta "insumos".
    - Creo la variable lectura la cual contendrá el contenido del archivo json.
    - Cierro el archivo.
    - Muestro por consola los datos del archivo Json.
- Else de la linea 159: Informará al usuario que no existe ningun archivo json para leer.
---
### Case 9 (Actualizar precios)  
![image](https://github.com/Thomas-Marino/Primer-parcial-laboratorio-1G/assets/123998550/629a20c7-917c-4629-8d95-ca9d6f45441e)
- If de la linea 165 a 188 cumple con el propósito de realizar la actualización de precios una sola vez en toda la ejecución.
    - Creo una lista de precios a la cual le voy a añadir como elementos los valores que se encuentran dentro del diccionario 'PRECIO' en cada uno de los elementos de la lista de insumos.
    - creo la variable precios_con_impuesto. Esta variable va a ser una lista la cual almacenará los valores dentro de la lista de precios habiendoles sumado el 8,6% de impuestos a cada uno  
    mediante la función map.
    -  Convierto los elementos de la lista en floats formateados.
    -  Abro el archivo insumos.csv en modo lectura y copio su contenido dentro de la variable "copia". Cierro el archivo.
    -  Abro el archivo insumos.csv nuevamente pero esta vez en modo escritura para modificarlo. creo la variable texto la cual será una lista que almacenará el archivo completo como string  
    -  Declaro la variable i en 0.
    -  For linea in texto.split(\n): linea representará cada renglon dentro de del string texto.
    -  Declaro la variable reemplazo en cada vuelta del for in. Esta variable almacenara el valor del diccionario 'PRECIO' de la lista_insumos en la posición "i-1". Tomo como posición i-1 y  
    no tomo solo a i porque tengo en cuenta que solo debo reemplazar el precio en todos las lineas exceptuando la primera linea del archivo csv.
    -  Modifico la linea reemplazando el precio anterior por el actualizado por medio de la expresión regular "sub".  
    El patrón utilizado solo matcheará con el fragmento de la linea que posea el simbolo "$", que luego del simbolo "$" contenga carácteres númericos a los cuales les seguirá un "." y que luego del       punto hayan más carácteres numericos.
    - Finalmente escribo la linea en el archivo y seteo la bandera precios_actualizados en True para realizar la actualización de precios una sola vez en todo el tiempo de ejecución. 
---
### Case 10 (Salir del programa)
![image](https://github.com/Thomas-Marino/Primer-parcial-laboratorio-1G/assets/123998550/a0c153db-5439-4b5b-aae1-5ff99878e749)
- Al ingresar el número 10 se mostrará un print que indique la finalización del programa y se cumplirá la condición del while saliendo así del menú.
---
### Case _ (Opcion incorrecta)
---
![image](https://github.com/Thomas-Marino/Primer-parcial-laboratorio-1G/assets/123998550/72611e50-b0eb-43f2-a2c0-d87dc46109e9)
- Informa al usuario que ingresó una opción que no está dentro del menú.
---
