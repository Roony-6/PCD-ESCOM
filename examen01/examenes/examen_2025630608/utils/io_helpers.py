from .validators import validar_linea_vacia, validar_numero_columnas
 

def leer_datos(RUTA_ARCHIVO_ENTRADA:str)-> list :
    """
    Lee el archivo de entrada y retorna una lista de diccionarios.
    
    Args:
        RUTA_ARACHIVO_ENTRADA: Ruta al archivo CSV
        
    Returns:
        list: Lista de diccionarios con los datos de cada registro
        
    Raises:
        FileNotFoundError: Si el archivo no existe
    """
    datos_raw=[]
    
    with open(RUTA_ARCHIVO_ENTRADA, 'r', encoding='utf-8') as archivo: #abrimos el archivo
        lineas = archivo.readlines()
        
        if not lineas:
            return datos_raw
        
        encabezado = lineas[0].strip().split(',')
        for linea in lineas[1:]:
            linea = linea.strip()
            
            if validar_linea_vacia(linea):
                continue
            
            valores = linea.split(',')
            if validar_numero_columnas(len(valores), len(encabezado)):
                
                datos_dict = dict(zip(encabezado,valores))
                
                datos_raw.append(datos_dict)
    return datos_raw

def generar_reporte_detalle(registros,RUTA_ARCHIVO_REPORTE_DETALLE):
    """
    Escribe el reporte detalle .
    
    Args:
        registros: Lista de objetos Producto
        ruta_archivo: Ruta donde guardar el CSV
    """
    encabezados = ["id_revision","vehiculo","tipo_vehiculo","presion_bar","estado_presion"]
    
    with open(RUTA_ARCHIVO_REPORTE_DETALLE, 'w', encoding='utf-8') as archivo:
        archivo.write(','.join(encabezados) + '\n')
        
        # Escribir datos
        for registro in registros:
            linea = f"{registro.id_revision},{registro.vehiculo},{registro.tipo_vehiculo},{registro.presion_bar:.2f},"
            linea += f"{registro.clasificar()}"
            archivo.write(linea + '\n')
    
            

def generar_reporte_resumen(registros,RUTA_ARCHIVO_REPORTE_RESUMEN):
    """
    Escribe el reporte detalle .
    
    Args:
        registros: Lista de objetos Producto
        ruta_archivo: Ruta donde guardar el CSV
    """
    encabezados = ["tipo_vehiculo","conteo","promedio","maximo"]
    
    with open(RUTA_ARCHIVO_REPORTE_RESUMEN, 'w', encoding='utf-8') as archivo:
        archivo.write(','.join(encabezados) + '\n')
        
        # Escribir datos
      #  for registro in registros:
      #      linea = f"{registro.tipo_vehiculo},{co},{registro.tipo_vehiculo},{registro.presion_bar:.2f},"
      #      linea += f"{registro.clasificar()}"
      #      archivo.write(linea + '\n')