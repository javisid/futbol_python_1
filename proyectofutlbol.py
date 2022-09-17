import csv
from collections import OrderedDict
from threading import local
# Funcion Menu Opciones
def menu_opciones():
    print()
    print()
    print("#################################################################################")
    print("     1. Determinar cuántas veces ganó un país de local o de visitante")
    print("     2. Determinar cuántas veces perdió un país de local o de visitante.")
    print("     3. Determinar cómo le fue al país en los últimos 10 partidos jugados")
    print("     4. Contra que rival jugó el último partido de local o de visitante.")
    print("     5. Como le fue al país históricamente jugando contra otro país indicado.")
    print("     6. Salir del programa")
    print("#################################################################################")
    print()
    print()
#    opcion = input("Ingrese el numero de la opcion deseada: ")
#    return opcion


#Funcion para listar los equipos disponibles
def presentacion_listaequipos():
    nombre_equipos = []
    nombre_archivo = "./futbol_python/partidos.csv"
    with open(nombre_archivo, "r") as archivo:
        partidos = csv.reader(archivo, delimiter=",")
    # Omitir el encabezado
        next(partidos, None)
        for fila in partidos:
            equipo = fila[2]
            nombre_equipos.append(equipo)
#print(nombre_equipos)
    nombres_norep = list(OrderedDict.fromkeys(nombre_equipos))
    nombres_norep2 = sorted(nombres_norep)
#    print(nombres_norep)
    for equipo in nombres_norep2:
        print(equipo)
    return nombres_norep        


# Funcion para verificacion de equipo ingresado valido
def validacionequipo(): 
    equipook=0
    global equiposvalidos
    while equipook == 0:
        equipo_ingresado=input("Ingrese el nombre del equipo, tal cual esta escrito en el listado: ")#
        for i in equiposvalidos:
            if  i != equipo_ingresado:
                equipook = equipook + 0
            elif i == equipo_ingresado:
                equipook = equipook +1
                return equipo_ingresado

# Vericar partidos ganados o perdidos de local.
def partidosganados():
    localovisitante = input("Verifique los partidos ganados de su equipos elija: local o visitante ")
    nombre_archivo = "./futbol_python/partidos.csv"
    global equipoingresado
    partidosganadoslocal = 0
    partidosganadosvisit = 0

    
    with open(nombre_archivo, "r") as archivo:
        partidos = csv.reader(archivo, delimiter=",")
        next(partidos, None)


        for resultado in partidos:  
            if resultado[1] == equipoingresado and resultado[4] < resultado[3]:
                partidosganadoslocal = partidosganadoslocal + 1 
            elif resultado[2] == equipoingresado and resultado[3] < resultado[4]:
                partidosganadosvisit = partidosganadosvisit + 1 

    if localovisitante == "local":
        print(f" {equipoingresado} gano {partidosganadoslocal} de local")
    elif localovisitante == "visitante":
        print(f" {equipoingresado} gano {partidosganadosvisit} de visitante")
    elif localovisitante != "local" or localovisitante != "visitante":
        print('Debe escribir "local" o "visitante"')


def partidosperdidos():
    localovisitante = input("Verifique los partidos perdidos de su equipos elija: local o visitante ")
    nombre_archivo = "./futbol_python/partidos.csv"
    global equipoingresado
    partidosperdidoslocal = 0
    partidosperdidosvisit = 0
    
    with open(nombre_archivo, "r") as archivo:
        partidos = csv.reader(archivo, delimiter=",")
        next(partidos, None)


        for resultado in partidos:  
            if resultado[1] == equipoingresado and resultado[4] > resultado[3]:
                partidosperdidoslocal = partidosperdidoslocal + 1 
            elif resultado[2] == equipoingresado and resultado[3] > resultado[4]:
                partidosperdidosvisit = partidosperdidosvisit + 1

    if localovisitante == "local":
        print(f" {equipoingresado} perdio {partidosperdidoslocal} de local")
    if localovisitante == "visitante":
        print(f" {equipoingresado} perdio {partidosperdidosvisit} de visitante")
    elif localovisitante != "local" or localovisitante != "visitante":
        print('Debe escribir "local" o "visitante"')



# FUNCION PARA OBTENER LOS PARTIDOS QUE GANO, EMPATO O PERDIO DE LOS ULTIMOS 10

def ultimos10():
    nombre_archivo = "./futbol_python/partidos.csv"
    global equipoingresado 


    # Filtrar el  csv con los partidos solo del equipo ingresado
    with open(nombre_archivo, "r") as archivo:
        partidos = csv.reader(archivo, delimiter=",")

        lineas_filtradas = []
        for line in archivo:
            filtro = line.split(',')
            if equipoingresado == filtro[1] or equipoingresado == filtro[2] or "date" == filtro[0]:
                lineas_filtradas.append(line)


    # Grabar un nuevo csv con los partidos solo del equipo ingresado
    archivo.close()
    f = open('./futbol_python/porequipo.csv','w').writelines([line for line in lineas_filtradas])
   

    nombre_archivo2 = "./futbol_python/porequipo.csv"

    with open(nombre_archivo2, "r") as archivo2:    
        data = list(csv.DictReader(archivo2))
 
        ultimos10 = data[-10 :]

        partidosganados = 0
        partidosperdidos = 0
        partidosempatados = 0
    
    
    for objeto in data[-10 :]:
        if objeto['home_team'] == equipoingresado and objeto['away_score'] < objeto['home_score']: 
            partidosganados = partidosganados +1    
        elif objeto['away_team'] == equipoingresado and objeto['home_score'] < objeto['away_score']: 
            partidosganados = partidosganados +1            
        elif objeto['away_score'] == objeto['home_score']:
            partidosempatados = partidosempatados + 1
        elif objeto['home_team'] == equipoingresado and objeto['away_score'] > objeto['home_score']:
            partidosperdidos = partidosperdidos + 1
        elif objeto['away_team'] == equipoingresado and objeto['away_score'] < objeto['home_score']:
            partidosperdidos = partidosperdidos + 1
    print("De los ultimos 10 partidos", equipoingresado,"gano",partidosganados,"empato",partidosempatados,"perdio",partidosperdidos)
    if partidosganados > partidosperdidos: print(equipoingresado,"gano mas partidos que los que perdio")
    if partidosganados < partidosperdidos: print(equipoingresado,"perdio mas partidos que los que gano")
  






