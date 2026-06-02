# Evidencias del taller

## Objetivo
- Crear el modelo de datos de una universidad con Facultades, Carreras, Profesores y Recursos Académicos.
- Usar SQLAlchemy para crear la base y cargar los datos desde los JSON existentes.
- Ejecutar consultas con `all`, `filter`, `order_by`, `or_` y `and_`.

## Archivos creados / usados
- `base-datos/configuracion.py`
- `base-datos/crear_base_entidades.py`
- `base-datos/poblar_base1.py`
- `base-datos/poblar_base2.py`
- `base-datos/poblar_base3.py`
- `base-datos/poblar_base4.py`
- `base-datos/consulta_all.py`
- `base-datos/consulta_filter.py`
- `base-datos/consulta_order_by.py`
- `base-datos/consulta_or.py`
- `base-datos/consulta_and.py`
- `base-datos/data/datos_universidad/datos/*.json`

## Dependencias
- Instalar SQLAlchemy con:

```bash
pip install -r base-datos/requirements.txt
```

## Ejecución
1. Crear la base de datos:
   ```bash
   python crear_base_entidades.py
   ```
2. Poblar desde JSON:
   ```bash
   python poblar_base1.py
   python poblar_base2.py
   python poblar_base3.py
   python poblar_base4.py
   ```
3. Ejecutar consultas de ejemplo:
   ```bash
   python consulta_all.py
   python consulta_filter.py
   python consulta_order_by.py
   python consulta_or.py
   python consulta_and.py
   ```
