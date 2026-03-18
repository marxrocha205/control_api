from pydantic import BaseModel


class ClienteBase(BaseModel):
    """
    Dados base do cliente
    """
    nome: str
    email: str
    telefone: str


class ClienteCreate(ClienteBase):
    """
    Dados para criação
    """
    pass


class ClienteUpdate(ClienteBase):
    """
    Dados para atualização
    """
    pass


class ClienteResponse(ClienteBase):
    """
    Dados retornados pela API
    """
    id: int
    ativo: bool

    class Config:
        from_attributes = True