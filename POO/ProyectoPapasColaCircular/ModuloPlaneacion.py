from POO.ProyectoPapasColaCircular.ListaCircular import ListaCircular
from ListaCircular import ListaCircular
from CampañaMarketing import CampañaMarketing
from UtilidadesSistema import mostrar_encabezado,pausa
import time
class ModuloPlaneacion:
    def __init__(self):
        self.campañas = ListaCircular()
        self._inicializar_campañas()

    def _inicializar_campañas(self):

        campañas_iniciales = [
            CampañaMarketing("Campaña Cosecha", "Marzo-Abril", "Promoción temporada de cosecha"),
            CampañaMarketing("Campaña Escolar", "Enero-Febrero", "Loncheras escolares"),
            CampañaMarketing("Campaña Navideña", "Diciembre", "Paquetes familiares"),
            CampañaMarketing("Feria Agrícola", "Julio", "Presencia en ferias regionales"),
            CampañaMarketing("Día de la Papa", "Mayo", "Celebración nacional")
        ]

        for campaña in campañas_iniciales:
            self.campañas.agregar(campaña)

    def menu(self):
        while True:
            mostrar_encabezado("FASE 1: PLANEACIÓN - CAMPAÑAS DE MARKETING")

            print("1.  Ver todas las campañas")
            print("2. ️  Ver campaña actual")
            print("3.  Ejecutar campaña actual")
            print("4. ️  Rotar a siguiente campaña")
            print("5.  Agregar nueva campaña")
            print("6.  Volver al menú principal")
            print("-" * 80)

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.ver_todas()
            elif opcion == "2":
                self.ver_actual()
            elif opcion == "3":
                self.ejecutar_actual()
            elif opcion == "4":
                self.rotar()
            elif opcion == "5":
                self.agregar_campaña()
            elif opcion == "6":
                break
            else:
                print("️ Opción no válida")
                pausa()

    def ver_todas(self):
        mostrar_encabezado("TODAS LAS CAMPAÑAS DE MARKETING")
        campañas = self.campañas.mostrar()

        for i, campaña in enumerate(campañas, 1):
            print(f"{i}. {campaña}")

        pausa()

    def ver_actual(self):
        mostrar_encabezado("CAMPAÑA ACTUAL EN ROTACIÓN")
        actual = self.campañas.obtener_actual()

        if actual:
            print(f" Campaña actual: {actual.nombre}")
            print(f" Mes: {actual.mes}")
            print(f" Descripción: {actual.descripcion}")
            print(f" Estado: {' Ejecutada' if actual.ejecutada else ' Pendiente'}")

        pausa()

    def ejecutar_actual(self):
        actual = self.campañas.obtener_actual()

        if actual:
            if actual.ejecutada:
                print(f"  La campaña '{actual.nombre}' ya fue ejecutada")
            else:
                print(f"\n Ejecutando campaña: {actual.nombre}")
                time.sleep(1)
                print(" Preparando materiales...")
                time.sleep(1)
                print(" Lanzando en redes sociales...")
                time.sleep(1)
                print(" Campaña en puntos de venta...")
                time.sleep(1)
                actual.ejecutada = True
                print(f"\n ¡Campaña '{actual.nombre}' ejecutada exitosamente!")

        pausa()

    def rotar(self):
        self.campañas.rotar()
        actual = self.campañas.obtener_actual()
        print(f"\n  Rotado a: {actual.nombre}")
        pausa()

    def agregar_campaña(self):
        mostrar_encabezado("AGREGAR NUEVA CAMPAÑA")

        nombre = input("Nombre de la campaña: ")
        mes = input("Mes(es) de ejecución: ")
        descripcion = input("Descripción: ")

        nueva = CampañaMarketing(nombre, mes, descripcion)
        self.campañas.agregar(nueva)

        print(f"\n Campaña '{nombre}' agregada exitosamente")
        pausa()