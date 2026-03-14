import sys

def fahrenheit_a_celsius(fahrenheit:float) -> float: 
    """Convierte Fahrenheit a Celsius."""
    return (fahrenheit - 32) * 5 / 9


def clasificar_temperatura(celsius: float) -> float:
    """Clasifica la temperatura segun rangos definidos."""
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
    
def procesar_linea(linea):
    