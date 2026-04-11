# Examen Parcial 1: 
## Sistema de Servicio de Taller Mecánico

Este proyecto consiste en una herramienta de procesamiento y análisis de datos diseñada para un taller mecánico que gestiona la presión de neumáticos en una zona fronteriza. El sistema permite unificar mediciones en diferentes unidades, clasificar el estado de seguridad de los vehículos y generar reportes métricos detallados.

Para consultar los requerimientos técnicos completos, reglas de negocio y umbrales de clasificación, consulta el:

#### 👉 [EXAMEN](./examen_2025630608/enunciado.md)
###  👉 [main.py](./examen_2025630608/main.py)

## Características Principales

- Procesamiento de Datos Robusto: Filtra registros inválidos (líneas vacías, valores no numéricos o unidades desconocidas) sin interrumpir la ejecución.

- Conversión de Unidades: Realiza la conversión automática de PSI a bar mediante la fórmula bar=PSI×0.0689.

- Clasificación de Presión: Categoriza cada neumático en niveles que van desde "Muy baja" hasta "Peligrosa" según estándares definidos.

- Generación de Reportes:

        Reporte de Detalle: Registro individual con IDs ordenados alfanuméricamente.

        Reporte de Resumen: Métricas agregadas (conteo, promedio y máximo) por tipo de vehículo, con ordenamiento por volumen de registros.

## Estructura del Repositorio

El proyecto sigue una arquitectura modular para facilitar el mantenimiento y la validación:
```text
examen_2025630608/
├── main.py                # Orquestador principal del flujo
├── models/
│   └── revision.py        # Clase Revision con lógica de clasificación
├── utils/
│   ├── io_helpers.py      # Funciones de lectura y escritura de CSV
│   └── validators.py      # Lógica de validación de integridad de datos
├── datos/
│   └── revisiones_neumaticos.csv  # Archivo fuente (verificado por SHA-256)
└── salidas/
    ├── reporte_detalle.csv # Reporte de registros válidos procesados
    └── reporte_resumen.csv # Reporte estadístico por tipo de vehículo
```

## Ejecución

Este programa ha sido desarrollado utilizando estrictamente la biblioteca estándar de Python, cumpliendo con la restricción de no utilizar librerías externas como Pandas o Numpy.

Para ejecutar el sistema y generar los reportes en la carpeta salidas/, utiliza el siguiente comando:
```bash
python main.py
```

**Elaboro: Roony Roldan Cruz**

**boleta: 2025630608**

**Materia: Programación para Ciencia de Datos**