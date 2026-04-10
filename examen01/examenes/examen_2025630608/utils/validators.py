def validar_linea_vacia(fila:str)->bool:
    """Valida si una linea es vacia
       Args: 
            fila: linea a validar
       Returns:
            bool: True si no es vacia, False si es vacia"""
    if not fila:
        return False
    else:
        True
        
def validar_numero_columnas(fila: str) -> bool:
    """Valida si el numero de columnas es valido
        Args: fila: fila
        Returns: bool: False si el numero de columnas no es 5
                        True si el numero de columnas es exactamente 5"""
    columnas = fila.split(",").strip()
    return len(columnas) == 5

def validar_presion(presion: str) -> bool:
    """
    Valida que la presion sea un numero.
    
    Args:
        presion: Presion a validar
        
    Returns:
        bool: True si es valido, False si no
    """
    try:
        presion = float(presion)
        return presion >= 0
    except (ValueError, TypeError):
        return False
    
def validar_unidades(unidad: str) -> bool:
    """
    Valida si las unidades son validas
    
    Args: 
        unidad: unidad a validar (sensible a mayusculas y minusculas)
    Returns:
        bool: true si es valida, False si no
    """
    return unidad in ["PSI", "bar"]
     
def validar_fila(fila: str) -> bool:
    """Funcion que valida si una linea de la entrada stdin es valida
        
        Args: str linea
        
        Returns: True o False"""
    columnas = []
    if not validar_linea_vacia(fila):
        return False,"Linea vacia" #verificamos linea vacia
    if not validar_numero_columnas(fila=fila):
        return False, "No son 5 datos"
    id_revision,vehiculo,presion,unidad,tipo_vehiculo = fila.split(',').strip()
    
    if not validar_presion(presion=presion):
        return False, "La presion no es valor numerico valido"
    if not validar_unidades(unidad=unidad):
        return False, "Las unidades son incorrectas"
    return True, None

    
        

