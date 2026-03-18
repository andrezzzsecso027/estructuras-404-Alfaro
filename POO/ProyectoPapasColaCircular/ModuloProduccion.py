from ListaCircular import *
from LineaProduccionPapas import *
from UtilidadesSistema import *
import time
class ModuloProduccion:
    def __init__(self):
        self.lineas = ListaCircular()
        self._inicializar_lineas()

    def _inicializar_lineas(self):

        lineas_iniciales = [
            LineaProduccion("Línea A", "Frituras Lisas", 200),
            LineaProduccion("Línea B", "Frituras Onduladas", 180),
            LineaProduccion("Línea C", "Chips Delgados", 150),
            LineaProduccion("Línea D", "Papas Artesanales", 100)
        ]

        for linea in lineas_iniciales:
            self.lineas.agregar(linea)

    def menu(self):
        while True:
            mostrar_encabezado("FASE 3: PRODUCCIÓN - LÍNEAS DE FABRICACIÓN")

            print("1.  Ver todas las líneas")
            print("2.  Ver línea actual")
            print("3. ️  Iniciar producción en línea actual")
            print("4. ️  Rotar a siguiente línea")
            print("5.  Ver estadísticas de producción")
            print("6.  Volver al menú principal")
            print("-" * 80)

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.ver_todas()
            elif opcion == "2":
                self.ver_actual()
            elif opcion == "3":
                self.iniciar_produccion()
            elif opcion == "4":
                self.rotar()
            elif opcion == "5":
                self.ver_estadisticas()
            elif opcion == "6":
                break
            else:
                print("  Opción no válida")
                pausa()

    def ver_todas(self):
        mostrar_encabezado("TODAS LAS LÍNEAS DE PRODUCCIÓN")
        lineas = self.lineas.mostrar()

        for i, linea in enumerate(lineas, 1):
            print(f"{i}. {linea}")
            print(f"   Total producido: {linea.total_producido} kg\n")

        pausa()

    def ver_actual(self):
        mostrar_encabezado("LÍNEA ACTUAL EN ROTACIÓN")
        actual = self.lineas.obtener_actual()

        if actual:
            print(f"Línea: {actual.nombre}")
            print(f" Producto: {actual.tipo_producto}")
            print(f" Capacidad: {actual.capacidad_hora} kg/hora")
            print(f" Estado: {'🔴 Ocupada' if actual.ocupada else '🟢 Libre'}")
            print(f" Total producido: {actual.total_producido} kg")

        pausa()

    def iniciar_produccion(self):
        actual = self.lineas.obtener_actual()

        if actual:
            if actual.ocupada:
                print(f" La línea '{actual.nombre}' está ocupada")
                pausa()
                return

            print(f"\n Línea seleccionada: {actual.nombre}")
            print(f" Producto: {actual.tipo_producto}")

            try:
                horas = int(input("Horas de producción (1-8): "))

                if horas <= 0 or horas > 8:
                    print(" Las horas deben estar entre 1 y 8")
                else:
                    actual.ocupada = True
                    cantidad_total = actual.capacidad_hora * horas

                    print(f"\n  INICIANDO PRODUCCIÓN DE {actual.tipo_producto}")
                    print(f"  Duración: {horas} hora(s)")
                    print(f" Cantidad estimada: {cantidad_total} kg\n")
                    print("-" * 80)

                    for hora in range(1, horas + 1):
                        print(f" Hora {hora}/{horas}: Produciendo {actual.tipo_producto}...")
                        time.sleep(2)
                        producido = actual.capacidad_hora
                        actual.total_producido += producido
                        print(f" Producidos: {producido} kg (Total acumulado: {actual.total_producido} kg)")

                    print("-" * 80)
                    print(f"\n ¡Producción completada!")
                    print(f" Total producido en esta sesión: {cantidad_total} kg")
                    actual.ocupada = False

            except ValueError:
                print(" Debe ingresar un número válido")

        pausa()

    def rotar(self):
        self.lineas.rotar()
        actual = self.lineas.obtener_actual()
        print(f"\n➡️  Rotado a: {actual.nombre} ({actual.tipo_producto})")
        pausa()

    def ver_estadisticas(self):
        mostrar_encabezado("ESTADÍSTICAS DE PRODUCCIÓN")
        lineas = self.lineas.mostrar()

        total_general = sum(l.total_producido for l in lineas)

        print(f"📊 Total producido: {total_general} kg\n")
        print("Distribución por línea:\n")

        for linea in lineas:
            porcentaje = (linea.total_producido / total_general * 100) if total_general > 0 else 0
            barra = "█" * int(porcentaje / 2)
            print(f"{linea.tipo_producto:25} | {linea.total_producido:6} kg | {porcentaje:5.1f}% | {barra}")

        pausa()