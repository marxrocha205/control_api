from pydantic import BaseModel
from datetime import date


class AssinaturaBase(BaseModel):
    """
    Base da assinatura
    """
    cliente_id: int
    plano_id: int


class AssinaturaCreate(AssinaturaBase):
    """
    Criação de assinatura
    """
    pass


class AssinaturaResponse(BaseModel):
    """
    Retorno da API
    """
    id: int
    cliente_id: int
    plano_id: int
    data_inicio: date
    data_fim: date
    status: str

    class Config:
        from_attributes = True