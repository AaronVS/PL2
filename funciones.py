import pandas as pd
import random
import datetime 

from choices import *

# Listas 

universidades_list = []
estudiantes_list = []
estancias_list = []
asignaturas_list = []
convalidaciones_list = []

#Funciones

def generar_universidades(numero_universidades):
    """
    Funcion que genera x universidades aleatoriamente y las exporta a un csv
    """
    print()
    print("-----------------------------------------------------")
    print("INICIO GENERADOR UNIVERSIDADES")
    print("-----------------------------------------------------")
    for i in range(numero_universidades):
        #universidad contienen el codigo de universidad, nombre, direccion, pais, telefono, email

        nueva_universidad =  [i,"Universidad"+str(i), "Direccion"+str(i), paises[random.randrange(len(paises))], create_phone() , "email"+str(i)+"@"+"universidad"+str(i)+".com"]
        universidades_list.append(nueva_universidad)

        if (i%(numero_universidades/10) == 0):
            print("Universidades generadas: " + str(i))
        
    
    universidades_df = pd.DataFrame(universidades_list)

    print("Universidades generadas: " + str(len(universidades_list)))
    
    universidades_df.to_csv (r'./csv/universidades.csv', index = False, header=False)

    print("-----------------------------------------------------")
    print("FIN GENERADOR UNIVERSIDADES")
    print("-----------------------------------------------------")

def generar_estudiantes(numero_estudiantes, numero_universidades):
    """
    Función que genera x estudiantes aleatoriamente y las exporta a un csv
    """
    print()
    print("-----------------------------------------------------")
    print("INICIO GENERADOR ESTUDIANTES")
    print("-----------------------------------------------------")

    for i in range(numero_estudiantes):
        #estudiante contienen el codigo de estudiante, nombre, apellidos, direccion, pais, telefono, email, creditos aprobados, universidad
        nuevo_estudiante =  [i,"Nombre"+str(i), "Apellido"+str(i), "Direccion"+str(i), paises[random.randrange(len(paises))], create_phone(), "email"+str(i)+"@"+"estudiante"+str(i)+".com", random.randrange(60,240), random.randrange(0,numero_universidades)]
        estudiantes_list.append(nuevo_estudiante)

        if (i%(numero_estudiantes/10) == 0):
            print("Estudiantes generados: " + str(i))
        
    
    estudiantes_df = pd.DataFrame(estudiantes_list)

    print("Estudiantes generados: " + str(len(estudiantes_list)))
    
    estudiantes_df.to_csv (r'./csv/estudiantes.csv', index = False, header=False)

    print("-----------------------------------------------------")
    print("FIN GENERADOR ESTUDIANTES")
    print("-----------------------------------------------------")


def generar_asignaturas():
    """
    Funcion que genera x asignaturas aleatoriamente y las exporta a un csv
    """
    print()
    print("-----------------------------------------------------")
    print("INICIO GENERADOR ASIGNATURAS")
    print("-----------------------------------------------------")

    universidades_df = pd.read_csv(r'./csv/universidades.csv', delimiter=",", names=["codigo", "nombre", "direccion", "pais", "telefono", "email"])

    codigo = 0
    for i in range(len(universidades_df)):
        for k in range (random.randrange(15,20)):
            #asignatura contienen el codigo de asignatura, nombre, creditos, universidad
            nueva_asignatura =  [codigo,"Asignatura"+str(k), ects[random.randrange(len(ects))], tipo_asignatura[random.randrange(len(tipo_asignatura))], universidades_df.iloc[i]["codigo"]]
            asignaturas_list.append(nueva_asignatura)
            codigo += 1
            if (codigo%100000 == 0):
                print("Asignaturas generadas: "+str(codigo))
        codigo += 1
        
        
    
    asignaturas_df = pd.DataFrame(asignaturas_list)

    print("Asignaturas generadas: " + str(len(asignaturas_list)))
    
    asignaturas_df.to_csv (r'./csv/asignaturas.csv', index = False, header=False)

    print("-----------------------------------------------------")
    print("FIN GENERADOR ASIGNATURAS")
    print("-----------------------------------------------------")


