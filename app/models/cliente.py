from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database import Base

class Cliente(Base):

    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String)

    email = Column(String)

    telefone = Column(String)

    ativo = Column(Boolean, default=True)

    empresa_id = Column(Integer, ForeignKey("empresas.id"))