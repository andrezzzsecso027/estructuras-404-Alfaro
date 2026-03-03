from datetime import datetime
from ListaTurnos import ListaTurnos
from Persona import Persona
from Usuario import Usuario
from ListaHorarios import ListaHorarios



class SistemaTransito:
    def __init__(self):
        self.horarios = ListaHorarios()
        self.turnos = ListaTurnos()
        self.inicializar_horarios()

    def inicializar_horarios(self):

        horarios = [9, 10, 11, 12, 13, 14, 15, 16]

        for hora in horarios:
            self.horarios.agregar_horario(hora)


    def menu_principal(self):
        while True:
            print("\n" + "=" * 60)
            print("🚦 AGENCIA DE TRÁNSITO - SISTEMA DE TURNOS")
            print("=" * 60)
            print("1. 👤 Usuario (Agendar turno)")
            print("2. 👨‍💼 Funcionario (Gestionar turnos)")
            print("3. 🚪 Salir")
            print("=" * 60)

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.menu_usuario()
            elif opcion == "2":
                self.menu_funcionario()
            elif opcion == "3":
                print("Gracias por usar el sistema!")
                break
            else:
                print(" Opción no válida")

    def menu_usuario(self):

        print("\n" + "=" * 60)
        print("👤 MÓDULO DE USUARIO - AGENDAR TURNO")
        print("=" * 60)

        if self.horarios.esta_vacia():
            print(" Lo sentimos, no hay horarios disponibles para hoy")
            input("\nPresione Enter para continuar...")
            return


        nombre = input("Nombre completo: ")
        cedula = input("Cédula: ")

        print("\nTipo de trámite:")
        print("1. Licencia de conducción")
        print("2. Pase")
        print("3. Traspaso")
        print("4. Duplicado")
        print("5. Comparendo")
        print("6. Otro")

        tramites = {
            "1": "Licencia de conducción",
            "2": "Pase",
            "3": "Traspaso",
            "4": "Duplicado",
            "5": "Comparendo",
            "6": "Otro"
        }

        opcion_tramite = input("Seleccione el trámite (1-6): ")
        tramite = tramites.get(opcion_tramite, "General")

        if not self.horarios.mostrar_horarios():
            return

        try:
            num_horario = int(input("\nSeleccione el número del horario: "))
            hora_seleccionada = self.horarios.seleccionar_horario(num_horario)

            if hora_seleccionada is None:
                print(" Horario no válido")
                input("\nPresione Enter para continuar...")
                return

            usuario = Usuario(nombre, cedula, hora_seleccionada, tramite)
            self.turnos.agregar_turno(usuario)

            print("\n" + "=" * 60)
            print("✅ TURNO AGENDADO EXITOSAMENTE")
            print("=" * 60)
            print(f"Nombre: {nombre}")
            print(f"Cédula: {cedula}")
            print(f"Hora: {hora_seleccionada}:00 hrs")
            print(f"Trámite: {tramite}")
            print("=" * 60)

        except ValueError:
            print(" Debe ingresar un número válido")

        input("\nPresione Enter para continuar...")

    def menu_funcionario(self):

        while True:
            print("\n" + "=" * 60)
            print("👨‍💼 MÓDULO DE FUNCIONARIO")
            print("=" * 60)
            print("1. 📋 Ver todos los turnos (resumido)")
            print("2. ✅ Atender siguiente turno")
            print("3. 👁️  Navegar entre turnos (visualizar)")
            print("4. 🚪 Volver al menú principal")
            print("=" * 60)

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.turnos.mostrar_turnos_resumido()
                input("\nPresione Enter para continuar...")
            elif opcion == "2":
                self.atender_turno()
            elif opcion == "3":
                self.navegar_turnos()
            elif opcion == "4":
                break
            else:
                print(" Opción no válida")

    def atender_turno(self):
        turno = self.turnos.obtener_primer_pendiente()

        if turno is None:
            print("\nNo hay turnos pendientes por atender")
            input("\nPresione Enter para continuar...")
            return

        print("\n" + "=" * 60)
        print(" ATENDIENDO TURNO")
        print("=" * 60)
        print(f"Cliente: {turno.usuario.nombre}")
        print(f"Cédula: {turno.usuario.cedula}")
        print(f"Hora: {turno.usuario.hora_turno}:00 hrs")
        print(f"Trámite: {turno.usuario.tramite}")
        print("=" * 60)

        confirmacion = input("\n¿Marcar como atendido? (s/n): ")

        if confirmacion.lower() == 's':
            turno.usuario.atendido = True
            print("Turno marcado como atendido")
        else:
            print(" Operación cancelada")

        input("\nPresione Enter para continuar...")

    def navegar_turnos(self):

        if self.turnos.esta_vacia():
            print("\n No hay turnos para visualizar")
            input("\nPresione Enter para continuar...")
            return

        actual = self.turnos.cabeza
        posicion = 1

        while True:

            temp = self.turnos.cabeza
            pos = 1
            while temp != actual:
                temp = temp.siguiente
                pos += 1

            print("\n" + "=" * 60)
            estado = " Atendido" if actual.usuario.atendido else " pendiente"
            print(f"Turno #{pos}/{self.turnos.cantidad} - {estado}")
            print("=" * 60)
            print(f"Cliente: {actual.usuario.nombre}")
            print(f"Cédula: {actual.usuario.cedula}")
            print(f"Hora: {actual.usuario.hora_turno}:00 hrs")
            print(f"Trámite: {actual.usuario.tramite}")
            print("=" * 60)

            print("\nNavegación:")
            if actual.anterior:
                print("  [A] ← Anterior")
            if actual.siguiente:
                print("  [S] → Siguiente")
            print("  [Q] Salir de navegación")

            opcion = input("\nElija una opción: ").upper()

            if opcion == 'A' and actual.anterior:
                actual = actual.anterior
            elif opcion == 'S' and actual.siguiente:
                actual = actual.siguiente
            elif opcion == 'Q':
                break
            else:
                print("Opción no válida")
                input("\nPresione Enter para continuar...")


if __name__ == "__main__":

    sistema = SistemaTransito()
    sistema.menu_principal()