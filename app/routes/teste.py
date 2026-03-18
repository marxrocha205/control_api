from fastapi import APIRouter, Depends

from app.core.deps import get_current_user, get_current_empresa
from app.models.user import User

router = APIRouter(
    prefix="/teste",
    tags=["Teste"]
)


@router.get("/")
def rota_protegida(
    user: User = Depends(get_current_user),
    empresa_id: int = Depends(get_current_empresa)
):
    """
    Rota protegida que só funciona com token válido
    """

    return {
        "mensagem": "Você está autenticado",
        "usuario": user.email,
        "empresa_id": empresa_id
    }