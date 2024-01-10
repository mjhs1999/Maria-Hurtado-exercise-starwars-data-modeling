from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    email = Column(String(250), primary_key=True)
    usuario = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Naves(Base):
    __tablename__ = 'naves'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    # Other columns...

class Personas(Base):
    __tablename__ = 'personas'
    id = Column(Integer, primary_key=True)
    # Other columns...

class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    # Other columns...

class Naves_favoritas(Base):
    __tablename__ = 'naves_favoritas'
    id = Column(Integer, primary_key=True)
    nave_id = Column(Integer, ForeignKey('naves.id'))
    usuario_id = Column(String(250), ForeignKey('usuarios.email'))

class Personas_favoritas(Base):
    __tablename__ = 'personas_favoritas'
    id = Column(Integer, primary_key=True)
    persona_id = Column(Integer, ForeignKey('personas.id'))
    usuario_id = Column(String(250), ForeignKey('usuarios.email'))

class Planetas_favoritas(Base):
    __tablename__ = 'planetas_favoritas'
    id = Column(Integer, primary_key=True)
    planeta_id = Column(Integer, ForeignKey('planetas.id'))
    usuario_id = Column(String(250), ForeignKey('usuarios.email'))

# Optionally, generate an entity-relationship diagram (ERD) for your models
render_er(Base, 'diagram.png')
