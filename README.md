# Primer-parcial-laboratorio-1G
---
### [Consigna.](https://docs.google.com/document/d/1MKLTkz4yQ4sdBsssIk2zXlBUpIjJm6e-CrCIeWTSG2s/edit)
---
## Explicación del código paso por paso. Cada función está argumentada dentro del código.
---
![image](https://github.com/Thomas-Marino/Primer-parcial-laboratorio-1G/assets/123998550/76fd5c3c-2337-409e-8db9-35e4aef05e17)
- Linea 1 a 7:  
Imports necesarios para el funcionamiento del código.
- Linea 9 a 16:  
Declaración de variables y banderas utilizadas en el código:  
numero_ingresado -> seteada a 0 para que pueda ingresarse al while del menú  
numero_facturacion -> variable utilizada para la resolución del punto 6.  
- Linea 16 a 203:  
Una vez dentro del while, se mostrara el menú con la función "mostrar_menu()".  
Luego se pide el ingreso de ún número el cual representará la acción que el usuario desee realizar dentro del menú.  
Este número_ingresado será utilizado en un match el cual realizará las acciones dentro del menú según el número ingresado.  
**Cada case del match representa cada una de las consignas, es decir, el case 1 representa a la consigna n°1.**
- ### Case 1  
![image](https://github.com/Thomas-Marino/Primer-parcial-laboratorio-1G/assets/123998550/7f7cbb37-355b-4f48-93dd-9dcf28a81d94)
- Linea 21 a 26:  
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
  
- Linea 27 a 29:  
Si el usuario ya ingreso previamente la opción 1, simplemente imprimo el aviso de que los datos ya fueron importados previamente para no tener que hacerlo otra vez.
---
- ### Case 2  
![image](https://github.com/Thomas-Marino/Primer-parcial-laboratorio-1G/assets/123998550/9b2b436f-c62d-4db2-a76e-d1b4b92188d9)
- If y else de las lineas 33 y 47 sirven para verificar si los datos ya fueron importados, si los datos no fueron importados, se mostrará el mensaje informandole al usuario que no los importó.  
- If de la linea 34 a 41:  
Cumple con la función de crear la lista y el set de las marcas una sola vez durante la ejecución del código.
- Else de la linea 41: Si el usuario ya ingresó previamente a la opción 2 o 3, solo se ejecutará el print de lo solicitado en el punto 2 en las lineas 43 a 46.
---
- ### Case 3  
![image](https://github.com/Thomas-Marino/Primer-parcial-laboratorio-1G/assets/123998550/09ff557d-4263-47a5-a99c-aebb98f6ddab)
- If y else de las lineas 52 y 68 sirven para verificar si los datos ya fueron importados, si los datos no fueron importados, se mostrará el mensaje informandole al usuario que no los importó.  
- If de la linea 53 a 59:  
Cumple con la función de crear la lista y el set de las marcas una sola vez durante la ejecución del código.
- Else de la linea 60:
Si el usuario ya ingresó previamente a la opción 2 o 3, solo se ejecutará el print de lo solicitado en el punto 3 en las lineas 62 a 67.  
---
- ### Case 4  
![image](https://github.com/Thomas-Marino/Primer-parcial-laboratorio-1G/assets/123998550/b6b4b23f-958b-44b2-8377-78cf5fe16366)

~~~
## Link del proyecto
- [Proyecto](https://www.tinkercad.com/things/jwLanq90ugF)
