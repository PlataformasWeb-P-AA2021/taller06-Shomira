from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and
# se importa la clase(s) del 
# archivo genera_base
from genera_base import Pais

# se genera enlace al gestor de base de datos

engine = create_engine('sqlite:///basepaises.db')

Session = sessionmaker(bind=engine)
session = Session()

#* Presentar todos los países que tengan en su cadena de nombre de país "uador" o en su cadena de capital "ito".

print("====consulta 5====")
resultado_c5 = session.query(Pais).filter(or_(Pais.nombre_pais.like("%uador%"), Pais.capital.like("%ito%"))).all() 
print(resultado_c5)