def generar_estancia():
    """
    Funcion que genera x estancias aleatoriamente y las exporta a un csv
    """

    print()
    print("-----------------------------------------------------")
    print("INICIO GENERADOR ESTANCIAS")
    print("-----------------------------------------------------")
    
    estudiantes_df = pd.read_csv(r'./csv/estudiantes.csv', delimiter=",", names=["codigo", "nombre", "apellidos", "direccion", "pais", "telefono", "email", "creditos_aprobados", "universidad"])
    universidades_df = pd.read_csv(r'./csv/universidades.csv', delimiter=",", names=["codigo", "nombre", "direccion", "pais", "telefono", "email"])

    for i in range(len(estudiantes_df)):
        
        duracion = duracion_estancia[random.randrange(len(duracion_estancia))]

        fecha_inicio = ""
        fecha_fin = ""

        if duracion == "1":
            fecha_inicio = fechas[0]
            fecha_fin = fechas[1]
        elif duracion == "2":
            fecha_inicio = fechas[1]
            fecha_fin = fechas[2]
        elif duracion == "A":
            fecha_inicio = fechas[0]
            fecha_fin = fechas[2]
        
        destino = universidades_df.iloc[random.randrange(len(universidades_df))]["codigo"]
        #mientras el destino sea igual a la universidad que estudia el estudiante se genera otro
        while destino == estudiantes_df.iloc[i]["universidad"]:
            destino = universidades_df.iloc[random.randrange(len(universidades_df))]["codigo"]
        
        nueva_estancia =  [fecha_inicio, fecha_fin, beca[random.randrange(len(beca))], duracion, random.randrange(501,2001), estudiantes_df.iloc[i]["codigo"], destino]
        
        estancias_list.append(nueva_estancia)

        if (i%(len(estudiantes_df)/10) == 0):
            print("Estancias generadas: " + str(i))
    
    estancias_df = pd.DataFrame(estancias_list)

    print("Estancias generadas: " + str(len(estancias_list)))
    
    estancias_df.to_csv (r'./csv/estancias.csv', index = False, header=False)

    print("-----------------------------------------------------")
    print("FIN GENERADOR ESTANCIAS")
    print("-----------------------------------------------------")

