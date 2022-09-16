import csv
from collections import OrderedDict

nombre_equipos = []
nombre_archivo = "futbol_python_1/partidos.csv"
with open(nombre_archivo, "r") as archivo:
    partidos = csv.reader(archivo, delimiter=",")
    # Omitir el encabezado
    next(partidos, None)
    for fila in partidos:
        # Tenemos la lista. En la 0 tenemos el nombre, en la 1 la calificación y en la 2 el precio
        equipo = fila[2]
        nombre_equipos.append(equipo)
#print(nombre_equipos)
nombres_norep = list(OrderedDict.fromkeys(nombre_equipos))
print(nombres_norep)
        


#        calificacion = int(fila[1])
#        precio = float(fila[2])
#        
#        print(
#            f"Elija el equipo : {nombres_norep} ")