import sys

def limpiar_valor(valor):
    """
    Limpia un valor individual:
    - Quita espacios
    - Elimina caracteres no validos
    - Retorna el numero limpio como string
    """
    caracteres_validos='0123456789.-'
    
    valor =valor.strip()
    
    for caracter in valor:
        if caracter in caracteres_validos:
            cadena_limpia+=caracter
    
    return cadena_limpia
            
        
    
    
    
def procesar_linea(linea):
    """
    Procesa una linea completa:
    - Separa por comas
    - Limpia cada valor
    - Trunca a entero
    - Suma todos
    - Retorna el resultado
    """
    suma=0
    
    if not linea:
        return 0
    elif linea.isspace():
        return 0
    
    elementos=linea.split(",")
    
    try:
        for elemento in elementos:
            suma+=int(float(limpiar_valor(elementos)))
                    
    except ValueError:
        return 0
    
    return suma

def main():
    """
    Lee de stdin linea por linea
    Procesa cada linea
    Imprime el resultado
    """
    for linea in sys.stdin:
        resultado = procesar_linea(linea)
        print(resultado)

if __name__ == "__main__":
    main()