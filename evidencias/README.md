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
Agrega aquí las capturas de pantalla o imágenes de la configuración y los resultados.

### Imagen 1: Conexión en pgAdmin
![pgAdmin servidor](./img_pgadmin_servidor.png)

### Imagen 2: Tablas creadas en PostgreSQL
![Tablas en PostgreSQL](./img_pgadmin_tablas.png)

### Imagen 3: Resultados de las consultas
![Resultados consultas](./img_consultas.png)