def generar_convalidaciones():
    """
    Funcion que genera x convalidaciones aleatoriamente y las exporta a un csv
    """

    print()
    print("-----------------------------------------------------")
    print("INICIO GENERADOR CONVALIDACIONES")
    print("-----------------------------------------------------")

    asignaturas_df = pd.read_csv(r'./csv/asignaturas.csv', delimiter=",", names=["codigo", "nombre", "creditos", "tipo", "universidad"])
    estancias_df = pd.read_csv(r'./csv/estancias.csv', delimiter=",", names=["fecha_inicio", "fecha_fin", "beca", "duracion", "creditos", "estudiante", "destino"])
    estudiantes_df = pd.read_csv(r'./csv/estudiantes.csv', delimiter=",", names=["codigo", "nombre", "apellidos", "direccion", "pais", "telefono", "email", "creditos_aprobados", "facultad"])

    for i in range(len(estancias_df)):
        if estancias_df.iloc[i]["duracion"] == "A":
            asignaturas_destino = asignaturas_df.loc[asignaturas_df["universidad"] == estancias_df.iloc[i]["destino"]]
            #las asignaturas de origen de la convalidacion son las de la universidad de origen
            asignaturas_origen = asignaturas_df.loc[asignaturas_df["universidad"] == estudiantes_df.iloc[estancias_df.iloc[i]["estudiante"]]["facultad"]]

            for k in range(random.randrange(6,10)):
                nota = random.randrange(len(nota_origen))
                nota_origen_asignada = nota_origen[nota]
                nota_destino_asignada = nota_destino[nota]

                fecha = fechas[random.randrange(1,2)]
                codigo_asignatura_destino = asignaturas_destino.iloc[random.randrange(len(asignaturas_destino))]["codigo"]
                codigo_asignatura_origen = asignaturas_origen.iloc[random.randrange(len(asignaturas_origen))]["codigo"]


                nueva_convalidacion = [nota_destino_asignada, nota_origen_asignada, fecha, estancias_df.iloc[i]["estudiante"], estancias_df.iloc[i]["destino"], codigo_asignatura_origen, codigo_asignatura_destino ]
                convalidaciones_list.append(nueva_convalidacion)

        elif estancias_df.iloc[i]["duracion"] == "1":

            asignaturas_destino = asignaturas_df.loc[asignaturas_df["universidad"] == estancias_df.iloc[i]["destino"]]
            asignaturas_origen = asignaturas_df.loc[asignaturas_df["universidad"] == estudiantes_df.iloc[estancias_df.iloc[i]["estudiante"]]["facultad"]]
            
            for k in range(random.randrange(6,10)):
                nota = random.randrange(len(nota_origen))
                nota_origen_asignada = nota_origen[nota]
                nota_destino_asignada = nota_destino[nota]

                fecha = fechas[1]
                codigo_asignatura_destino = asignaturas_destino.iloc[random.randrange(len(asignaturas_destino))]["codigo"]
                codigo_asignatura_origen = asignaturas_origen.iloc[random.randrange(len(asignaturas_origen))]["codigo"]


                nueva_convalidacion = [nota_destino_asignada, nota_origen_asignada, fecha, estancias_df.iloc[i]["estudiante"], estancias_df.iloc[i]["destino"], codigo_asignatura_origen, codigo_asignatura_destino ]
                convalidaciones_list.append(nueva_convalidacion)

        elif estancias_df.iloc[i]["duracion"] == "2":

            asignaturas_destino = asignaturas_df.loc[asignaturas_df["universidad"] == estancias_df.iloc[i]["destino"]]
            asignaturas_origen = asignaturas_df.loc[asignaturas_df["universidad"] == estudiantes_df.iloc[estancias_df.iloc[i]["estudiante"]]["facultad"]]

            for k in range(random.randrange(6,10)):
                nota = random.randrange(len(nota_origen))
                nota_origen_asignada = nota_origen[nota]
                nota_destino_asignada = nota_destino[nota]

                fecha = fechas[2]
                codigo_asignatura_destino = asignaturas_destino.iloc[random.randrange(len(asignaturas_destino))]["codigo"]
                codigo_asignatura_origen = asignaturas_origen.iloc[random.randrange(len(asignaturas_origen))]["codigo"]


                nueva_convalidacion = [nota_origen_asignada, nota_destino_asignada, fecha, estancias_df.iloc[i]["estudiante"], estancias_df.iloc[i]["destino"], codigo_asignatura_origen, codigo_asignatura_destino ]
                convalidaciones_list.append(nueva_convalidacion)

        if (i%(len(estancias_df)/20) == 0):
            print("Convalidaciones generadas: " + str(i))

    convalidaciones_df = pd.DataFrame(convalidaciones_list)

    print ("Convalidaciones generadas: " + str(len(convalidaciones_list)))
    
    convalidaciones_df.to_csv(r'./csv/convalidaciones.csv', index=False, header=False)

    print("-----------------------------------------------------")
    print("FIN GENERADOR CONVALIDACIONES")
    print("-----------------------------------------------------")
    

#Funciones para generar los datos
def create_phone(): 
         # Segundo dígito 
    second = [3, 4, 5, 7, 8][random.randint(0, 4)] 
         # Tercer dígito 
    third = { 3: random.randint(0, 9), 
        4: [5, 7, 9][random.randint(0, 2)], 
        5: [i for i in range(10) if i != 4][random.randint(0, 8)], 
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)], 
        8: random.randint(0, 9), }[second] 
         # Últimos ocho dígitos 
    suffix = random.randint(9999999,100000000) 
         # Fusionar número de teléfono 
    return "1{}{}{}".format(second, third, suffix)

