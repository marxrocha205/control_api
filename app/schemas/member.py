from pydantic import BaseModel
from datetime import date

class AlunoBase(BaseModel):

    nome: str
    data_matricula: date
    data_vencimento: date
    plano: str
    address_id: int


class AlunoCreate(AlunoBase):
    pass


class Aluno(AlunoBase):

    id: int

    class Config:
        from_mode = True