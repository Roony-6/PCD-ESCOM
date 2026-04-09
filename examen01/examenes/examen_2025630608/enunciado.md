# Examen Parcial 1 - Programación para Ciencia de Datos

## Sistema de Servicio de Taller Mecánico

**Matrícula:** `2025630608`
**Fecha límite de entrega:** (por definir)
**Valor:** 100 puntos

---

## Contexto

Un taller mecánico en zona fronteriza revisa neumáticos de vehículos mexicanos y americanos. Las presiones se registran en PSI (sistema americano) y bar (sistema métrico). Necesitan unificar a bar, clasificar el estado de presión y generar reportes por tipo de vehículo.

---

## Datos de Entrada

El archivo `datos/revisiones_neumaticos.csv` contiene registros con las siguientes columnas:

| Columna | Tipo esperado | Descripción |
|---------|---------------|-------------|
| `id_revision` | texto | Código de revisión |
| `vehiculo` | texto | Vehículo |
| `presion` | numérico (decimal) | Presión del neumático |
| `unidad` | texto (`PSI` o `bar`) | Unidad (PSI o bar) |
| `tipo_vehiculo` | texto | Tipo de vehículo |

**Unidades posibles:** `PSI` (PSI) y `bar` (Bar)

**Importante:** El archivo contiene aproximadamente 1000 registros. Algunos registros
contienen errores intencionales (valores no numéricos, unidades inválidas, columnas
faltantes o sobrantes, líneas vacías). Tu programa debe manejar estos casos sin
detenerse.

### Huella de integridad de los datos

El archivo de datos proporcionado tiene el siguiente hash SHA-256:

```
5e5b4e94488cf943acec8178956bdee6daccf97ae2bd569e0d12bc9cfad79ab4
```

**No modifiques el archivo de datos.** Este hash se verificará automáticamente al
calificar tu examen. Si el hash no coincide, se considerará que los datos fueron
alterados y se penalizará la calificación.

> Para verificar el hash de tu archivo puedes usar:
> ```python
> import hashlib
> with open("datos/revisiones_neumaticos.csv", "r", encoding="utf-8") as f:
>     print(hashlib.sha256(f.read().encode("utf-8")).hexdigest())
> ```

---

## Reglas de Procesamiento

### 1. Lectura del archivo
Lee el archivo CSV desde `datos/revisiones_neumaticos.csv`. El archivo usa comas (`,`) como
separador. La primera línea es el encabezado con los nombres de las columnas.

**¿Cómo leerlo?** Abre el archivo con `open()`, lee todas las líneas, separa la
primera línea (header) del resto. Para cada línea de datos, usa `.split(",")` para
obtener los valores individuales.

### 2. Validación de cada fila
Para cada fila del archivo (después del header), verifica que sea válida. Una fila
es **inválida** y debe ignorarse si cumple cualquiera de estas condiciones:

- **Línea vacía:** la línea no contiene texto (o solo espacios en blanco)
- **Número incorrecto de columnas:** al separar por coma, no resultan exactamente
  5 valores
- **Valor no numérico:** el campo `presion` no se puede convertir a `float`
  (usa `try/except ValueError`)
- **Unidad no reconocida:** el campo `unidad` no es ni `PSI` ni `bar`
  (la comparación es sensible a mayúsculas/minúsculas)

**Importante:** Tu programa no debe detenerse ni mostrar errores cuando encuentre
filas inválidas; simplemente las ignora y continúa con la siguiente.

### 3. Conversión de unidades
Para los registros válidos, convierte los valores que están en `PSI` a `bar`
usando la fórmula:

```
bar = PSI × 0.0689
```

En Python:
```python
bar_val = psi * 0.0689
```

Los valores que **ya están en `bar`** se mantienen sin cambio alguno.

Después de la conversión, redondea el resultado a **2 decimales**
usando la función `round()`.

### 4. Clasificación
Clasifica cada registro según el valor **ya convertido** a `bar`:

| Categoría | Rango (bar) | Regla |
|-----------|------|-------|
| Muy baja | < 1.59 | `valor < 1.59` |
| Baja | 1.59 - 1.92 | `1.59 <= valor < 1.92` |
| Normal | 1.92 - 2.88 | `1.92 <= valor < 2.88` |
| Alta | 2.88 - 3.58 | `2.88 <= valor < 3.58` |
| Peligrosa | >= 3.58 | `valor >= 3.58` |


> **Convención de límites:** Los límites inferiores son **inclusivos** (`>=`) y los
> superiores son **exclusivos** (`<`), excepto en la última categoría donde solo hay
> límite inferior inclusivo.

### 5. Generación de archivos de salida

Tu programa debe generar **dos archivos CSV** en la carpeta `salidas/`. A continuación
se describe cada uno en detalle.

---

## Archivo de Salida 1: `salidas/reporte_detalle.csv`

