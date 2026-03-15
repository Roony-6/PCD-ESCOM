# RETO SEMANA 02
# Clasificador de temperaturas

El programa lee desde la entrada estándar (`stdin`), limpia y procesa los datos, unifica las temperaturas al sistema métrico y clasifica el clima de cada ciudad siguiendo estándares establecidos en la práctica
y entrega los datos procesados y clasificados en la salida estándar (`stdout`)

---

## Reglas de Clasificación

El sistema utiliza los siguientes rangos en grados Celsius:

| Temperatura (°C) | Clasificación | Ejemplo |
| :--- | :--- | :--- |
| < 0 | **Congelante** | Moscú en invierno |
| 0 a 15 | **Frio** | Londres en primavera |
| 16 a 25 | **Templado** | CDMX todo el año |
| 26 a 35 | **Calido** | Miami en verano |
| > 35 | **Extremo** | Dubái en agosto |

---

## Uso

### 1. Preparar los datos
Desde un archivo, por ejemplo: `entrada.txt` (o `.csv`), con el siguiente formato, asegurándote de incluir el encabezado:
```csv
ciudad,temperatura,unidad
CDMX,22,C
Nueva York,50,F
Error,abc,C
Miami,95,F
```
### 2. Ejecutar el script
Desde la terminal puedes usar los siguiente comandos

#### Linux/MacOs
 ```bash
 python main.py < entrada.txt
 ```

 ### 3. Salida esperada
 El programa generará un reporte limpio en consola, ignorando los datos inválidos e imprimiendo la temperatura convertida con 2 decimales:

 ```
 ciudad,temperatura_celsius,clasificacion
CDMX,22.0,Templado
Nueva York,10.0,Frio
Miami,35.0,Calido
```

## [Ver Codigo](./main.py)