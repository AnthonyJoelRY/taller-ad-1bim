import json
from pathlib import Path
from sqlalchemy import select
from configuracion import SessionLocal
from crear_base_entidades import Profesor, Carrera, crear_base

DATA_DIR = Path(__file__).resolve().parent / 'data' / 'datos_universidad' / 'datos'


def cargar_json(nombre_archivo):
    with open(DATA_DIR / nombre_archivo, 'r', encoding='utf-8') as f:
        return json.load(f)


def poblar_profesores():
    data = cargar_json('profesores.json')
    with SessionLocal() as session:
        for item in data:
            carrera = session.scalar(select(Carrera).where(Carrera.nombre == item['carrera']))
            if carrera is None:
                raise ValueError(f"Carrera no encontrada: {item['carrera']}")
            objeto = session.get(Profesor, item['id'])
            if objeto is None:
                objeto = Profesor(
                    id=item['id'],
                    nombres=item['nombres'],
                    apellidos=item['apellidos'],
                    correo=item['correo'],
                    especialidad=item['especialidad'],
                    carrera=carrera,
                )
                session.add(objeto)
            else:
                objeto.nombres = item['nombres']
                objeto.apellidos = item['apellidos']
                objeto.correo = item['correo']
                objeto.especialidad = item['especialidad']
                objeto.carrera = carrera
        session.commit()
        print(f'Profesores insertados o actualizados: {len(data)}')


if __name__ == '__main__':
    crear_base()
    poblar_profesores()