Este archivo contiene **un registro por cada fila válida** del archivo de entrada,
con el valor ya convertido y su clasificación.

### Columnas del archivo

| # | Columna | Tipo | Descripción | Ejemplo |
|---|---------|------|-------------|---------|
| 1 | `id_revision` | texto | ID original, copiado tal cual de la entrada | `REV-0001` |
| 2 | `vehiculo` | texto | Nombre original, copiado tal cual de la entrada | (varía) |
| 3 | `tipo_vehiculo` | texto | Grupo/categoría original | (varía) |
| 4 | `presion_bar` | decimal | Valor convertido a bar, con 2 decimales | `37.50` |
| 5 | `estado_presion` | texto | Clasificación asignada según los umbrales | (varía) |

### Reglas del archivo
- **Primera línea (header):** `id_revision,vehiculo,tipo_vehiculo,presion_bar,estado_presion`
- **Ordenamiento:** ascendente por `id_revision` (orden alfabético/numérico del ID)
- **Separador:** coma (`,`), sin espacios alrededor
- **Decimales:** los valores en `presion_bar` deben tener exactamente
  2 decimales (usa f-string: `f"{valor:.2f}"`)
- **Sin filas inválidas:** solo aparecen registros que pasaron la validación

### Cómo generarlo paso a paso
1. Filtra solo los registros válidos (los que pasaron la validación del paso 2)
2. Para cada registro: convierte el valor (paso 3), clasifícalo (paso 4)
3. Almacena los resultados en una lista
4. Ordena la lista por ID ascendente
5. Escribe el header seguido de cada registro, una línea por registro

---

## Archivo de Salida 2: `salidas/reporte_resumen.csv`

Este archivo contiene **una fila por cada grupo** (`tipo_vehiculo`), con métricas
agregadas calculadas a partir de los registros válidos.

### Columnas del archivo

| # | Columna | Tipo | Descripción | Cómo calcularlo |
|---|---------|------|-------------|-----------------|
| 1 | `tipo_vehiculo` | texto | Nombre del grupo | La clave del diccionario de agrupación |
| 2 | `conteo` | entero | Cantidad de registros válidos en ese grupo | Contar cuántos registros pertenecen al grupo |
| 3 | `promedio` | decimal | Promedio del valor convertido, 2 decimales | Suma de valores / conteo |
| 4 | `maximo` | decimal | Valor máximo convertido, 2 decimales | El mayor valor del grupo |

### Reglas del archivo
- **Primera línea (header):** `tipo_vehiculo,conteo,promedio,maximo`
- **Ordenamiento principal:** descendente por `conteo` (el grupo con más registros primero)
- **Desempate:** si dos grupos tienen el mismo conteo, orden alfabético por `tipo_vehiculo`
- **Decimales:** `promedio` y `maximo` con exactamente 2 decimales
- **`conteo`** es un entero (sin decimales)

### Cómo generarlo paso a paso
1. Usa un **diccionario** para agrupar: la clave es el valor de `tipo_vehiculo`, el valor
   es otro diccionario con `conteo`, `suma` y `maximo`
2. Recorre todos los registros válidos (ya procesados en el detalle):
   - Si el grupo no existe en el diccionario, créalo con conteo=0, suma=0.0, maximo=-infinito
   - Incrementa el conteo, suma el valor convertido, actualiza el máximo si corresponde
3. Calcula el promedio: `promedio = suma / conteo`
4. Ordena por conteo descendente (y alfabético en caso de empate)
5. Escribe el header seguido de cada grupo

---

## Estructura del Proyecto Requerida

```
examen_2025630608/
├── main.py                    # Punto de entrada: orquesta todo el proceso
├── models/
│   ├── __init__.py            # Puede estar vacío o exportar la clase
│   └── revision.py        # Definición de la clase Revision
├── utils/
│   ├── __init__.py            # Puede estar vacío o exportar funciones
│   ├── io_helpers.py          # Funciones para leer CSV y escribir reportes
│   └── validators.py          # Funciones para validar filas del CSV
├── datos/
│   └── revisiones_neumaticos.csv      # Archivo de entrada (proporcionado, NO modificar)
└── salidas/
    ├── reporte_detalle.csv    # Generado por tu programa
    └── reporte_resumen.csv    # Generado por tu programa
```

### Descripción de cada archivo

**`main.py`** — Punto de entrada. Al ejecutar `python main.py` desde la raíz del
proyecto, debe:
1. Leer el archivo de datos usando funciones de `utils/io_helpers.py`
2. Validar cada fila usando funciones de `utils/validators.py`
3. Crear objetos `Revision` para cada registro válido
4. Generar el reporte de detalle y escribirlo en `salidas/reporte_detalle.csv`
5. Generar el reporte de resumen y escribirlo en `salidas/reporte_resumen.csv`

**`models/revision.py`** — Contiene la clase `Revision` (ver sección siguiente).

