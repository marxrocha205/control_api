from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True)

    senha = Column(String)

    empresa_id = Column(Integer, ForeignKey("empresas.id"))