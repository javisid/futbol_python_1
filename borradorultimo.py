import csv
#Contra quien jugó el último partido de local o de visitante.
nombre_equipos = []
nombre_archivo = "futbol_python_1/partidos.csv"
equipoingresado = "Argentina"
partidosperdidosvisit = 0
partidosganadosvisit = 0
partidosempatados = 0
with open(nombre_archivo, "r") as archivo3:
    partidos = list(csv.DictReader(archivo3))
#    partidos = csv.reader(archivo, delimiter=",")
    partidoslocal = []
    partidosvisit = []
    for line in partidos:
#        filtro = line.split(',')
        if equipoingresado == line['home_team'] or "date" == line['date']:
            partidoslocal.append(line)    
        if equipoingresado == line['away_team'] or "date" == line['date']:
            partidosvisit.append(line)
    for resultado in partidoslocal[-1 :]:
        print(resultado['away_team'])
    for resultado in partidosvisit[-1 :]:
        print(resultado['home_team'])
print(archivo3)