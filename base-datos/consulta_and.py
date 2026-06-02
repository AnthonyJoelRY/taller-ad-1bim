from sqlalchemy import and_, select
from configuracion import SessionLocal
from crear_base_entidades import Profesor


def consulta_and():
    with SessionLocal() as session:
        profesores_filtrados = session.scalars(
            select(Profesor).where(
                and_(
                    Profesor.especialidad == 'Bases de Datos',
                    Profesor.correo.like('%@universidad.edu')
                )
            )
        ).all()
        print('Profesores con especialidad Bases de Datos y correo institucional:')
        for profesor in profesores_filtrados:
            print(profesor)


if __name__ == '__main__':
    consulta_and()
