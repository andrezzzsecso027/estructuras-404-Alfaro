from ModuloPlaneacion import *
from ModuloProduccion import *
from ModuloAbastecimiento import *
from ModuloDistribuccion import *
from ModuloLogisticaInversa import *
class SistemaSupplyChain:
    def __init__(self):
        self.planeacion = ModuloPlaneacion()
        self.abastecimiento = ModuloAbastecimiento()
        self.produccion = ModuloProduccion()
        self.distribucion = ModuloDistribucion()
        self.logistica_inversa = ModuloLogisticaInversa()

    def menu_principal(self):
        while True:
            mostrar_encabezado("MENÚ PRINCIPAL")

            print("FASES DE LA CADENA DE SUMINISTRO:\n")
            print("1. 📋 PLANEACIÓN - Campañas de Marketing")
            print("2. 🚜 ABASTECIMIENTO - Proveedores de Papa")
            print("3. 🏭 PRODUCCIÓN - Líneas de Fabricación")
            print("4. 🚛 DISTRIBUCIÓN - Rutas de Entrega")
            print("5. 🔄 LOGÍSTICA INVERSA - Devoluciones")
            print("\n6. 🚪 Salir del sistema")
            print("-" * 80)

            opcion = input("Seleccione una fase: ")

            if opcion == "1":
                self.planeacion.menu()
            elif opcion == "2":
                self.abastecimiento.menu()
            elif opcion == "3":
                self.produccion.menu()
            elif opcion == "4":
                self.distribucion.menu()
            elif opcion == "5":
                self.logistica_inversa.menu()
            elif opcion == "6":
                print("\n ¡Gracias por usar el sistema!")
                break
            else:
                print(" Opción no válida")
                pausa()


if __name__ == "__main__":
    sistema = SistemaSupplyChain()
    sistema.menu_principal()