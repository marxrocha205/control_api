from pydantic import BaseModel


class PlanoBase(BaseModel):
    """
    Estrutura base do plano
    """
    nome: str
    descricao: str
    preco: float
    duracao_dias: int


class PlanoCreate(PlanoBase):
    """
    Criação de plano
    """
    pass


class PlanoUpdate(PlanoBase):
    """
    Atualização de plano
    """
    pass


class PlanoResponse(PlanoBase):
    """
    Retorno da API
    """
    id: int

    class Config:
        from_attributes = True