**`utils/io_helpers.py`** — Contiene al menos:
- Una función para **leer** el archivo CSV y retornar las filas como lista de listas o diccionarios
- Una función para **escribir** un archivo CSV a partir de una lista de datos

**`utils/validators.py`** — Contiene al menos:
- Una función para **validar** si una fila del CSV es válida (número correcto de
  columnas, valor numérico, unidad reconocida)
- Debe retornar `True`/`False` o una tupla `(es_valido, mensaje_error)`

---

## Clase Requerida: `Revision`

La clase `Revision` en `models/revision.py` debe incluir:

- **`__init__(self, ...)`**: Recibe y almacena como atributos: `id_revision`,
  `vehiculo`, el valor ya convertido a bar, y `tipo_vehiculo`
- **`clasificar(self)`**: Método que retorna un string con la clasificación según
  los umbrales definidos (ej: `"Muy baja"`, `"Baja"`, etc.)
- **`__str__(self)`**: Retorna una representación legible para el usuario
  (ej: `"REV-0001 - NombreEjemplo (tipo_vehiculo: GrupoEjemplo) - 37.5 bar"`)
- **`__repr__(self)`**: Retorna una representación técnica para depuración
  (ej: `"Revision(id='REV-0001', valor=37.5, clase='Normal')"`)

---

## Ejemplo

### Entrada (primeras filas de `datos/revisiones_neumaticos.csv`):
```csv
id_revision,vehiculo,presion,unidad,tipo_vehiculo
REV-0001,Nissan Frontier 2023,30.71,PSI,Lujo
REV-0002,Ford Ranger 2023,3.15,bar,Pickup
REV-0003,Chevrolet Aveo 2022,2.08,bar,Compacto
REV-0004,Ford Ranger 2023,31.69,PSI,Sedán
REV-0005,Mercedes C300 2023,41.33,PSI,Pickup
```

### Salida detalle esperada (`salidas/reporte_detalle.csv`):
```csv
id_revision,vehiculo,tipo_vehiculo,presion_bar,estado_presion
REV-0001,Nissan Frontier 2023,Lujo,2.12,Normal
REV-0002,Ford Ranger 2023,Pickup,3.15,Alta
REV-0003,Chevrolet Aveo 2022,Compacto,2.08,Normal
REV-0004,Ford Ranger 2023,Sedán,2.18,Normal
REV-0005,Mercedes C300 2023,Pickup,2.85,Normal
```

### Salida resumen esperada (`salidas/reporte_resumen.csv`):
```csv
tipo_vehiculo,conteo,promedio,maximo
Minivan,133,2.39,3.79
SUV,118,2.54,3.77
Deportivo,116,2.33,3.72
Compacto,115,2.54,3.79
Pickup,113,2.47,3.79
```

---

## Criterios de Evaluación

| Criterio | Puntos | Detalle |
|----------|--------|---------|
| Estructura del proyecto | 15 | Carpetas, archivos, `__init__.py`, imports correctos |
| Clase `Revision` | 20 | `__init__`, `clasificar()`, `__str__`, `__repr__` |
| Validación de datos | 10 | Manejo correcto de filas inválidas |
| Conversión de unidades | 15 | Fórmula correcta, precisión decimal |
| Clasificación | 10 | Umbrales correctos, categorías asignadas |
| Agrupación y métricas | 15 | Conteo, promedio, máximo por grupo |
| Formato de salida | 10 | CSVs con columnas, orden y formato correctos |
| Git | 5 | Mínimo 5 commits descriptivos, `.gitignore` |
| **Total** | **100** | |

> **Nota:** Se verificará automáticamente que el hash SHA-256 del archivo de datos
> coincida con `5e5b4e94488cf943acec8178956bdee6daccf97ae2bd569e0d12bc9cfad79ab4`. Si el archivo fue modificado, se aplicará una
> penalización.

---

## Instrucciones de Entrega

1. Crea un repositorio en GitHub llamado `examen1_pcd`
2. Desarrolla tu solución siguiendo la estructura indicada
3. Asegúrate de que tu programa funciona ejecutando: `python main.py`
4. Tu programa debe leer de `datos/revisiones_neumaticos.csv` y escribir en `salidas/`
5. Haz **mínimo 5 commits** con mensajes descriptivos
6. Incluye un `.gitignore` apropiado
7. **NO modifiques** el archivo `datos/revisiones_neumaticos.csv` (se verificará su integridad)
8. Entrega el enlace a tu repositorio antes de la fecha límite

## Restricciones

- **NO** uses pandas, numpy ni librerías externas (solo biblioteca estándar de Python)
- **NO** copies código de otros compañeros (cada examen tiene datos y umbrales únicos)
- **NO** modifiques el archivo de datos proporcionado
- Tu código debe funcionar con **cualquier** archivo que siga el formato descrito,
  no solo con los datos proporcionados
