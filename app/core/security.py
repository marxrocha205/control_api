# Responsável por:
# - Gerar hash de senha
# - Verificar senha
# - Criar token JWT

from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES


# Configuração do algoritmo de hash de senha
# bcrypt é padrão de mercado
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_senha(senha: str):
    """
    Converte senha em hash seguro.
    Nunca salvamos senha em texto puro.
    """
    return pwd_context.hash(senha)


def verificar_senha(senha: str, senha_hash: str):
    """
    Verifica se a senha digitada bate com o hash armazenado.
    """
    return pwd_context.verify(senha, senha_hash)


def criar_token(dados: dict):
    """
    Cria token JWT com tempo de expiração.
    """
    dados_copy = dados.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    dados_copy.update({"exp": expire})

    token = jwt.encode(dados_copy, SECRET_KEY, algorithm=ALGORITHM)

    return token