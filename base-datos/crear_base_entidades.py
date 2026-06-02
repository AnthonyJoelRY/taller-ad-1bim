from datetime import date
from sqlalchemy import Column, Date, ForeignKey, Integer, String, create_engine, text
from sqlalchemy.orm import relationship
from urllib.parse import urlparse, urlunparse
from configuracion import Base, engine, SQLALCHEMY_DATABASE_URI

class Facultad(Base):
    __tablename__ = 'facultades'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(150), unique=True, nullable=False)
    ubicacion = Column(String(150), nullable=False)
    decano = Column(String(120), nullable=False)
    carreras = relationship('Carrera', back_populates='facultad', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Facultad(id={self.id}, nombre='{self.nombre}', ubicacion='{self.ubicacion}', decano='{self.decano}')>"

class Carrera(Base):
    __tablename__ = 'carreras'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(200), unique=True, nullable=False)
    codigo = Column(String(50), unique=True, nullable=False)
    facultad_id = Column(Integer, ForeignKey('facultades.id'), nullable=False)
    facultad = relationship('Facultad', back_populates='carreras')
    profesores = relationship('Profesor', back_populates='carrera', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Carrera(id={self.id}, nombre='{self.nombre}', codigo='{self.codigo}', facultad='{self.facultad.nombre if self.facultad else None}')>"

class Profesor(Base):
    __tablename__ = 'profesores'

    id = Column(Integer, primary_key=True)
    nombres = Column(String(120), nullable=False)
    apellidos = Column(String(120), nullable=False)
    correo = Column(String(200), unique=True, nullable=False)
    especialidad = Column(String(150), nullable=False)
    carrera_id = Column(Integer, ForeignKey('carreras.id'), nullable=False)
    carrera = relationship('Carrera', back_populates='profesores')
    recursos = relationship('RecursoAcademico', back_populates='profesor', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Profesor(id={self.id}, nombre='{self.nombres} {self.apellidos}', correo='{self.correo}', carrera='{self.carrera.nombre if self.carrera else None}')>"

class RecursoAcademico(Base):
    __tablename__ = 'recursos_academicos'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(250), nullable=False)
    fecha_publicacion = Column(Date, nullable=False)
    tipo = Column(String(80), nullable=False)
    url = Column(String(250), nullable=False)
    profesor_id = Column(Integer, ForeignKey('profesores.id'), nullable=False)
    profesor = relationship('Profesor', back_populates='recursos')

    def __repr__(self):
        return f"<RecursoAcademico(id={self.id}, titulo='{self.titulo}', tipo='{self.tipo}', profesor='{self.profesor.nombres} {self.profesor.apellidos}' if self.profesor else None)>"


def ensure_database_exists():
    if SQLALCHEMY_DATABASE_URI.startswith('sqlite://'):
        return

    parsed = urlparse(SQLALCHEMY_DATABASE_URI)
    db_name = parsed.path.lstrip('/')
    if not db_name:
        return

    parsed_no_db = parsed._replace(path='', params='', query='', fragment='')
    uri_no_db = urlunparse(parsed_no_db)

    engine_no_db = create_engine(
        uri_no_db,
        echo=False,
        future=True,
        isolation_level='AUTOCOMMIT' if parsed.scheme.startswith('postgresql') else None,
    )

    with engine_no_db.connect() as connection:
        if parsed.scheme.startswith('mysql'):
            connection.execute(text(f'CREATE DATABASE IF NOT EXISTS `{db_name}`'))
        elif parsed.scheme.startswith('postgresql'):
            exists = connection.execute(
                text('SELECT 1 FROM pg_database WHERE datname = :db_name'),
                {'db_name': db_name}
            ).first()
            if exists is None:
                connection.execute(text(f'CREATE DATABASE "{db_name}"'))
        else:
            return


def crear_base():
    ensure_database_exists()
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    crear_base()
