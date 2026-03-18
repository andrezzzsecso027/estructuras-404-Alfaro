import os
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausa():
    input("\n[Presione Enter para continuar...]")

def mostrar_encabezado(titulo):
    limpiar_pantalla()
    print("=" * 80)
    print(f"🥔 SISTEMA DE SUPPLY CHAIN - AGROINDUSTRIA DE PAPA DEL SUMAPAZ")
    print("=" * 80)
    print(f"\n📌 {titulo}\n")
    print("-" * 80)
