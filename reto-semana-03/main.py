#!/usr/bin/env python3
import sys
import math

def procesar_linea(linea: str) -> tuple | None:
    """Parsea una línea CSV. Retorna (producto, cantidad, precio_unitario) o None."""
    if not linea.strip():
        return None

    columnas = linea.strip().split(',')
    
    # Validar que tengamos exactamente 4 columnas
    if len(columnas) != 4:
        print(f"Advertencia: Fila ignorada por longitud incorrecta - {linea.strip()}", file=sys.stderr)
        return None

    fecha, producto, cantidad_str, precio_str = columnas
    
    # Ignorar silenciosamente la fila de encabezados si entra a la función
    if cantidad_str.strip().lower() == "cantidad":
        return None

    try:
        producto = producto.strip()
        if not producto:
            return None
            
        cantidad = int(cantidad_str.strip())
        precio_unitario = float(precio_str.strip())
        
        # Bloqueo explícito de valores negativos, cero en cantidad y datos corruptos (inf, nan)
        if cantidad <= 0:
            print(f"Advertencia: Cantidad inválida ({cantidad}) en producto '{producto}'", file=sys.stderr)
            return None
            
        if precio_unitario < 0 or math.isinf(precio_unitario) or math.isnan(precio_unitario):
            print(f"Advertencia: Precio inválido o corrupto ({precio_unitario}) en producto '{producto}'", file=sys.stderr)
            return None
            
        return producto, cantidad, precio_unitario
        
    except (ValueError, TypeError):
        # Captura errores si 'cantidad' o 'precio' traen letras en lugar de números
        print(f"Advertencia: Error de tipo numérico en fila - {linea.strip()}", file=sys.stderr)
        return None


def almacenar_datos(producto: str, cantidad: int, precio_unitario: float, productos: dict):
    """Acumula unidades e ingresos por producto."""
    if producto not in productos:
        productos[producto] = {"unidades": 0, "ingresos_totales": 0.0}

    productos[producto]["unidades"] += cantidad
    productos[producto]["ingresos_totales"] += precio_unitario * cantidad  


def generar_resumen(productos: dict):
    "Genera el resumen de ventas"
    # Forzamos la salida al stdout por seguridad, aunque print() lo hace por defecto
    print("producto,unidades_vendidas,ingreso_total,precio_promedio", file=sys.stdout)
    
    # Ordenar por ingreso descendente antes de imprimir
    ordenados = sorted(
        productos.items(),
        key=lambda x: x[1]["ingresos_totales"],
        reverse=True
    )
    
    for producto, data in ordenados:
        unidades = data["unidades"]
        ingresos = data["ingresos_totales"]
        promedio = ingresos / unidades if unidades else 0.0
        print(f"{producto},{unidades},{ingresos:.2f},{promedio:.2f}", file=sys.stdout)


def main():
    productos = {}

    for linea in sys.stdin:
        resultado = procesar_linea(linea)
        if resultado:
            producto, cantidad, precio_unitario = resultado
            almacenar_datos(producto, cantidad, precio_unitario, productos)

    generar_resumen(productos)  


if __name__ == "__main__":
    main()