# Archivo: demo_02_logicos.py
"""
Demo 2: Operadores Lógicos
Objetivo: Mostrar el uso de operadores and, or, not
"""

def demo_logicos():
    # Configuración de producto
    precio = 500
    stock = 10
    
    print("=== Demo: Operadores Lógicos ===")
    print(f"Precio: ${precio}")
    print(f"Stock: {stock}")
    
    # Verificar si el producto está disponible para venta
    precio_valido = precio > 0
    hay_stock = stock > 0
    
    disponible = precio_valido or hay_stock
    print(f"\nPrecio válido: {precio_valido}")
    print(f"Hay stock: {hay_stock}")
    print(f"¿Producto disponible? {disponible}")

if __name__ == "__main__":
    demo_logicos()
