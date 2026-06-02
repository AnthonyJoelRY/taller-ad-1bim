import json
from datetime import datetime
from pathlib import Path
from sqlalchemy import select
from configuracion import SessionLocal
from crear_base_entidades import RecursoAcademico, Profesor, crear_base

DATA_DIR = Path(__file__).resolve().parent / 'data' / 'datos_universidad' / 'datos'


def cargar_json(nombre_archivo):
    with open(DATA_DIR / nombre_archivo, 'r', encoding='utf-8') as f:
        return json.load(f)


def parse_fecha(valor):
    return datetime.strptime(valor, '%Y-%m-%d').date()


def poblar_recursos():
    data = cargar_json('recursos_academicos.json')
    with SessionLocal() as session:
        for item in data:
            nombre_completo = item['profesor']
            try:
                nombres, apellidos = nombre_completo.split(' ', 1)
            except ValueError:
                raise ValueError(f"Formato incorrecto de profesor: {nombre_completo}")
            profesor = session.scalar(
                select(Profesor).where(
                    Profesor.nombres == nombres,
                    Profesor.apellidos == apellidos,
                )
            )
            if profesor is None:
                raise ValueError(f"Profesor no encontrado: {nombre_completo}")
            objeto = session.get(RecursoAcademico, item['id'])
            if objeto is None:
                objeto = RecursoAcademico(
                    id=item['id'],
                    titulo=item['titulo'],
                    fecha_publicacion=parse_fecha(item['fecha_publicacion']),
                    tipo=item['tipo'],
                    url=item['url'],
                    profesor=profesor,
                )
                session.add(objeto)
            else:
                objeto.titulo = item['titulo']
                objeto.fecha_publicacion = parse_fecha(item['fecha_publicacion'])
                objeto.tipo = item['tipo']
                objeto.url = item['url']
                objeto.profesor = profesor
        session.commit()
        print(f'Recursos académicos insertados o actualizados: {len(data)}')


if __name__ == '__main__':
    crear_base()
    poblar_recursos()
