from sqlalchemy import or_, select
from configuracion import SessionLocal
from crear_base_entidades import Carrera


def consulta_or():
    with SessionLocal() as session:
        carreras_filtradas = session.scalars(
            select(Carrera).where(
                or_(Carrera.codigo.like('%ISW%'), Carrera.codigo.like('%ADM%'))
            )
        ).all()
        print('Carreras con código ISW o ADM:')
        for carrera in carreras_filtradas:
            print(carrera)


if __name__ == '__main__':
    consulta_or()
