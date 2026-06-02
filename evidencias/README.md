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


```bash
cd base-datos
pip install -r requirements.txt
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

## Cambio de motor de base de datos
Para cambiar el motor de base de datos solo tienes que editar `base-datos/configuracion.py` y comentar o descomentar la URL correspondiente.

Ejemplos en `configuracion.py`:
```python
# SQLite local
# SQLALCHEMY_DATABASE_URI = 'sqlite:///universidad.db'

# MariaDB / MySQL
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:rootpassword@localhost:3308/orm_db'

# PostgreSQL
SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost:5434/orm_db'
```

Solo debe quedar descomentada la línea del motor que quieras usar.

## Evidencias visuales
# Primera Parte.
<img width="1564" height="594" alt="image" src="https://github.com/user-attachments/assets/41116da5-1dac-4359-95ec-6ea37418b45a" />

### Imagen 1: Conexión en pgAdmin
<img width="819" height="831" alt="image" src="https://github.com/user-attachments/assets/fa721234-5fb0-4064-bdc1-a051a2e66340" />

### Imagen 2: Tablas creadas en PostgreSQL
<img width="708" height="496" alt="image" src="https://github.com/user-attachments/assets/7fce559e-b19a-4bf1-abdc-06a2039e6000" />

### Imagen 3: Conexión en phpadmin
<img width="1609" height="586" alt="image" src="https://github.com/user-attachments/assets/b735ad74-400a-42de-960a-ab151f8246a6" />

### Imagen 4: Resultados de las consultas
<img width="1372" height="607" alt="image" src="https://github.com/user-attachments/assets/8d974563-1c5d-48e8-964b-4f28195c787a" />

### Imagen 5: Resultados de las consultas + consulta nueva
<img width="1738" height="265" alt="image" src="https://github.com/user-attachments/assets/55d477ba-c325-4f53-8e47-e98be0c648db" />


