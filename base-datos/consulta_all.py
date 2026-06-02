from sqlalchemy import select
from configuracion import SessionLocal
from crear_base_entidades import Facultad


def consulta_all():
    with SessionLocal() as session:
        facultades = session.scalars(select(Facultad)).all()
        print('Todas las facultades:')
        for f in facultades:
            print(f)


if __name__ == '__main__':
    consulta_all()
