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
        
def validar_numero_columnas(numero_columnas: int, len_encabezado: int) -> bool:
    """Valida si el numero de columnas es valido
        Args: numero_columnas: numero de columnas  
              len_encabezado: total de columnas del csv
        Returns: bool: False si el numero de columnas no es igual al numero de columnas del encabezado
                        True si el numero de columnas exactamente igual a los datos del encabezado"""
    
    if numero_columnas == len_encabezado:
        return True
    else:
        False
def validar_id_revision(id_revision):
    """
    Valida que el id no este vacio.
    
    Args:
        id: El id d a validar
    Returns:
        bool: True si es valido, False si no
    """
    if not id_revision or not str(id_revision).strip():
        return False
    return True

def validar_vehiculo(vehiculo):
    """
    Valida que el vehiculo no este vacio.
    
    Args:
        vvehiculo: El vehiculo d a validar 
    Returns:
        bool: True si es valido, False si no
    """
    if not vehiculo or not str(vehiculo).strip():
        return False
    return True

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

def validar_registro(id_revision,vehiculo,presion,unidad,tipo_vehiculo ) -> bool:
    """Funcion que valida si una linea de la entrada stdin es valida
        
        Args: str linea
        
        Returns: True o False"""
    
    
    if not validar_id_revision(id_revision):
        return False, "id invalido"
    if not validar_vehiculo(vehiculo):
        return False, "El vehiculo es vacio"
    if not validar_presion(presion=presion):
        return False, "La presion no es valor numerico valido"
    if not validar_unidades(unidad=unidad):
        return False, "Las unidades son incorrectas"
    return True, None

    
        

