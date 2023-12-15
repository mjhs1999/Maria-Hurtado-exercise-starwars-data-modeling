import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

class Usuario(Base):
    __tablename__ = 'usuarios'
    email = Column(Integer, primary_key=True)
    usuario = Column(String(250), ForeignKey('naves_favoritas'),ForeignKey('personas_favoritas'),ForeignKey('planetas_favoritas'))
    password = Column(String(250), nullable=False)
## creating ship class
class Naves(Base):
    __tablename__ = 'naves'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    modelo = Column(String(250), nullable=False)
    clase_de_nave = Column(String(250), nullable=False)
    costo_en_creditos = Column(String(250), nullable=False)
    longitud = Column(String(250), nullable=False)
    capacidad_de_pasajeros = Column(Integer, nullable=False)
    MGLT = Column(String(250), nullable=False)
    capacidad_de_carga = Column(Integer, nullable=False)
    provisiones = Column(Integer, nullable=False)
    hypermotor = Column(String(250), nullable=False)

    ##creating person class
    ##creating planets
    ##creating favs
render_er(Base, 'diagram.png')
