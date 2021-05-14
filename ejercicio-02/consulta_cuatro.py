
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_base
from genera_base import Pais

# se genera enlace al gestor de base de
# datos

engine = create_engine('sqlite:///basepaises.db')


Session = sessionmaker(bind=engine)
session = Session()

#* Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa
print("====consulta 4====")
resultado_c4 = session.query(Pais).filter(Pais.continente == "EU").order_by(Pais.capital).all()
print(resultado_c4)







