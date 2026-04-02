import sys

def procesar_linea(linea: str) -> tuple | None:
    """Parsea una línea CSV. Retorna (producto, cantidad, precio_unitario) o None."""
    if not linea.strip():
        return None

    columnas = linea.strip().split(',')
    if len(columnas) != 4:
        return None

    fecha, producto, cantidad_str, precio_str = columnas

    try:
        producto = producto.strip()
        cantidad = int(cantidad_str.strip())
        precio_unitario = float(precio_str.strip())
        if cantidad <= 0 or precio_unitario < 0:
            return None
        return producto, cantidad, precio_unitario
    except (ValueError, TypeError):
        return None


def almacenar_datos(producto: str, cantidad: int, precio_unitario: float, productos: dict):
    """Acumula unidades e ingresos por producto."""
    if producto not in productos:
        productos[producto] = {"unidades": 0, "ingresos_totales": 0.0}

    productos[producto]["unidades"] += cantidad
    productos[producto]["ingresos_totales"] += precio_unitario * cantidad  

def generar_resumen(productos: dict):
    """Imprime el reporte CSV final."""
    print("producto,unidades_vendidas,ingreso_total,precio_promedio")
    for producto, data in productos.items():
        unidades = data["unidades"]
        ingresos = data["ingresos_totales"]
        promedio = ingresos / unidades if unidades else 0.0  # evita error de division por cero
        print(f"{producto},{unidades},{ingresos:.2f},{promedio:.2f}")


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
