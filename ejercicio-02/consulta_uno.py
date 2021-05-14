  
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# se importa la clase(s) del 
# archivo genera_base
from genera_base import Pais

# se genera enlace al gestor de base de
# datos para el ejemplo se usa la base de datos sqlite

engine = create_engine('sqlite:///basepaises.db')

Session = sessionmaker(bind=engine)
session = Session()


# Presentar todos los países del continente americano
resultado_c1 = session.query(Pais).filter(Pais.continente=="NA").all()
print(resultado_c1)








