from pydantic import BaseModel


class UserCreate(BaseModel):
    """
    Dados para criar usuário
    """
    email: str
    senha: str
    empresa_id: int


class UserResponse(BaseModel):
    """
    Dados retornados ao cliente (sem senha)
    """
    id: int
    email: str
    empresa_id: int

    class Config:
        from_attributes = True