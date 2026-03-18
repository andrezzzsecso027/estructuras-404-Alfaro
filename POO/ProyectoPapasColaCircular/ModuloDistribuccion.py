from ListaCircular import *
from PuntoDistribuccion import *
from UtilidadesSistema import *
import time
from datetime import datetime
class ModuloDistribucion:
    def __init__(self):
        self.puntos = ListaCircular()
        self.inventario_camion = 0
        self._inicializar_puntos()

    def _inicializar_puntos(self):

        puntos_iniciales = [
            PuntoDistribucion("Tienda Centro", "Calle 10 #5-20", 150),
            PuntoDistribucion("Supermercado Norte", "Av. Principal #15-40", 300),
            PuntoDistribucion("Minimarket Sur", "Carrera 8 #3-10", 120),
            PuntoDistribucion("Tienda Barrio Alto", "Barrio Nuevo #12-5", 100)
        ]

        for punto in puntos_iniciales:
            self.puntos.agregar(punto)

    def menu(self):
        while True:
            mostrar_encabezado("FASE 4: DISTRIBUCIÓN - RUTAS DE ENTREGA")

            print(f" Inventario del camión: {self.inventario_camion} kg\n")
            print("1.  Ver todos los puntos de distribución")
            print("2.  Cargar camión")
            print("3. ️  Iniciar ruta de distribución")
            print("4. ️  Ver siguiente punto en ruta")
            print("5.  Ver estadísticas de distribución")
            print("6.  Volver al menú principal")
            print("-" * 80)

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.ver_todos()
            elif opcion == "2":
                self.cargar_camion()
            elif opcion == "3":
                self.iniciar_ruta()
            elif opcion == "4":
                self.siguiente_punto()
            elif opcion == "5":
                self.ver_estadisticas()
            elif opcion == "6":
                break
            else:
                print("️Opción no válida")
                pausa()

    def ver_todos(self):
        mostrar_encabezado("TODOS LOS PUNTOS DE DISTRIBUCIÓN")
        puntos = self.puntos.mostrar()

        for i, punto in enumerate(puntos, 1):
            print(f"{i}. {punto}")
            print(f"   Inventario actual: {punto.inventario_actual} kg")
            if punto.ultima_entrega:
                print(f"   Última entrega: {punto.ultima_entrega}")
            print()

        pausa()

    def cargar_camion(self):
        mostrar_encabezado("CARGAR CAMIÓN")

        try:
            cantidad = int(input("Cantidad a cargar (kg, máx 2000): "))

            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0")
            elif cantidad > 2000:
                print("La capacidad máxima del camión es 2000 kg")
            else:
                print("\n Cargando camión...")
                time.sleep(1)
                print(" Organizando paquetes...")
                time.sleep(1)
                self.inventario_camion = cantidad
                print(f"\n Camión cargado con {cantidad} kg")

        except ValueError:
            print("Debe ingresar un número válido")

        pausa()

    def iniciar_ruta(self):
        if self.inventario_camion == 0:
            print("\n El camión está vacío. Debe cargarlo primero.")
            pausa()
            return

        mostrar_encabezado("INICIANDO RUTA DE DISTRIBUCIÓN")

        print(f" Inventario inicial: {self.inventario_camion} kg")
        print("️  Comenzando ruta circular...\n")
        time.sleep(2)

        puntos = self.puntos.mostrar()

        for i, punto in enumerate(puntos, 1):
            if self.inventario_camion <= 0:
                print("\n ¡Camión sin inventario!")
                print(" Regresando a la fábrica para recargar...")
                time.sleep(2)
                break

            print(f"\n Punto {i}/{len(puntos)}: {punto.nombre}")
            print(f"📍 Dirección: {punto.direccion}")
            time.sleep(2)

            entrega = min(punto.demanda_semanal, self.inventario_camion)

            print(f" Entregando {entrega} kg...")
            time.sleep(2)

            self.inventario_camion -= entrega
            punto.inventario_actual += entrega
            punto.ultima_entrega = datetime.now().strftime("%Y-%m-%d %H:%M")

            print(f" Entrega completada")
            print(f" Inventario del camión: {self.inventario_camion} kg restantes")
            time.sleep(1)

        if self.inventario_camion > 0:
            print(f"\n Ruta completada. Inventario restante: {self.inventario_camion} kg")

        pausa()

    def siguiente_punto(self):
        actual = self.puntos.obtener_actual()

        if actual:
            print(f"\n Siguiente punto: {actual.nombre}")
            print(f" Dirección: {actual.direccion}")
            print(f" Demanda semanal: {actual.demanda_semanal} kg")
            self.puntos.rotar()

        pausa()

    def ver_estadisticas(self):
        mostrar_encabezado("ESTADÍSTICAS DE DISTRIBUCIÓN")
        puntos = self.puntos.mostrar()

        total_inventario = sum(p.inventario_actual for p in puntos)
        total_demanda = sum(p.demanda_semanal for p in puntos)

        print(f" Total en puntos de venta: {total_inventario} kg")
        print(f" Demanda semanal total: {total_demanda} kg\n")
        print("Inventario por punto:\n")

        for punto in puntos:
            cobertura = (punto.inventario_actual / punto.demanda_semanal * 100) if punto.demanda_semanal > 0 else 0
            barra = "█" * int(cobertura / 5)
            print(f"{punto.nombre:25} | {punto.inventario_actual:4} kg | Cobertura: {cobertura:5.1f}% | {barra}")

        pausa()