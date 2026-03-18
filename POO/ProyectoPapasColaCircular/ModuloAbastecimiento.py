from ListaCircular import *
from Proveedor import *
from UtilidadesSistema import mostrar_encabezado,pausa
import time
class ModuloAbastecimiento:
    def __init__(self):
        self.proveedores = ListaCircular()
        self._inicializar_proveedores()

    def _inicializar_proveedores(self):

        proveedores_iniciales = [
            Proveedor("Finca El Rosal", "Vereda San José", 500),
            Proveedor("Finca La Esperanza", "Vereda La Palma", 800),
            Proveedor("Finca Los Pinos", "Vereda El Carmen", 600),
            Proveedor("Finca Santa Rita", "Vereda Arrayanes", 700),
            Proveedor("Finca Villa Nueva", "Vereda Chorreras", 550)
        ]

        for proveedor in proveedores_iniciales:
            self.proveedores.agregar(proveedor)

    def menu(self):
        while True:
            mostrar_encabezado("FASE 2: ABASTECIMIENTO - PROVEEDORES ROTATIVOS")

            print("1. 📋 Ver todos los proveedores")
            print("2. 🎯 Ver proveedor actual")
            print("3. 📦 Realizar pedido al proveedor actual")
            print("4. ➡️  Rotar a siguiente proveedor")
            print("5. 📊 Ver estadísticas de abastecimiento")
            print("6. 🔙 Volver al menú principal")
            print("-" * 80)

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.ver_todos()
            elif opcion == "2":
                self.ver_actual()
            elif opcion == "3":
                self.realizar_pedido()
            elif opcion == "4":
                self.rotar()
            elif opcion == "5":
                self.ver_estadisticas()
            elif opcion == "6":
                break
            else:
                print(" Opción no válida")
                pausa()

    def ver_todos(self):
        mostrar_encabezado("TODOS LOS PROVEEDORES")
        proveedores = self.proveedores.mostrar()

        for i, proveedor in enumerate(proveedores, 1):
            print(f"{i}. {proveedor}")
            print(f"   Total suministrado: {proveedor.total_suministrado} kg\n")

        pausa()

    def ver_actual(self):
        mostrar_encabezado("PROVEEDOR ACTUAL EN ROTACIÓN")
        actual = self.proveedores.obtener_actual()

        if actual:
            print(f" Proveedor: {actual.nombre}")
            print(f" Ubicación: {actual.ubicacion}")
            print(f" Capacidad: {actual.capacidad_kg} kg")
            print(f" Estado: {' Disponible' if actual.disponible else ' No disponible'}")
            print(f" Total suministrado: {actual.total_suministrado} kg")

        pausa()

    def realizar_pedido(self):
        actual = self.proveedores.obtener_actual()

        if actual:
            if not actual.disponible:
                print(f" El proveedor '{actual.nombre}' no está disponible")
                pausa()
                return

            print(f"\n📦 Realizando pedido a: {actual.nombre}")
            print(f"Capacidad disponible: {actual.capacidad_kg} kg")

            try:
                cantidad = int(input("Cantidad a pedir (kg): "))

                if cantidad <= 0:
                    print(" La cantidad debe ser mayor a 0")
                elif cantidad > actual.capacidad_kg:
                    print(f" La cantidad excede la capacidad del proveedor ({actual.capacidad_kg} kg)")
                else:
                    print(f"\n Procesando pedido...")
                    time.sleep(1)
                    print(" Contactando al proveedor...")
                    time.sleep(1)
                    print(" Pedido confirmado")
                    time.sleep(1)
                    print(" Programando recolección...")
                    time.sleep(1)

                    actual.total_suministrado += cantidad
                    print(f"\n✅ ¡Pedido de {cantidad} kg realizado exitosamente!")
                    print(f"📊 Total acumulado de {actual.nombre}: {actual.total_suministrado} kg")

            except ValueError:
                print(" Debe ingresar un número válido")

        pausa()

    def rotar(self):
        self.proveedores.rotar()
        actual = self.proveedores.obtener_actual()
        print(f"\n  Rotado a: {actual.nombre}")
        pausa()

    def ver_estadisticas(self):
        mostrar_encabezado("ESTADÍSTICAS DE ABASTECIMIENTO")
        proveedores = self.proveedores.mostrar()

        total_general = sum(p.total_suministrado for p in proveedores)

        print(f"📊 Total abastecido: {total_general} kg\n")
        print("Distribución por proveedor:\n")

        for proveedor in proveedores:
            porcentaje = (proveedor.total_suministrado / total_general * 100) if total_general > 0 else 0
            barra = "█" * int(porcentaje / 2)
            print(f"{proveedor.nombre:25} | {proveedor.total_suministrado:6} kg | {porcentaje:5.1f}% | {barra}")

        pausa()