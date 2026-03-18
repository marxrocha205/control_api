from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base

class Plano(Base):

    __tablename__ = "planos"

    id = Column(Integer, primary_key=True)

    nome = Column(String)

    descricao = Column(String)

    preco = Column(Float)

    duracao_dias = Column(Integer)

    empresa_id = Column(Integer, ForeignKey("empresas.id"))