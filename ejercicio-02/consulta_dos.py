from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# se importa la clase(s) del 
# archivo genera_base
from genera_base import Pais


engine = create_engine('sqlite:///basepaises.db')


Session = sessionmaker(bind=engine)
session = Session()

# * Presentar los países de Asía, ordenados por el atributo Dial.

print("====Consulta 2====")
resultado_c2= session.query(Pais).filter(Pais.continente=="AS").order_by(Pais.dial).all()
print(resultado_c2)










