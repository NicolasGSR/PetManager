from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Paciente(Base):
    __tablename__ = "pacientes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    especie = Column(String)
    idade = Column(Integer)

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class ItemEstoque(Base):
    __tablename__ = "estoque"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    quantidade = Column(Integer)