#pip install sqlalchemy
from sqlalchemy import create_engine, text, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
#from sqlalchemy.ext.declarative import declarative_base
import datetime

HOST = 'DESKTOP-T1J5D35\SQLEXPRESS'
BANCO = 'Aula4'
DRIVER = 'ODBC Driver 17 for SQL Server'

CONN = f'mssql+pyodbc://{HOST}/{BANCO}?trusted_connection=yes&driver={DRIVER}'


engine = create_engine(CONN, echo=True)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'Pessoa'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    usuario = Column(String(20))
    senha = Column(String(10))

class Tokens(Base):
    __tablename__ = 'Tokens'
    id = Column(Integer, primary_key=True)
    id_pessoa = Column(Integer, ForeignKey('Pessoa.id'))
    token = Column(String(100))
    data = Column(DateTime, default=datetime.datetime.utcnow())

Base.metadata.create_all(engine)