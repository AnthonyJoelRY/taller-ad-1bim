from sqlalchemy import select
from configuracion import SessionLocal
from crear_base_entidades import RecursoAcademico, Profesor, Carrera, Facultad
import sys


def recursos_por_facultad(nombre_facultad: str):
    with SessionLocal() as session:
        stmt = (
            select(RecursoAcademico)
            .join(RecursoAcademico.profesor)
            .join(Profesor.carrera)
            .join(Carrera.facultad)
            .where(Facultad.nombre == nombre_facultad)
            .order_by(RecursoAcademico.fecha_publicacion)
        )
        recursos = session.scalars(stmt).all()
        return recursos


def main():
    if len(sys.argv) > 1:
        facultad = ' '.join(sys.argv[1:])
    else:
        facultad = input('Nombre de la facultad: ').strip()
    if not facultad:
        print('Debe indicar el nombre de la facultad.')
        sys.exit(1)

    recursos = recursos_por_facultad(facultad)
    if not recursos:
        print(f'No se encontraron recursos para la facultad: {facultad}')
        return

    print(f'Recursos académicos para la facultad "{facultad}":\n')
    for r in recursos:
        prof = r.profesor
        carrera = prof.carrera.nombre if prof and prof.carrera else 'N/A'
        print(f'- {r.titulo} ({r.tipo}) — {r.fecha_publicacion} — Profesor: {prof.nombres} {prof.apellidos} — Carrera: {carrera} — URL: {r.url}')


if __name__ == '__main__':
    main()
