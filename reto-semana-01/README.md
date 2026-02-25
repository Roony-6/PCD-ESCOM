# RETO SEMANA 1

El programa lee desde la entrada estándar (`stdin`), limpia y procesa los datos siguiendo reglas de negocio estrictas, y entrega el total sumado en la salida estándar (`stdout`).

## Reglas de Procesamiento
Para garantizar la integridad de los datos, el script aplica las siguientes reglas:

1.  **Limpieza de Ruido:** Se eliminan caracteres no numéricos incrustados en los datos (ej. `1a2` se convierte en `12`).
2.  **Truncado de Decimales:** Los números decimales se truncan a su valor entero **antes** de realizar la suma (ej. `3.9` -> `3`).
3.  **Manejo de Espacios:** Se ignoran espacios en blanco extra alrededor de los valores.
4.  **Líneas Vacías:** Cualquier línea vacía o que contenga solo espacios devuelve un resultado de `0`.

### [Codigo](./main.py)