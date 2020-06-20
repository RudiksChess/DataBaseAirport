"""
@author: Rudik Roberto Rompich
@carnet: 19857
@clase: Herramientas Tecnologicas

Ejercicio 8 : Base de datos y relaciones

"""


import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


datos = pd.read_csv('datosactividad.csv')
f = open('registro.txt','w')





def Reservar(numero):

    condicion = pd.to_numeric(datos.loc[datos["ID"] == numero, "Seats"])
    if  condicion.values !=0:
          datos.loc[datos["ID"] == numero, "Seats"] -= 1
          f.write("\n Se ha hecho una reserva en el vuelo: "+str(numero)+"\n")
          f.write(str(datos.loc[datos['ID'] == numero]))
          print("\nSe ha hecho una reserva en el vuelo: "+str(numero)+"\n")
          print(str(datos.loc[datos['ID'] == numero]))

    else:
          print("No hay espacios disponibles. No se ha reservado. \n")



def ModificarReserva(numero, nuevo):
    condicion = pd.to_numeric(datos.loc[datos["ID"] == nuevo, "Seats"])

    if condicion.values != 0:

        datos.loc[datos["ID"] == numero, "Seats"] += 1
        datos.loc[datos["ID"] == nuevo, "Seats"] -= 1
        f.write("\nSe ha cancelado la anterior reserva y se ha reservado el nuevo vuelo: "+str(nuevo)+"\n")
        f.write(str(datos.loc[datos['ID'] == nuevo]))

        print("\nSe ha cancelado la anterior reserva y se ha reservado el nuevo vuelo: "+str(nuevo)+"\n")
        print(str(datos.loc[datos['ID'] == nuevo]))

    else:

        print("No hay espacios disponibles. No se ha reservado y no se ha modificado su anterior reserva. \n")

def EliminarReserva(numero):

     datos.loc[datos["ID"] == numero, "Seats"] += 1

     f.write("\nSe ha eliminado la reserva del vuelo: "+str(numero)+"\n")
     f.write(str(datos.loc[datos['ID'] == numero]))

     print("Se ha eliminado la reserva.")


def AgregarConexion(ID,Airline,Origin,Destination,Flight,Departure,Duration,Arrival,Seats):
    global datos

    verificacion= datos.loc[datos["ID"] == ID, "ID"]
    condicion = verificacion.values

    if ID == condicion:

        print("Este número de iD ya existe. Volver a repetir el proceso, por favor.")
    else:
        data2 = pd.DataFrame.from_records({"ID": ID,"Airline": Airline,"Origin":Origin,"Destination":Destination,"Flight":Flight,"Departure":Departure,"Duration":Duration,"Arrival":Arrival,"Seats":Seats},index=[50])
        datos = datos.append(data2)
        f.write("\nSe ha agregado una nueva conexión de vuelo: "+str(ID)+"\n")
        f.write(str(datos.loc[datos['ID'] == ID]))
        print("Se ha asignado con existo una nueva conexión")
        print(str(datos.loc[datos['ID'] == ID]))

def ModificarConexion(ID,Airline,Origin,Destination,Flight,Departure,Duration,Arrival,Seats):
    datos.loc[datos["ID"] ==ID, "Airline"]= Airline
    datos.loc[datos["ID"] ==ID, "Origin"]= Origin
    datos.loc[datos["ID"] ==ID, "Destination"]= Destination
    datos.loc[datos["ID"] ==ID, "Flight"]= Flight
    datos.loc[datos["ID"] ==ID, "Departure"]= Departure
    datos.loc[datos["ID"] ==ID, "Duration"]= Duration
    datos.loc[datos["ID"] ==ID, "Arrival"]= Arrival
    datos.loc[datos["ID"] ==ID, "Seats"]= Seats

    f.write("\nSe ha modificado la conexión del vuelo: "+str(ID)+"\n")
    f.write(str(datos.loc[datos['ID'] == ID]))
    print("Se ha modificado con éxito la  conexión")
    print(str(datos.loc[datos['ID'] == ID]))


