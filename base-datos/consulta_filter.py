from sqlalchemy import select
from configuracion import SessionLocal
from crear_base_entidades import RecursoAcademico


def consulta_filter():
    with SessionLocal() as session:
        recursos_video = session.scalars(
            select(RecursoAcademico).where(RecursoAcademico.tipo == 'Video')
        ).all()
        print('Recursos de tipo Video:')
        for recurso in recursos_video:
            print(recurso)


if __name__ == '__main__':
    consulta_filter()
