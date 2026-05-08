# Reto semana 06
# Validador de codigos
Sistema de validación automática de códigos para una empresa de logística. Reemplaza el proceso manual de verificación usando **expresiones regulares** en Python para validar cuatro tipos de códigos: productos, envíos, empleados y facturas.
 
---
 
## Estructura del proyecto
 
```
reto_06/
├── reto_06_validador_codigos_SOLUCION.ipynb   # Notebook con solución completa
└── README.md
```
 
---
 
## Tipos de código soportados
 
| Tipo | Formato | Ejemplo válido |
|------|---------|----------------|
| Producto | `ABC-1234-MX` | `TEC-0001-MX` |
| Envío | `ENV-YYYY-MM-DD-NNNNNN` | `ENV-2024-03-15-001234` |
| Empleado | `EMP-XXX-NNNN` | `EMP-VEN-1234` |
| Factura | `FAC-S-NNNNNN` | `FAC-A-123456` |
 
### Reglas de validación
 
**Producto** `ABC-1234-MX`
- Categoría: exactamente 3 letras mayúsculas
- Número: exactamente 4 dígitos
- País: exactamente 2 letras mayúsculas
**Envío** `ENV-YYYY-MM-DD-NNNNNN`
- Año: 2020 – 2030
- Mes: 01 – 12
- Día: 01 – 31
- Secuencial: 6 dígitos
**Empleado** `EMP-XXX-NNNN`
- Departamento: `VEN`, `ADM`, `TEC`, `LOG` o `RHH`
- Número: 4 dígitos, no puede empezar con 0
**Factura** `FAC-S-NNNNNN`
- Serie: `A`, `B`, `C`, `D` o `E` (mayúscula)
- Número: exactamente 6 dígitos
---
 
## Funciones implementadas
 
### Parte 1 — Validación individual (40 pts)
 
```python
validar_producto(codigo)  # → {"valido": bool, "categoria", "numero", "pais"}
validar_envio(codigo)     # → {"valido": bool, "fecha", "secuencial"}
validar_empleado(codigo)  # → {"valido": bool, "departamento", "numero"}
validar_factura(codigo)   # → {"valido": bool, "serie", "numero"}
```
 
### Parte 2 — Validador universal (30 pts)
 
```python
validar_codigo(codigo)
# → {"codigo", "tipo", "valido", "detalles"}
```
 
Detecta automáticamente el tipo por prefijo y delega al validador correspondiente.
 
### Parte 3 — Procesamiento por lotes (30 pts)
 
```python
procesar_lote(lista_de_codigos)
# → {"total", "validos", "invalidos", "por_tipo": {...}, "detalle": [...]}
```
 
### Bonus — Funcionalidades extra (+10 pts)
 
```python
sugerir_correccion(codigo)              # Propone corrección en mayúsculas
validar_fecha_real(anio, mes, dia)      # Verifica fechas reales con datetime
exportar_resultados(reporte, archivo)   # Exporta el detalle a CSV
```
 
---
 
## Salida esperada (lote completo)
 
```
============================================================
                 REPORTE DE VALIDACIÓN
============================================================
 
Total procesados: 25
Válidos:   11 (44.0%)
Inválidos: 14 (56.0%)
 
Desglose por tipo:
----------------------------------------
  Producto    :   3/5   (60% válidos)
  Envio       :   2/5   (40% válidos)
  Empleado    :   3/6   (50% válidos)
  Factura     :   3/6   (50% válidos)
  Desconocido :   0/3   (0% válidos)
 
============================================================
```
 
---
 
## Cómo ejecutar
 
1. Abrir `reto_06_validador_codigos_SOLUCION.ipynb` en Jupyter Notebook o JupyterLab.
2. Seleccionar **Kernel → Restart & Run All**.
3. Verificar que todas las celdas muestren la salida esperada.