def EliminarConexion(ID):
    global datos
    datos = datos[datos.ID != ID]

    f.write("\nSe ha eliminado la conexión del vuelo: "+str(ID)+"\n")

    print("Se ha eliminado con éxito la  conexión")



def GenerarTXT():
    f.close()

def GenerarExcel():
    datos.to_csv("DATOSFINALES.csv", sep=',', index= False)


lol = int(input("\n|BIENVENIDO AL CONTROLADOR DE VUELOS | \n" +

                "SELECCIONE UNA ACCIÓN PARA REALIZAR: \n\n" +
                "1. MOSTRAR VUELOS DISPONIBLES \n\n" +

                "2. Realizar una reserva \n" +
                "3. Modificar una reserva \n" +
                "4. Eliminar una reserva  \n" +
                "5. Agregar una conexión entre ciudades \n" +
                "6. Eliminar una conexión entre ciudades  \n" +
                "7. Modificar una conexión entre ciudades  \n" +
                "8. Generar registro de acciones realizadas  \n" +
                "9. Generar archivo Excel \n" +
                "0. Salir \n\n" +
                "OPCIÓN:"))

while lol != 0:

        if lol == 1:
            print(datos)

        elif lol == 2:
            w = int(input("¿En qué vuelo quiere hacer una reservación?: "))
            Reservar(w)


        elif lol == 3:
            w = int(input("¿Qué reserva de vuelo quiere modificar?: "))
            x = int(input("¿En qué vuelo quiere hacer una reservación?: "))
            ModificarReserva(w,x)

        elif lol == 4:
            w = int(input("¿Qué reserva vuelo quiere eliminar?: "))
            EliminarReserva(w)

        elif lol == 5:
            x1 = int(input("Asignar ID: "))
            x2 = str(input("Asignar Airline: "))
            x3 = str(input("Asignar Origin: "))
            x4 = str(input("Asignar Destination: "))
            x5 = str(input("Asignar Flight:: "))
            x6 = str(input("Asignar Departure: "))
            x7 = str(input("Asignar Duration: "))
            x8 = str(input("Asignar Arrival: "))
            x9 = str(input("Asignar Seats: "))
            AgregarConexion(x1,x2,x3,x4,x5,x6,x7,x8,x9)

        elif lol == 6:
            x1 = int(input("¿Cuál es el ID del vuelo que quiere eliminar?: "))

            EliminarConexion(x1)


        elif lol == 7:
            x1 = int(input("¿Cuál es el ID del vuelo que quiere modificar?: "))
            x2 = str(input("Asignar Airline: "))
            x3 = str(input("Asignar Origin: "))
            x4 = str(input("Asignar Destination: "))
            x5 = str(input("Asignar Flight:: "))
            x6 = str(input("Asignar Departure: "))
            x7 = str(input("Asignar Duration: "))
            x8 = str(input("Asignar Arrival: "))
            x9 = str(input("Asignar Seats: "))
            ModificarConexion(x1,x2,x3,x4,x5,x6,x7,x8,x9)
        elif lol == 8:

            GenerarTXT()

        elif lol == 9:
            GenerarExcel()





        else:

            print("Vuelva a ingresar un valor válido")

        lol = int(input("\n|BIENVENIDO AL CONTROLADOR DE VUELOS | \n" +

                        "SELECCIONE UNA ACCIÓN PARA REALIZAR: \n\n" +
                        "1. MOSTRAR VUELOS DISPONIBLES \n\n" +

                        "2. Realizar una reserva \n" +
                        "3. Modificar una reserva \n" +
                        "4. Eliminar una reserva  \n" +
                        "5. Agregar una conexión entre ciudades \n" +
                        "6. Eliminar una conexión entre ciudades  \n" +
                        "7. Modificar una conexión entre ciudades  \n" +
                        "8. Generar registro de acciones realizadas  \n" +
                        "9. Generar archivo Excel \n" +
                        "0. Salir \n\n" +
                        "OPCIÓN:"))
