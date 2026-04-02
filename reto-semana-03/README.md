# Reto Semana 3
# Analizador de Ventas

Herramienta que lee un flujo de transacciones de ventas desde `stdin`, agrupa los datos por producto y genera un reporte consolidado en formato CSV ordenado por ingreso total.
 
---
 
## Objetivo
 
Dado un archivo CSV con registros de ventas, el programa calcula por cada producto:
 
- Total de unidades vendidas
- Ingreso total generado (`cantidad × precio_unitario`)
- Precio promedio de venta (`ingreso_total / unidades_vendidas`)
 
El reporte se ordena de **mayor a menor ingreso total**.
 
---
 
## Uso
 
**Requisitos:** Python 3.10+
 
```bash
# Usando redirección de archivo
python main.py < ventas.csv
 
# Usando pipe
cat ventas.csv | python main.py
```
 
> El programa filtra automáticamente el encabezado, líneas vacías y filas malformadas.
 
---
 
## Entrada
 
Archivo CSV con exactamente **4 columnas** por fila:
 
```
fecha,producto,cantidad,precio_unitario
```
 
| Columna | Tipo | Descripción |
|---|---|---|
| `fecha` | `str` | Fecha de la transacción (YYYY-MM-DD), se ignora |
| `producto` | `str` | Nombre del producto |
| `cantidad` | `int` | Unidades vendidas |
| `precio_unitario` | `float` | Precio por unidad |
 
**Filas ignoradas silenciosamente:**
- Líneas vacías o con número de columnas distinto a 4
- Filas donde `cantidad` o `precio_unitario` no sean numéricos válidos
 
---
 
## Salida
 
CSV con 4 columnas, **ordenado por `ingreso_total` descendente**:
 
```
producto,unidades_vendidas,ingreso_total,precio_promedio
```
 
Los valores monetarios se presentan con **2 decimales**. Las unidades son enteros sin decimales.
 
---
 
## Ejemplo de uso
 
**Entrada (`entrada_facil.txt`):**
```
fecha,producto,cantidad,precio_unitario
2026-01-01,Laptop,2,15000.00
2026-01-02,Mouse,10,250.00
2026-01-03,Laptop,1,14500.00
2026-01-04,Teclado,5,800.00
2026-01-05,Mouse,8,250.00
```
 
**Comando:**
```bash
python main.py < entrada_facil.txt
```
 
**Salida:**
```
producto,unidades_vendidas,ingreso_total,precio_promedio
Laptop,3,44500.00,14833.33
Mouse,18,4500.00,250.00
Teclado,5,4000.00,800.00
```
 