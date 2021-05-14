from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_base
from genera_base import Pais

# se genera enlace al gestor de base de datos


engine = create_engine('sqlite:///basepaises.db')


Session = sessionmaker(bind=engine)
session = Session()
#* Presentar los lenguajes de cada país.
# Obtener todos los registros de Pais unicamente el nombre y el los lenguajes
print("====consulta 3====")

resultado_c3 = session.query(Pais.nombre_pais,Pais.lenguajes).all()
print(resultado_c3)

for i in resultado_c3:
    print("Pais:  %s y sus Lenguanjes:  %s"% ( i[0] , i[1]))
