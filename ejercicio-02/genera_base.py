from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basepaises.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Pais(Base):
    __tablename__ = 'paises'
    
    id = Column(Integer, primary_key=True)
    nombre_pais = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geoname_ID = Column(Integer)
    itu = Column(String)
    lenguajes = Column(String)
    estado_dependencia = Column(String)

    def __repr__(self):
            return "|||Pais: nombre_pais: %s | capital : %s  | continente : %s | dial : %s | geonameID : %s | itu : %s | lenguajes : %s | estado_dependencia: %s" % (
                            self.nombre_pais, 
                            self.capital, 
                            self.continente,
                            self.dial,
                            self.geoname_ID,
                            self.itu,
                            self.lenguajes,
                            self.estado_dependencia +"\n")
    

Base.metadata.create_all(engine)