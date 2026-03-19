from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.cliente import ClienteCreate
from app.services.cliente_service import (
    criar_cliente_service,
    listar_clientes_service
)
from app.core.deps import get_current_empresa


router = APIRouter(prefix="/clientes", tags=["Clientes"])


@router.post("/")
def criar_cliente(
    dados: ClienteCreate,
    db: Session = Depends(get_db),
    empresa_id: int = Depends(get_current_empresa)
):
    return criar_cliente_service(db, dados.dict(), empresa_id)


@router.get("/")
def listar_clientes(
    db: Session = Depends(get_db),
    empresa_id: int = Depends(get_current_empresa)
):
    return listar_clientes_service(db, empresa_id)