# Dependências reutilizáveis (injeção do FastAPI)
# Aqui vamos validar o token e pegar o usuário logado

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.config import SECRET_KEY, ALGORITHM
from app.database import get_db
from app.models.user import User


# Define padrão de autenticação Bearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    """
    Pega o usuário atual baseado no token JWT
    """

    try:
        # Decodifica o token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        email: str = payload.get("sub")

        if email is None:
            raise HTTPException(status_code=401, detail="Token inválido")

    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

    # Busca usuário no banco
    usuario = db.query(User).filter(User.email == email).first()

    if usuario is None:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")

    return usuario


def get_current_empresa(user: User = Depends(get_current_user)):
    """
    Retorna a empresa do usuário logado
    """
    return user.empresa_id