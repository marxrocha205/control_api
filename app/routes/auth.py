from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.auth import LoginSchema
from app.schemas.user import UserCreate
from app.core.security import hash_senha, verificar_senha, criar_token


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register")
def registrar(user: UserCreate, db: Session = Depends(get_db)):
    """
    Cria novo usuário (admin da empresa)
    """

    # Verifica se já existe usuário com esse email
    usuario_existente = db.query(User).filter(
        User.email == user.email
    ).first()

    if usuario_existente:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    # Cria usuário com senha criptografada
    novo_usuario = User(
        email=user.email,
        senha=hash_senha(user.senha),
        empresa_id=user.empresa_id
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return {"message": "Usuário criado com sucesso"}


@router.post("/login")
def login(dados: LoginSchema, db: Session = Depends(get_db)):
    """
    Realiza login e retorna token JWT
    """

    usuario = db.query(User).filter(
        User.email == dados.email
    ).first()

    if not usuario:
        raise HTTPException(status_code=400, detail="Usuário não encontrado")

    # Verifica senha
    if not verificar_senha(dados.senha, usuario.senha):
        raise HTTPException(status_code=400, detail="Senha inválida")

    # Cria token com dados do usuário
    token = criar_token({
        "sub": usuario.email,
        "empresa_id": usuario.empresa_id
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }