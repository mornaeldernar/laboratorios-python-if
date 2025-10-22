# Archivo: demo_01_comparaciones.py
"""
Demo 1: Operadores de Comparación
Objetivo: Mostrar el uso básico de operadores de comparación
"""

def demo_comparaciones():
    # Ejemplo 1: Comparaciones básicas
    edad = 25
    edad_minima = 18
    
    print("=== Demo: Operadores de Comparación ===")
    print(f"Edad: {edad}")
    print(f"Edad mínima: {edad_minima}")
    print(f"¿Es mayor de edad? {edad >= edad_minima}")
    print(f"¿Es menor de edad? {edad < edad_minima}")
    
    # Ejemplo 2: Comparación de precios
    precio = 100
    precio_oferta = 100
    
    print(f"\nPrecio regular: ${precio}")
    print(f"Precio oferta: ${precio_oferta}")
    print(f"¿Está en oferta? {precio > precio_oferta}")

if __name__ == "__main__":
    demo_comparaciones()