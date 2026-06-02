# Datos JSON - Universidad

Estos archivos deben ser leídos desde Python para poblar la base de datos mediante SQLAlchemy.

Importante:
- Los archivos no usan claves foráneas numéricas para las relaciones.
- Cada relación debe resolverse buscando el objeto correspondiente por nombre.

Ejemplos:
- En carreras.json, el campo "facultad" contiene el nombre de la facultad.
- En profesores.json, el campo "carrera" contiene el nombre de la carrera.
- En recursos_academicos.json, el campo "profesor" contiene nombres y apellidos del profesor.

El estudiante debe buscar el objeto relacionado y asignarlo mediante la relación ORM.
