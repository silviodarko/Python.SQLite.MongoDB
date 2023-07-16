# Parte 1 - Implementando um Banco de Dados Relacional com SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    endereco = Column(String)

    contas = relationship("Conta", back_populates="cliente")


class Conta(Base):
    __tablename__ = "conta"

    id = Column(Integer, primary_key=True)
    numero = Column(String)
    saldo = Column(Integer)
    cliente_id = Column(Integer, ForeignKey("cliente.id"))

    cliente = relationship("Cliente", back_populates="contas")


# Parte 2 - Implementando um Banco de Dados NoSQL com Pymongo
from pymongo import MongoClient

# Conectando ao MongoDB Atlas
client = MongoClient("<url_de_conexão>")

# Criando um banco de dados
db = client["banco"]

# Definindo uma coleção "bank" para os documentos de clientes
collection = db["bank"]


# Inserindo documentos
document1 = {
    "cliente": {
        "nome": "Cliente 1",
        "endereco": "Rua A"
    },
    "contas": [
        {
            "numero": "001",
            "saldo": 1000
        }
    ]
}

document2 = {
    "cliente": {
        "nome": "Cliente 2",
        "endereco": "Rua B"
    },
    "contas": [
        {
            "numero": "002",
            "saldo": 2000
        },
        {
            "numero": "003",
            "saldo": 3000
        }
    ]
}

# Inserindo um único documento
collection.insert_one(document1)

# Inserindo vários documentos de uma vez
collection.insert_many([document2])


