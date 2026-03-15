import sys

def fahrenheit_a_celsius(fahrenheit:float) -> float: 
    """ Convierte Fahrenheit a Celsius."""
    return (fahrenheit - 32) * 5 / 9


def clasificar_temperatura(celsius: float) -> float:
    """ Clasifica la temperatura segun rangos definidos."""
    if celsius < 0:
        return "Congelante"
    elif celsius <= 15:  # 0 a 15
        return "Frio"
    elif celsius <= 25:  # 16 a 25
        return "Templado"
    elif celsius <= 35:  # 26 a 35
        return "Calido"
    else:  # > 35
        return "Extremo"
    
def procesar_linea(linea:str) -> str:
    """ Procesa cada linea de la entrada stdin"""

    if not linea:
        return False
    
    
    elementos= linea.strip().split()
    
    if (len(elementos) != 3):
        return False
    if elementos[2].upper() not in ["C","F"]:
        return False
    
        
    try:
                
        ciudad = elementos[0].upper()
        grados = f"{float(elementos[1].strip()):.2f}"
        clasificacion = clasificar_temperatura(fahrenheit_a_celsius(elementos[2]) if elementos[2] == "F" else elementos[2].upper())
        
    except :
        return False
    
    return f"{ciudad},{grados},{clasificacion}"
    
    

def main():
    #imprimir encabezado
    print("ciudad,temperatura_celsius,clasificacion")
    
    for linea in sys.stdin:
        continue
    
    
if __name__ == "__main__":
    main()
        

    