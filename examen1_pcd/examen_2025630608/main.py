from models.revision import Revision
from utils.io_helpers import leer_datos, generar_reporte_detalle,generar_reporte_resumen
from utils.validators import validar_registro

RUTA_ARCHIVO_ENTRADA = "datos/revisiones_neumaticos.csv"
RUTA_ARCHIVO_REPORTE_DETALLE="salidas/reporte_detalle.csv"
RUTA_ARCHIVO_REPORTE_RESUMEN = "salidas/reporte_resumen.csv"

def crear_registros(datos_raw):
    registros = []
    
    convertir_presion = lambda presion, unidad: presion if unidad.strip() == "bar" else presion * 0.0689
    
    for i,dato in enumerate(datos_raw):
        
        id_revision = dato.get("id_revision")
        vehiculo = dato.get("vehiculo")
        presion = dato.get("presion")
        unidad = dato.get("unidad")
        tipo_vehiculo = dato.get("tipo_vehiculo")
        #validamos registro valido
        es_valido, mensaje = validar_registro(id_revision,vehiculo,
                                              presion,unidad,tipo_vehiculo)
        
        if not es_valido:
            print(f"Advertencia: Ignorando registro invalido - {mensaje} {i}")
            continue
        #creamos el registro Revision
        
        registro = Revision(id_revision=id_revision,vehiculo=vehiculo,
                            presion_bar=convertir_presion(float(presion),unidad),
                            tipo_vehiculo=tipo_vehiculo)     
        registros.append(registro)  
        
    return registros

def datos_por_tipo_vehiculo(registros):
    tipos_vehiculos = {}
   
    for registro in registros:
        
        if registro.tipo_vehiculo not in tipos_vehiculos:
            tipos_vehiculos[registro.tipo_vehiculo] = {"conteo": 0,
                                                        "suma": 0,
                                                        "promedio": 0,
                                                        "maximo": float("-inf")}
        tipos_vehiculos[registro.tipo_vehiculo]["conteo"] += 1
        tipos_vehiculos[registro.tipo_vehiculo]["suma"]+= registro.presion_bar
        tipos_vehiculos[registro.tipo_vehiculo]["maximo"]= registro.presion_bar if registro.presion_bar > tipos_vehiculos[registro.tipo_vehiculo]["maximo"] else tipos_vehiculos[registro.tipo_vehiculo]["maximo"]
    
    for tipo in tipos_vehiculos:
        tipos_vehiculos[tipo]["promedio"] = tipos_vehiculos[tipo]["suma"] / tipos_vehiculos[tipo]["conteo"]
    return tipos_vehiculos
        
        

def main():
    datos_raw = leer_datos(RUTA_ARCHIVO_ENTRADA) #Leemos los datos
    registros = crear_registros(datos_raw)       #Creamos los registros
    registros_ordenados = sorted(registros, key=lambda registro: (registro.id_revision.split('-')[0], int(registro.id_revision.split('-')[1]))) # ordenamos los registros
    generar_reporte_detalle(registros_ordenados, RUTA_ARCHIVO_REPORTE_DETALLE) #generamos reporte_detalle.csv
    
    #Guardamos los datos en un diccionario (tipos_vehiculos)
    tipos_vehiculos=datos_por_tipo_vehiculo(registros)
    
    # Convertimos el diccionario a una lista de diccionarios o tuplas para ordenar
    lista_resumen = []
    for tipo, datos in tipos_vehiculos.items():
        datos["tipo_vehiculo"] = tipo
        lista_resumen.append(datos)

    # Ordenamiento: por conteo (negativo para descendente) y luego tipo (ascendente)
    
    lista_ordenada = sorted(lista_resumen, key=lambda x: (-x["conteo"], x["tipo_vehiculo"]))
    generar_reporte_resumen(lista_ordenada,RUTA_ARCHIVO_REPORTE_RESUMEN) #Generamos el reporte resumen
    

if __name__ == "__main__":
    main()