# Archivo: demo_03_if_else.py
"""
Demo 3: Estructuras if-else
Objetivo: Mostrar control de flujo básico
"""

def demo_if_else():
    print("=== Demo: Estructuras if-else ===")
    
    # Ejemplo con calificación
    calificacion = 100
    beca = True
    print(f"Calificación: {calificacion}")
    
    if calificacion >= 90:
        if calificacion == 100 and beca:
            print("Tiene beca completa")
            print("Pertenece al cuadro de honor")
        if beca:
            print("Beca del 90%")
        print("Resultado: Excelente")
    elif calificacion >= 80:
        if beca:
            print("Tiene beca parcial")
        print("Resultado: Muy bien")
    elif calificacion >= 70:
        if beca:
            print("Pierde la beca")
            beca = False
        print("Resultado: Bien")
    elif calificacion >= 60:
        print("Resultado: Suficiente")
    else:
        print("Resultado: Necesita mejorar")

if __name__ == "__main__":
    demo_if_else()