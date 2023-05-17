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
    producto = {}
    producto['ID'] = int(categoria[0])
    producto['NOMBRE'] = str(categoria[1])
    producto['MARCA'] = capitalizador(str(categoria[2]))
    producto['PRECIO'] = float(categoria[3].replace("$", ""))
    producto['DESCRIPCION'] = str(categoria[4].replace("|!*|", ", "))
    lista_insumos.append(producto)
