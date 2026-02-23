import sys

def limpiar_valor(valor):
    """
    Limpia un valor individual:
    - Quita espacios
    - Elimina caracteres no validos
    - Retorna el numero limpio como string
    """
    # Tu codigo aqui
    pass

def procesar_linea(linea):
    """
    Procesa una linea completa:
    - Separa por comas
    - Limpia cada valor
    - Trunca a entero
    - Suma todos
    - Retorna el resultado
    """
    # Tu codigo aqui
    pass

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