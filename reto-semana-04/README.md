# RETO SEMANA 04 
# SISTEMA DE INVENTARIO MODULAR

Esta herramienta de línea de comandos diseñada para gestionar el inventario de una cadena de tiendas de tecnología. El sistema automatiza la lectura de existencias, valida la integridad de los datos, identifica productos con stock crítico y genera un reporte detallado para el departamento de compras, priorizando aquellos que requieren atención inmediata

## Estructura del reto:
El codigo sigue una estructura modular --que de hecho es el objetivo del reto-- para organizar y estructurar mejor el proyecto. 

```text
reto-semana-04/
├── main.py                # Punto de entrada 
├── README.md              # Documentación del reto (este archivo)
├── models/                # Lógica de negocio (Clases de dominio)
│   ├── __init__.py        
│   └── producto.py        # Definición de la clase Producto y sus métodos
├── utils/                 # Funciones de soporte y utilerias
│   ├── __init__.py        
│   ├── io.py              # Manejo de lectura/escritura de archivos CSV
│   └── validators.py      # Lógica de validación de datos de entrada
├── data/                  # Almacenamiento de datos de entrada
│   └── inventario.csv     # Archivo fuente con el stock actual
└── outputs/               # Resultados del procesamiento
    └── reporte_inventario.csv  # Reporte de productos para reorden
```

## Uso 
Asegurate de tener python 3 instalado
```bash
sudo pacman -S python3
```
y ejecuta el siguiente comando (ubicado en la raiz del proyecto ```reto-semana-04```)
```bash
python main.py 
```

## Especificación de Entrada

El sistema procesa el archivo localizado en `data/inventario.csv`. Cada producto está identificado por un SKU único y se asume que no existen registros duplicados que requieran consolidación.

### Formato de Columnas
| Columna | Tipo | Descripción | Ejemplo |
| :--- | :--- | :--- | :--- |
| `sku` | Texto | Identificador único del producto | `SKU001` |
| `nombre` | Texto | Nombre descriptivo del artículo | `Laptop HP` |
| `categoria` | Texto | Clasificación departamental | `Electronica` |
| `precio` | Decimal | Precio unitario de venta | `15000.00` |
| `stock` | Entero | Cantidad física disponible en almacén | `5` |
| `stock_minimo` | Entero | Umbral para solicitar reorden | `10` |

### Gestión de Errores en Datos
El sistema implementa una política de **tolerancia a fallos**, ignorando silenciosamente las líneas que presenten:
* Valores no numéricos en los campos de `precio`, `stock` o `stock_minimo`.
* Registros con un número de columnas distinto a seis (datos faltantes o excedentes).
* SKUs o nombres vacíos.

---

##  Especificación de Salida

El reporte final se genera en `outputs/reporte_inventario.csv` e incluye exclusivamente los productos cuyo stock actual es estrictamente menor al stock mínimo configurado.

### Formato del Reporte
| Columna | Tipo | Descripción / Cálculo |
| :--- | :--- | :--- |
| `sku` | Texto | SKU del producto |
| `nombre` | Texto | Nombre del producto |
| `categoria` | Texto | Categoría |
| `stock_actual` | Entero | Cantidad actual en inventario |
| `stock_minimo` | Entero | Nivel de stock mínimo requerido |
| `unidades_faltantes`| Entero | `stock_minimo - stock_actual` |
| `valor_inventario` | Decimal | `precio * stock_actual` (formateado a 2 decimales) |

### Reglas de Negocio Aplicadas
1.  **Filtrado**: Solo productos con necesidad de reorden.
2.  **Ordenamiento**: Los registros se presentan ordenados por `unidades_faltantes` de forma **descendente** (priorizando los productos con mayor desabasto).