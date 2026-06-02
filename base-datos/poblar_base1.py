import json
from pathlib import Path
from sqlalchemy import select
from configuracion import SessionLocal
from crear_base_entidades import Facultad, crear_base

DATA_DIR = Path(__file__).resolve().parent / 'data' / 'datos_universidad' / 'datos'


def cargar_json(nombre_archivo):
    with open(DATA_DIR / nombre_archivo, 'r', encoding='utf-8') as f:
        return json.load(f)


def poblar_facultades():
    data = cargar_json('facultades.json')
    with SessionLocal() as session:
        for item in data:
            objeto = session.get(Facultad, item['id'])
            if objeto is None:
                objeto = Facultad(
                    id=item['id'],
                    nombre=item['nombre'],
                    ubicacion=item['ubicacion'],
                    decano=item['decano'],
                )
                session.add(objeto)
            else:
                objeto.nombre = item['nombre']
                objeto.ubicacion = item['ubicacion']
                objeto.decano = item['decano']
        session.commit()
        print(f'Facultades insertadas o actualizadas: {len(data)}')


if __name__ == '__main__':
    crear_base()
    poblar_facultades()
