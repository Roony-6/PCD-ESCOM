# RETO SEMANA 1 
# Calculadora de sumas
---
El programa lee desde la entrada estándar (`stdin`), limpia y procesa los datos siguiendo reglas de negocio estrictas, y entrega el total sumado en la salida estándar (`stdout`).

## Reglas de Procesamiento
Para garantizar la integridad de los datos, el script aplica las siguientes reglas:

1.  **Limpieza de Ruido:** Se eliminan caracteres no numéricos incrustados en los datos (ej. `1a2` se convierte en `12`).
2.  **Truncado de Decimales:** Los números decimales se truncan a su valor entero **antes** de realizar la suma (ej. `3.9` -> `3`).
3.  **Manejo de Espacios:** Se ignoran espacios en blanco extra alrededor de los valores.
4.  **Líneas Vacías:** Cualquier línea vacía o que contenga solo espacios devuelve un resultado de `0`.

---

## Uso
- Linux/Mac
```bash
python main.py < ejemplo_1.txt
```
---
## Ejemplo de entrada y salida
- Entrada (contenido del archivo `ejemplo_1.txt`)
```
1,2,3
10

1.9,2.1,3.7
1a2,3b,4
-5,10,3
5 , 10 , 15  
0,0,0
-1,-2,-3
abc,def
3.99
-0.5,0.5
 ,1,2, 
100

```
- Salida:

```
6
10
0
6
19
8
30
0
-6
0
3
0
3
100

```


### [Codigo](./main.py)