import math

def validar_sku(sku):
    if not sku or not str(sku).strip():
        return False
    return True

def validar_precio(precio):
    try:
        precio_num = float(precio)
        # Se bloquean los 'inf' y 'nan' que vienen en el CSV
        return precio_num >= 0 and not math.isinf(precio_num) and not math.isnan(precio_num)
    except (ValueError, TypeError):
        return False

def validar_stock(stock):
    try:
        stock_num = int(stock)
        return stock_num >= 0
    except (ValueError, TypeError):
        return False

def validar_producto(sku, nombre, categoria, precio, stock, stock_minimo):
    if not validar_sku(sku):
        return False, "SKU vacío o inválido"
    if not nombre or not str(nombre).strip():
        return False, "Nombre vacío"
    if not validar_precio(precio):
        return False, f"Precio inválido: {precio}"
    if not validar_stock(stock):
        return False, f"Stock inválido: {stock}"
    if not validar_stock(stock_minimo):
        return False, f"Stock mínimo inválido: {stock_minimo}"
    
    return True, None