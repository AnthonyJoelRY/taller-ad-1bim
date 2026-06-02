from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#Para probar con diferentes motores de base de datos solo descomenta la línea que corresponda al que quiera usar.

# SQLite local (recomendado para pruebas sin servidor externo)
SQLALCHEMY_DATABASE_URI = 'sqlite:///universidad.db'

# MariaDB / MySQL
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:rootpassword@localhost:3308/orm_db'

# PostgreSQL
# SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost:5434/orm_db'

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, future=True)
Base = declarative_base()
