import sys 

def procesar_linea(linea: str) -> tuple:
    """Funcion que procesa una linea desde la entrada stdin 
    
    Args: 
        linea: linea recibida desde stdin.
        
    Returns:
        Linea procesada (tupla con los datos utiles).
        None si no cumple con las reglas de negocio
    """
    if not linea:
        return None
    
    columnas = linea.strip().split(',')
    #Ignoramos lineas vacias
    
    #Debe tener exactamente 4 columnas
    if len(columnas) != 4:
        return None
    
    fecha,producto,cantidad,precio_unitario = columnas
    
    # Verificamos datos numericos cantidad (int) precio_unitario(float)
    try:
        producto = producto.strip()
        cantidad = int(cantidad.strip())
        precio_unitario = float(precio_unitario.strip())
        return producto,cantidad,precio_unitario
    
    except Exception as e:
        return None    
       
def calcular_precio_promedio(producto:dict) -> float:
    """"Calcula el precio promedio de cada producto en el registro productos"""
    try:
        return producto.get("ingreso") / producto.get("unidades") 
        
    except Exception:
        return None

def almacenar_datos(producto: str, cantidad: int, precio_unitario:float, productos: dict):
    """"Almacena los datos de forma estructurada

        Args: producto, precio_unitario, cantidad
        
        Returns: 
    """
    if producto not in productos:
        productos[producto]={"unidades":0,
                             "ingresos_totales":0}
        productos[producto]["unidades"]+=cantidad
        productos[producto]["ingresos_totales"]+=precio_unitario
    
   


def main():
    productos = {}
      
    for linea in sys.stdin:
        
        resultado = procesar_linea(linea)
        if resultado:
            
            producto,cantidad,precio_unitario=resultado
            almacenar_datos(producto,cantidad,precio_unitario,productos)
            
            
    print(productos)
main()
            
            
#productos={}
#resultado = procesar_linea("")
#if resultado:
#    print(resultado)
#    productos = guardar_datos(*resultado, productos)
#    print(productos)