#Contra quien jugó el último partido de local o de visitante.
def ultimorival():
    nombre_archivo = "./futbol_python/partidos.csv"
    equipoingresado = "Argentina"
    with open(nombre_archivo, "r") as archivo3:
        localovisitante = input("Verifique los partidos perdidos de su equipos elija: local o visitante ")
        partidos = list(csv.DictReader(archivo3))
        partidoslocal = []
        partidosvisit = []
        for line in partidos:
            if equipoingresado == line['home_team'] or "date" == line['date']:
                partidoslocal.append(line)    
            if equipoingresado == line['away_team'] or "date" == line['date']:
                partidosvisit.append(line)
        for resultado in partidoslocal[-1 :]:
            equiporivaldelocal = resultado['away_team']
        for resultado in partidosvisit[-1 :]:
            equiporivaldevisitante = resultado['home_team']

        if localovisitante == "local":
            print(f" {equipoingresado} jugo su ultimo partido de local contra  {equiporivaldelocal}")
        elif localovisitante == "visitante":
            print(f" {equipoingresado} jugo su ultimo partido de visitante contra  {equiporivaldevisitante}")
        else:
            print('Debe escribir "local" o "visitante"')





#Como le fue al país históricamente jugando contra otro país indicado.
def historicovs():
    nombre_archivo = "./futbol_python/partidos.csv"
    global equipoingresado
    equipoadversario = input("Elija el pais rival: ")
    partidosperdidos = 0
    partidosganados = 0
    partidosempatados = 0
    with open(nombre_archivo, "r") as archivo4:
        partidos = list(csv.DictReader(archivo4))

# FUNCION PARA OBTENER RESULTADOS CONTRA UN EQUIPO ESPECIFICO
        for objeto in partidos:
            if objeto['home_team'] == equipoingresado and objeto['away_team'] == equipoadversario:
                if objeto['home_score'] > objeto['away_score']: 
                    partidosganados = partidosganados +1    
            if objeto['home_team'] == equipoingresado and objeto['away_team'] == equipoadversario:
                if objeto['home_score'] < objeto['away_score']:
                    partidosperdidos = partidosperdidos +1    
            if objeto['home_team'] == equipoingresado and objeto['away_team'] == equipoadversario:               
                if objeto['away_score'] == objeto['home_score']:
                    partidosempatados = partidosempatados + 1
            if objeto['away_team'] == equipoingresado and objeto['home_team'] == equipoadversario:               
                if objeto['away_score'] == objeto['home_score']:        
                    partidosempatados = partidosempatados + 1
            if objeto['away_team'] == equipoingresado and objeto['home_team'] == equipoadversario:
                if objeto['away_score'] > objeto['home_score']:
                    partidosganados = partidosganados +1
            if objeto['away_team'] == equipoingresado and objeto['home_team'] == equipoadversario:
                if objeto['away_score'] < objeto['home_score']:
                    partidosperdidos = partidosperdidos + 1
    partidostotal=partidosempatados+partidosganados+partidosperdidos

    if partidostotal < 1:
        print(f"No se regoistran partidos contra {equipoadversario}")
    elif partidostotal > 0:
        print(f"En el historial de {equipoingresado} contra {equipoadversario} jugaron un total de {partidostotal} donde {equipoingresado} gano {partidosganados}, perdio {partidosperdidos} y empataron {partidosempatados}")





#############################MAIN###################################################################################################################################

if __name__ == '__main__':


    salir = False
    opcion = 0

    print("########################################################")
    print("Bienvenidos a Estadisticas futbol")
    print("########################################################")


    print("########################################################")
    print("Puede obtener algunos datos de los siguientes equipos disponibles")
    print("########################################################")
   


#    presentacion_listaequipos()
    equiposvalidos = presentacion_listaequipos()
#    equipook=0
#    while equipook == 0:
#        equipoingresado=input("Ingrese el nombre del equipo, tal cual esta escrito en el listado: ")#
#        for i in equiposvalidos:
#            if  i != equipoingresado:
#                equipook = equipook + 0
#            elif i == equipoingresado:
#                equipook = equipook +1

                
 ##   equipoingresado = presentacion_listaequipos() 
    equipoingresado = validacionequipo()       


    print(f"Elija que desea saber de {equipoingresado}")
    
    
    
    

    while not salir:
        if opcion == "1": 
            partidosganados()
        if opcion == "2": 
            partidosperdidos()
        if opcion == "3": 
            ultimos10()
        if opcion == "4":
            ultimorival()
        if opcion == "5":
            historicovs()
        if opcion == "6":
            print("MUCHAS GRACIAS! VUELVA PRONTOS!")
            salir = True     
        else:
            menu_opciones()
            opcion = input("elegir una opciones del 1 al 6: ")
    




