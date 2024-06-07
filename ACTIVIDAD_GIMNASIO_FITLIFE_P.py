import os
import msvcrt
import csv
#FUNCION PARA CREAR TÍTULOS
def titulo(texto:str):
    os.system("cls")
    print(f"\033[35m{texto.upper()}\033[0m")
def error(texto:str):
    print(f"\033[31m{texto.upper()}\033[0m")
def exito(texto:str):
    print(f"\033[32m{texto.upper()}\033[0m")
#TUPLAS - CLASES
clases=[
    ("PESAS","LUN-MIE 8:30-10:00AM",10),
    ("ZUMBA","MAR-JUE 3:30-5:40PM",20),
    ("NUTRICIÓN","VIE 6:00-7:30",2),
    ("CROSSFIT","SAB 11:30-12:55PM",10)]
#DICCIONARIO - USUARIOS
usuarios={}
#LISTA - RESERVAS
reservas=[]
#CONTADOR ID DE USUARIO
numero_usuario=100
#INICIAR EL SISTEMA
print("<<PRESS ANY KEY>>")
msvcrt.getch()
os.system("cls")
while True:
    print("\033[35m═══════════════════════════════════")
    print("     SISTEMA GESTIÓN FITLIFE       ")
    print("═══════════════════════════════════\033[0m")
    print("1) REGISTRAR USUARIO")
    print("2) RESERVAR CLASES")
    print("3) CONSULTAR CLASES DISPONIBLES")
    print("4) CONSULTAR RESERVAS DE USUARIO")
    print("5) CONSULTAR USUARIOS")
    print("0) SALIR")
    print("\033[35m═══════════════════════════════════\033[0m")
    opcion=input("SELECCIONE: ")
    if opcion=="0":
        titulo("ADIOS")
        break
    elif opcion=="1":
        titulo("REGISTRAR USUARIO")
        nombre=input("INGRESE NOMBRE DE USUARIO: ").upper()
        #VALIDAR QUE EL NOMBRE DE USURIO NO SE REPITA
        if nombre not in usuarios.values():
            usuarios[numero_usuario]=nombre
            exito(f"USUARIO REGISTRADO CON ÉXITO. SU ID ES: {numero_usuario}")
            numero_usuario+=100
        else:
            error("EL USUARIO YA SE ENCUENTRA REGISTRADO")
    elif opcion=="2":
        titulo("RESERVAR CLASES")
        codigo=int(input("INGRESE CODIGO DE USUARIO: "))
        if codigo in usuarios:
            curso=input("INGRESE NOMBRE PARA INSCRIBIRSE: ").upper()
            centinela=False
            centinela_cupos=False
            for c in clases:
                if c[0]==curso:
                    centinela=True
                    if c[2]>0:
                        centinela_cupos=True
                        reservas.append([codigo,usuarios[codigo],c[0],c[1]])
                        exito("RESERVA REALIZADA CON ÉXITO")
                        #DESCONTAR CUPO
                        actualizacion_cupo=(c[0],c[1],c[2]-1)
                        clases.remove(c)
                        clases.append(actualizacion_cupo)
                        with open('ACTIVIDAD 19/reservas.csv','w',newline='',encoding='utf-8') as f:
                            escribir=csv.writer(f,delimiter=',')
                            escribir.writerows(reservas)
                        break
            if not centinela:
                error("EL CURSO NO EXISTE")
            if not centinela_cupos:
                error("NO QUEDAN CUPOS DISPONIBLES PARA LA CLASE")
        else:
            error("EL CODIGO DE USUARIO NO SE ENCUENTRA REGISTRADO")
    elif opcion=="3":
        titulo("CONSULTAR CLASES DISPONIBLES")
        for c in clases:
            print(f"{c[0]}\nHORARIO: {c[1]}\nCUPOS: {c[2]}")
            print("═════════════════════════")
    elif opcion=="4":
        titulo("CONSULTAR RESERVAS DE USUARIO")
        if len(reservas)>0:
            condigo=int(input("INGRESE CODIGO DEL USUARIO: "))
            centinela=False
            for r in reservas:
                if r[0]==codigo:
                    print(f"{r[0]} {r[1]}\nCURSO: {r[2]}\nHORARIO: {r[3]}")
                    print("═════════════════════════════")
                    centinela=True
            if not centinela:
                error("EL CODIGO NO TIENE RESERVAS ASOCIADAS")
        else:
            error("NO EXISTEN RESERVAS")
    elif opcion=="5":
        titulo("CONSULTAR USUARIOS")
        if len(usuarios)>0:
            for u in usuarios:
                print(f"{u} : {usuarios[u]}")
        else:
            error("NO HAY USUARIOS REGISTRADOS")
    else:
        error("OPCIÓN NO VALIDA")