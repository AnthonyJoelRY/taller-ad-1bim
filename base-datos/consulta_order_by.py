from sqlalchemy import select
from configuracion import SessionLocal
from crear_base_entidades import Profesor


def consulta_order_by():
    with SessionLocal() as session:
        profesores_ordenados = session.scalars(
            select(Profesor).order_by(Profesor.apellidos)
        ).all()
        print('Profesores ordenados por apellido:')
        for profesor in profesores_ordenados:
            print(profesor)


if __name__ == '__main__':
    consulta_order_by()
