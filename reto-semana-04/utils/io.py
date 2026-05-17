import sys

def leer_inventario(archivo=sys.stdin):
    productos_raw = []
    
    # Lee directamente del flujo de entrada
    lineas = archivo.readlines()
    
    if not lineas:
        return productos_raw
    
    encabezados = lineas[0].strip().split(',')
    
    for linea in lineas[1:]:
        linea = linea.strip()
        if not linea:
            continue
        
        valores = linea.split(',')
        if len(valores) == len(encabezados):
            producto_dict = dict(zip(encabezados, valores))
            productos_raw.append(producto_dict)
            
    return productos_raw

def escribir_reporte(productos, archivo=sys.stdout):
    encabezados = [
        "sku", "nombre", "categoria", "stock_actual", 
        "stock_minimo", "unidades_faltantes", "valor_inventario"
    ]
    
    # Escribe directamente al flujo de salida
    archivo.write(','.join(encabezados) + '\n')
    
    for p in productos:
        linea = f"{p.sku},{p.nombre},{p.categoria},{p.stock},"
        linea += f"{p.stock_minimo},{p.unidades_faltantes()},{p.valor_inventario():.2f}"
        archivo.write(linea + '\n')