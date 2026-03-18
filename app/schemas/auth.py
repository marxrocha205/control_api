from pydantic import BaseModel


class LoginSchema(BaseModel):
    """
    Dados recebidos no login
    """
    email: str
    senha: str


class TokenSchema(BaseModel):
    """
    Resposta do login
    """
    access_token: str
    token_type: str