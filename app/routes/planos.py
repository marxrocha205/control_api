from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.plano import Plano
from app.schemas.plano import PlanoCreate, PlanoUpdate
from app.core.deps import get_current_empresa


router = APIRouter(
    prefix="/planos",
    tags=["Planos"]
)


@router.post("/")
def criar_plano(
    dados: PlanoCreate,
    db: Session = Depends(get_db),
    empresa_id: int = Depends(get_current_empresa)
):
    """
    Cria plano vinculado à empresa
    """

    plano = Plano(
        **dados.dict(),
        empresa_id=empresa_id  # 🔥 multi-tenant
    )

    db.add(plano)
    db.commit()
    db.refresh(plano)

    return plano


@router.get("/")
def listar_planos(
    db: Session = Depends(get_db),
    empresa_id: int = Depends(get_current_empresa)
):
    """
    Lista planos da empresa
    """

    return db.query(Plano).filter(
        Plano.empresa_id == empresa_id
    ).all()


@router.get("/{plano_id}")
def buscar_plano(
    plano_id: int,
    db: Session = Depends(get_db),
    empresa_id: int = Depends(get_current_empresa)
):
    """
    Busca plano específico
    """

    plano = db.query(Plano).filter(
        Plano.id == plano_id,
        Plano.empresa_id == empresa_id
    ).first()

    if not plano:
        raise HTTPException(status_code=404, detail="Plano não encontrado")

    return plano


@router.put("/{plano_id}")
def atualizar_plano(
    plano_id: int,
    dados: PlanoUpdate,
    db: Session = Depends(get_db),
    empresa_id: int = Depends(get_current_empresa)
):
    """
    Atualiza plano
    """

    plano = db.query(Plano).filter(
        Plano.id == plano_id,
        Plano.empresa_id == empresa_id
    ).first()

    if not plano:
        raise HTTPException(status_code=404, detail="Plano não encontrado")

    for key, value in dados.dict().items():
        setattr(plano, key, value)

    db.commit()
    db.refresh(plano)

    return plano


@router.delete("/{plano_id}")
def deletar_plano(
    plano_id: int,
    db: Session = Depends(get_db),
    empresa_id: int = Depends(get_current_empresa)
):
    """
    Remove plano
    """

    plano = db.query(Plano).filter(
        Plano.id == plano_id,
        Plano.empresa_id == empresa_id
    ).first()

    if not plano:
        raise HTTPException(status_code=404, detail="Plano não encontrado")

    db.delete(plano)
    db.commit()

    return {"message": "Plano removido com sucesso"}