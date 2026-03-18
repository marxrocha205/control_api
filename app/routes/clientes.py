from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.cliente import Cliente
from app.schemas.cliente import ClienteCreate, ClienteUpdate
from app.core.deps import get_current_empresa


router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)


@router.post("/")
def criar_cliente(
    dados: ClienteCreate,
    db: Session = Depends(get_db),
    empresa_id: int = Depends(get_current_empresa)
):
    """
    Cria cliente vinculado à empresa do usuário
    """

    cliente = Cliente(
        **dados.dict(),
        empresa_id=empresa_id  # 🔥 vínculo automático
    )

    db.add(cliente)
    db.commit()
    db.refresh(cliente)

    return cliente


@router.get("/")
def listar_clientes(
    db: Session = Depends(get_db),
    empresa_id: int = Depends(get_current_empresa)
):
    """
    Lista apenas clientes da empresa do usuário
    """

    return db.query(Cliente).filter(
        Cliente.empresa_id == empresa_id
    ).all()


@router.get("/{cliente_id}")
def buscar_cliente(
    cliente_id: int,
    db: Session = Depends(get_db),
    empresa_id: int = Depends(get_current_empresa)
):
    """
    Busca cliente específico da empresa
    """

    cliente = db.query(Cliente).filter(
        Cliente.id == cliente_id,
        Cliente.empresa_id == empresa_id
    ).first()

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    return cliente


@router.put("/{cliente_id}")
def atualizar_cliente(
    cliente_id: int,
    dados: ClienteUpdate,
    db: Session = Depends(get_db),
    empresa_id: int = Depends(get_current_empresa)
):
    """
    Atualiza cliente da empresa
    """

    cliente = db.query(Cliente).filter(
        Cliente.id == cliente_id,
        Cliente.empresa_id == empresa_id
    ).first()

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    for key, value in dados.dict().items():
        setattr(cliente, key, value)

    db.commit()
    db.refresh(cliente)

    return cliente


@router.delete("/{cliente_id}")
def deletar_cliente(
    cliente_id: int,
    db: Session = Depends(get_db),
    empresa_id: int = Depends(get_current_empresa)
):
    """
    Remove cliente (soft delete opcional futuramente)
    """

    cliente = db.query(Cliente).filter(
        Cliente.id == cliente_id,
        Cliente.empresa_id == empresa_id
    ).first()

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    db.delete(cliente)
    db.commit()

    return {"message": "Cliente removido com sucesso"}