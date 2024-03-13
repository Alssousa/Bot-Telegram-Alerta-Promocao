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
        
    def verificar_user(username: str):
        with Session(engine) as session:
            user = session.scalar(select(Pessoa.id).where(Pessoa.username == username))
            if user:
                print("Usuario carregado: ", user)
                return user
            else:
                print("Criando novo usuario: ", username)
                Pessoa.add_user(username)
                return Pessoa.verificar_user(username)
                
    
class Produto(Base):
    __tablename__= 'product'
    id = Column(Integer, primary_key=True, nullable=False)
    pessoa_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    nome = Column(String(400), nullable=False)
    url = Column(String, nullable=False)
    data_verificacao = Column(DateTime, nullable=False)
    preco_inicial = Column(String, nullable=False)
    preco_atual = Column(String)
    melhor_preço = Column(String)
    nome_loja = Column(String(100), nullable=False)
    data_promocao = Column(DateTime)
    
    def add_produto(nome: str, url: str, preco_inicial: str, nome_loja: str, data_verificacao: DateTime, pessoa_id):
        #print(f'Estou aqui na função add...\ndebug: nome: {nome}, preco_inicial: {preco_inicial}, nome_loja: {nome_loja}, data_verificacao: {data_verificacao}, pessoa_id: {pessoa_id}, url: {url}')
        if nome and url and preco_inicial and nome_loja and data_verificacao and pessoa_id:
            produto = Produto(nome=nome, url=url, data_verificacao=data_verificacao, preco_inicial=preco_inicial, nome_loja=nome_loja, pessoa_id=pessoa_id)
            try:
                with Session(engine) as session:
                    produtos = session.scalars(select(Produto.nome).where(Produto.pessoa_id == pessoa_id)).fetchall()
                    print("lista de produtos do usuario: ", produtos)
                    #verif_produto = any(nome == produto for produto in produtos)
                    if produtos:
                        for item in produtos:
                            print("nome: ", item, 'prod: ', item)
                            if item == nome:
                                print('Produto existente :D')
                                return f'O produto < {nome} > já está em sua lista de monitoramento. Favor aguarde. Qualquer promoção enviaremos uma notificação para você!'
                            else:
                                session.add(produto)
                                try:
                                    session.commit()
                                    return 'O produto foi adicionado em sua lista de monitoramento.'
                                except Exception as e:
                                    print(f"Erro ao cadastrar produto: ", e)
                    else:
                        session.add(produto)
                        try:
                            session.commit()
                            return 'O produto foi adicionado em sua lista de monitoramento.'
                        except Exception as e:
                            print(f"Erro ao cadastrar produto: ", e)
                        
            except Exception as e:
                print("Erro ao tentar fazer conexão com o banco de dados: ", e)