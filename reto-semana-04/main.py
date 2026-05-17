import sys
from models.producto import Producto
from utils.validators import validar_producto
from utils.io import leer_inventario, escribir_reporte

def crear_productos(datos_raw):
    productos = []
    skus_procesados = set()
    
    for datos in datos_raw:
        sku = datos.get('sku')
        
        if sku in skus_procesados:
            continue
            
        es_valido, error = validar_producto(
            sku,
            datos.get('nombre'),
            datos.get('categoria'),
            datos.get('precio'),
            datos.get('stock'),
            datos.get('stock_minimo')
        )
        
        if not es_valido:
            # Enviamos los errores a stderr para no ensuciar el stdout
            print(f"Advertencia: Ignorando registro inválido - {error}", file=sys.stderr)
            continue
            
        producto = Producto(
            sku=sku,
            nombre=datos['nombre'],
            categoria=datos['categoria'],
            precio=float(datos['precio']),
            stock=int(datos['stock']),
            stock_minimo=int(datos['stock_minimo'])
        )
        productos.append(producto)
        skus_procesados.add(sku)
        
    return productos

def filtrar_necesitan_reorden(productos):
    return [p for p in productos if p.necesita_reorden()]

def ordenar_por_faltantes(productos):
    return sorted(productos, key=lambda p: p.unidades_faltantes(), reverse=True)

def main():
    # 1. Leer desde sys.stdin
    datos_raw = leer_inventario(sys.stdin)
    
    # 2. Procesar
    productos = crear_productos(datos_raw)
    necesitan_reorden = filtrar_necesitan_reorden(productos)
    necesitan_reorden = ordenar_por_faltantes(necesitan_reorden)
    
    # 3. Escribir hacia sys.stdout
    escribir_reporte(necesitan_reorden, sys.stdout)

if __name__ == "__main__":
    main()