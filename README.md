# ae1bim-oct25-feb26


# Bases de Datos para SQLAlchemy

Este proyecto utiliza dos motores de bases de datos:

* PostgreSQL
* MariaDB

## Levantar los servicios

Ubíquese dentro de la carpeta:

```bash
cd todo-docker
```

Ejecute:

```bash
docker compose up -d
```

Verifique que los contenedores estén ejecutándose:

```bash
docker ps
```

## Interfaces gráficas

### PostgreSQL (pgAdmin)

```text
http://localhost:5050
```

### MariaDB (phpMyAdmin)

```text
http://localhost:8080
```

## Detener los servicios

```bash
docker compose down
```

## Nota

Las carpetas y archivos de datos son creados automáticamente por Docker durante el primer arranque de los contenedores.

## Analizar la siguiente problemática y solucionar

* En una universidad compuesta por varias áreas académicas, cada Facultad representa una unidad organizativa encargada de administrar carreras y coordinar actividades académicas. De cada facultad se requiere registrar un identificador único, su nombre oficial, la ubicación física dentro de la universidad y el nombre del decano que la dirige. Dentro de cada facultad se ofertan distintas Carreras, y cada una debe quedar asociada necesariamente a la facultad a la que pertenece. Para cada carrera se debe almacenar un identificador propio, su nombre completo y un código interno que la distingue de otras ofertas académicas. Las carreras están conformadas por un conjunto de Profesores, quienes imparten clases, desarrollan investigación y producen material educativo. Cada profesor debe estar vinculado a una sola carrera. Para ellos se necesita guardar un identificador, nombres y apellidos, un correo institucional y el área de especialidad que poseen dentro de su campo profesional. Además, los profesores elaboran diversos Recursos Académicos que sirven de apoyo para estudiantes y otros docentes. Estos recursos pueden ser, por ejemplo, libros, videos o guías de estudio. De cada recurso se debe registrar un identificador, su título, la fecha en que fue publicado, el tipo de recurso según su clasificación y una URL donde pueda ser consultado o descargado. Cada recurso debe estar asociado obligatoriamente al profesor que lo creó. 

* Dentro del directorio *base-datos*:
  * Usar configuracion.py donde se debe agregar información de la base de datos.
  * Usar crear_base_entidades.py para crear la información para la base de datos haciendo uso de SqlAlchemy, en función de la problemática
  * Use el directorio data/data_universidad y analice lo correspondiente para poblar la base de datos
    * Usar poblar_base1.py para que permita ingresar datos de una entidad
    * Usar poblar_base2.py para que permita ingresar datos de una entidad
    * Usar poblar_base3.py para que permita ingresar datos de una entidad
    * Usar poblar_base4.py para que permita ingresar datos de una entidad
  * Realizar consultas a las entidades de la base de datos. Un ejemplo con cada una de las siguientes funciones como: all, filter, order_by, or, and. Usar los archivos correspondientes del repositorio.

## Evidencias

* Crear una carpeta de evidencias y subir todo lo necesario que verifique el taller

## Restricciones

* No usar la librería Pandas
