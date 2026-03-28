import sys 

def procesar_linea(linea: str) -> sthr:
    """Funcion que procesa una linea desde la entrada stdin 
    
    Args: 
        linea: linea recibida desde stdin.
        
    Returns:
        Linea procesada.
        None si no cumple con las reglas de negocio
    """
    
    columnas = linea.strip().split(',')
    
    
    #Debe tener exactamente 4 columnas
    if len(columnas) != 4:
        return None
    
    fecha,producto,cantidad,precio_unitario = columnas
    
