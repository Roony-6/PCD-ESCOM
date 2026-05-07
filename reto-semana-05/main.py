"""
Perfilador de Datasets CSV
Analiza cualquier archivo CSV y genera un reporte de calidad de datos.
"""

import argparse
import sys
from utils.data_profiler import leer_csv, perfilar_columna, escribir_csv

def main():
    parser = argparse.ArgumentParser(description="Perfilador de Datasets CSV")
    parser.add_argument("--input", "-i", required=True, help="Ruta al CSV de entrada")
    parser.add_argument("--output", "-o", required=True, help="Ruta al CSV de salida")
    
    args = parser.parse_args()
    print(f"Perfilando: {args.input}")
    
    try:
        encabezados, filas = leer_csv(args.input)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {args.input}")
        sys.exit(1)
    
    if not encabezados:
        print("Error: El archivo está vacío")
        sys.exit(1)
    
    print(f"Columnas encontradas: {len(encabezados)}")
    print(f"Registros: {len(filas)}")
    
    perfiles = []
    for i, nombre_col in enumerate(encabezados):
        valores = [fila[i] if i < len(fila) else "" for fila in filas]
        perfil = perfilar_columna(nombre_col, valores)
        perfiles.append(perfil)
    
    escribir_csv(args.output, perfiles)
    print(f"Perfil guardado en: {args.output}")
    print("¡Completado!")

if __name__ == "__main__":
    main()