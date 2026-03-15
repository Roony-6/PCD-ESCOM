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

    if not linea or "ciudad,temperatura" in linea: #verifica si la linea es vacia o es el encabezado
        return None
    
    elementos= linea.strip().split(',')
    #print(elementos)
    
    if (len(elementos) != 3):
        return None
    
    if elementos[2].strip().upper() not in ['F','C']:
        return None
    try:
        ciudad = elementos[0].strip()
        #print(ciudad)
        valor_temperatura = float(elementos[1].strip())
        #print(valor_temperatura)
        celsius = fahrenheit_a_celsius(valor_temperatura) if elementos[2].strip() == "F" else valor_temperatura
        #print(celsius)
        clasificacion = clasificar_temperatura(celsius)        
        #print(clasificacion)
        return f"{ciudad},{celsius:.2f},{clasificacion}"
    except Exception as e:
        ##print(e)
       return None

def main():
    #imprimir encabezado
    print("ciudad,temperatura_celsius,clasificacion")
    
    for linea in sys.stdin:
        resultado = procesar_linea(linea)
        if resultado:
            print(resultado)   
    
if __name__ == "__main__":
    main()
        

    