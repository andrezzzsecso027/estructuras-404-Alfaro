from ListaCircular import *
from TipoDevolucion import *
from UtilidadesSistema import *
import time
class ModuloLogisticaInversa:
    def __init__(self):
        self.tipos_devolucion = ListaCircular()
        self._inicializar_tipos()

    def _inicializar_tipos(self):

        tipos_iniciales = [
            TipoDevolucion("Producto Vencido", "Destrucción y registro de pérdida"),
            TipoDevolucion("Empaque Defectuoso", "Re-empaque en planta"),
            TipoDevolucion("Error de Distribución", "Re-distribuir a punto correcto"),
            TipoDevolucion("Producto Dañado", "Evaluación y clasificación")
        ]

        for tipo in tipos_iniciales:
            self.tipos_devolucion.agregar(tipo)

    def menu(self):
        while True:
            mostrar_encabezado("FASE 5: LOGÍSTICA INVERSA - DEVOLUCIONES")

            print("1.  Ver tipos de devolución")
            print("2.  Ver tipo actual en análisis")
            print("3.  Registrar nueva devolución")
            print("4. ️  Rotar a siguiente tipo")
            print("5.  Ver estadísticas de devoluciones")
            print("6.  Volver al menú principal")
            print("-" * 80)

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.ver_todos()
            elif opcion == "2":
                self.ver_actual()
            elif opcion == "3":
                self.registrar_devolucion()
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
        mostrar_encabezado("TIPOS DE DEVOLUCIÓN")
        tipos = self.tipos_devolucion.mostrar()

        for i, tipo in enumerate(tipos, 1):
            print(f"{i}. {tipo}")
            print(f"   Proceso: {tipo.proceso}\n")

        pausa()

    def ver_actual(self):
        mostrar_encabezado("TIPO ACTUAL EN ANÁLISIS")
        actual = self.tipos_devolucion.obtener_actual()

        if actual:
            print(f" Tipo: {actual.tipo}")
            print(f"️  Proceso: {actual.proceso}")
            print(f" Casos registrados: {actual.cantidad_registrada}")

        pausa()

    def registrar_devolucion(self):
        actual = self.tipos_devolucion.obtener_actual()

        if actual:
            print(f"\n Registrando devolución: {actual.tipo}\n")

            try:
                cantidad = int(input("Cantidad de unidades devueltas: "))

                if cantidad <= 0:
                    print(" La cantidad debe ser mayor a 0")
                else:
                    print(f"\n Procesando devolución de tipo '{actual.tipo}'...")
                    time.sleep(1)
                    print(f" Registrando en sistema...")
                    time.sleep(1)
                    print(f" Aplicando proceso: {actual.proceso}")
                    time.sleep(2)

                    actual.cantidad_registrada += cantidad

                    print(f"\n Devolución registrada exitosamente")
                    print(f" Total de casos de '{actual.tipo}': {actual.cantidad_registrada}")

            except ValueError:
                print(" Debe ingresar un número válido")

        pausa()

    def rotar(self):
        self.tipos_devolucion.rotar()
        actual = self.tipos_devolucion.obtener_actual()
        print(f"\n  Rotado a: {actual.tipo}")
        pausa()

    def ver_estadisticas(self):
        mostrar_encabezado("ESTADÍSTICAS DE DEVOLUCIONES")
        tipos = self.tipos_devolucion.mostrar()

        total = sum(t.cantidad_registrada for t in tipos)

        print(f" Total de devoluciones: {total} casos\n")

        if total > 0:
            print("Distribución por tipo:\n")

            for tipo in tipos:
                porcentaje = (tipo.cantidad_registrada / total * 100) if total > 0 else 0
                barra = "█" * int(porcentaje / 2)
                print(f"{tipo.tipo:25} | {tipo.cantidad_registrada:4} casos | {porcentaje:5.1f}% | {barra}")
        else:
            print("No hay devoluciones registradas aún.")

        pausa()