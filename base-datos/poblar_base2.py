import json
from pathlib import Path
from sqlalchemy import select
from configuracion import SessionLocal
from crear_base_entidades import Carrera, Facultad, crear_base

DATA_DIR = Path(__file__).resolve().parent / 'data' / 'datos_universidad' / 'datos'


def cargar_json(nombre_archivo):
    with open(DATA_DIR / nombre_archivo, 'r', encoding='utf-8') as f:
        return json.load(f)


def poblar_carreras():
    data = cargar_json('carreras.json')
    with SessionLocal() as session:
        for item in data:
            facultad = session.scalar(select(Facultad).where(Facultad.nombre == item['facultad']))
            if facultad is None:
                raise ValueError(f"Facultad no encontrada: {item['facultad']}")
            objeto = session.get(Carrera, item['id'])
            if objeto is None:
                objeto = Carrera(
                    id=item['id'],
                    nombre=item['nombre'],
                    codigo=item['codigo'],
                    facultad=facultad,
                )
                session.add(objeto)
            else:
                objeto.nombre = item['nombre']
                objeto.codigo = item['codigo']
                objeto.facultad = facultad
        session.commit()
        print(f'Carreras insertadas o actualizadas: {len(data)}')


if __name__ == '__main__':
    crear_base()
    poblar_carreras()
