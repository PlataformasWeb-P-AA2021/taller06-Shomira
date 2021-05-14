from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import requests
from genera_base import Pais

import json

# se genera en enlace al gestor de base de
# datos para el ejemplo se usa la base de datos sqlite
engine = create_engine('sqlite:///basepaises.db')


Session = sessionmaker(bind=engine)
session = Session()

data_json = requests.get('https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json')
datos = json.loads(data_json.content)

# print(datos)

for d in datos:
    print(d)
    p = Pais(nombre_pais=d['CLDR display name'], capital=d['Capital'], continente=d['Continent'], \
            dial=d['Dial'], geoname_ID=d['Geoname ID'], itu=d['ITU'], lenguajes=d['Languages'], estado_dependencia=d['is_independent'])
    session.add(p)

# confirmar transacciones
session.commit()