import csv
from collections import OrderedDict
# Funcion Menu Opciones
def menu_opciones():
    print("     1.Determinar cuántas veces ganó un país de local o de visitante")
    print("     2. Determinar cuántas veces perdió un país de local o de visitante.")
    print("     3. Determinar cómo le fue al país en los últimos 10 partidos jugados")
    print("     4. Contra quien jugó el último partido de local o de visitante.")
    print("     5. Como le fue al país históricamente jugando contra otro país indicado.")
    opcion = input("Ingrese el numero de la opcion deseada: ")
    return opcion


#Funcion para listar los equipos disponibles
def presentacion_listaequipos():
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
    nombres_norep2 = sorted(nombres_norep)
#    print(nombres_norep)
    for equipo in nombres_norep2:
        print(equipo)
    return nombres_norep        

# Vericar partidos ganados o perdidos de local.
def Partidoslocal():
#    nombre_equipos = []
#    nombre_archivo = "futbol_python_1/partidos.csv"
#    nombre_equipos = []
    nombre_archivo = "futbol_python_1/partidos.csv"
    equipoingresado = "England"
    partidosganadoslocal = 0
    partidosperdidoslocal = 0
    partidosempatados = 0


    with open(nombre_archivo, "r") as archivo:
        partidos = csv.reader(archivo, delimiter=",")
        next(partidos, None)


        for resultado in partidos:  
            if resultado[1] == equipoingresado and resultado[4] < resultado[3]:
                partidosganadoslocal = partidosganadoslocal + 1 
            elif resultado[1] == equipoingresado and resultado[4] > resultado[3]:
                partidosperdidoslocal = partidosperdidoslocal + 1
            elif resultado[1] == equipoingresado and resultado[4] == resultado[3]:
                partidosempatados = partidosempatados + 1

    print(f"Partidos ganados de local:", partidosganadoslocal)
    print(f"Partidos perdidos de local:", partidosperdidoslocal)
    print(f"Partidos empatados:", partidosempatados)


def Partidosvisitante():
#    nombre_equipos = []
#    nombre_archivo = "futbol_python_1/partidos.csv"
#nombre_equipos = []
    nombre_archivo = "futbol_python_1/partidos.csv"
    equipoingresado = "England"
    partidosperdidosvisit = 0
    partidosganadosvisit = 0
    partidosempatados = 0

    with open(nombre_archivo, "r") as archivo:
        partidos = csv.reader(archivo, delimiter=",")
        next(partidos, None)

        for resultado in partidos:   
            if resultado[2] == equipoingresado and resultado[3] < resultado[4]:
                partidosganadosvisit = partidosganadosvisit + 1 
            elif resultado[2] == equipoingresado and resultado[3] > resultado[4]:
                partidosperdidosvisit = partidosperdidosvisit + 1
            elif resultado[2] == equipoingresado and resultado[4] == resultado[3]:
                partidosempatados = partidosempatados + 1

    print(f"Partidos ganados de visitante:", partidosganadosvisit)
    print(f"Partidos perdidos  de visitante:", partidosperdidosvisit)
    print(f"Partidos empatados visitante:", partidosempatados)





#############################MAIN###################################################################################################################################

if __name__ == '__main__':
    print("########################################################")
    print("########################################################")
    print("########################################################")

    print("Bienvenidos a Estadisticas futbol")
    print("########################################################")

    print("Puede obtener algunos datos de los siguientes equipos disponibles")
    print("########################################################")
    print("########################################################")
    print("########################################################")

    presentacion_listaequipos()
    equiposvalidos = presentacion_listaequipos()
    equipook=0
    while equipook == 0:
        equipoingresado=input("Ingrese el nombre del equipo, tal cual esta escrito en el listado:")
        for i in equiposvalidos:
            if  i != equipoingresado:
                equipook = equipook + 0
            elif i == equipoingresado:
                equipook = equipook +1
            
    print(f"Elija que desea saber de {equipoingresado}")
    
    
    
    opcion=menu_opciones()
    print(opcion)

