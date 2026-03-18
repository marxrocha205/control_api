from sqlalchemy import Column, Integer, Date, String, ForeignKey
from app.database import Base

class Assinatura(Base):

    __tablename__ = "assinaturas"

    id = Column(Integer, primary_key=True)

    cliente_id = Column(Integer, ForeignKey("clientes.id"))

    plano_id = Column(Integer, ForeignKey("planos.id"))

    data_inicio = Column(Date)

    data_fim = Column(Date)

    status = Column(String)  # ativa, vencida, cancelada

    empresa_id = Column(Integer, ForeignKey("empresas.id"))