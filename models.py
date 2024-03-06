from sqlalchemy import Column, String, Integer, DateTime, Table, Float, ForeignKey, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session
from db_config import engine


Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    produtos = relationship('Produto', backref='pessoa', lazy=True)
    
    #Função -> Cadastrar Usuario no banco de dados. Realiza uma consulta utilizando o username, caso não o encontre, cadastra o mesmo.
    def add_user(username: str):
        if username:
            pessoa = Pessoa(username=username)
        with Session(engine) as session:
            result = session.scalars(select(Pessoa.id, Pessoa.username).where(Pessoa.username == username))
            print('resultado da consulta: ', type(result))
            if len(result.fetchall()) == 0:
                session.add(pessoa)
                try:
                    session.commit()
                except Exception as e:
                    print("Erro ao cadastrar usuario: ", e)
    
class Produto(Base):
    __tablename__= 'product'
    id = Column(Integer, primary_key=True, nullable=False)
    pessoa_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    nome = Column(String(250), nullable=False)
    link = Column(String, nullable=False)
    data_verificao = Column(DateTime, nullable=False)
    preço_inicial = Column(Float, nullable=False)
    preço_atual = Column(Float)
    melhor_preço = Column(Float)
    nome_loja = Column(String(100), nullable=False)
    data_promocao = Column(DateTime)