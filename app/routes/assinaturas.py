from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date, timedelta

from app.database import get_db
from app.models.assinatura import Assinatura
from app.models.plano import Plano
from app.models.cliente import Cliente

from app.schemas.assinatura import AssinaturaCreate
from app.core.deps import get_current_empresa


router = APIRouter(
    prefix="/assinaturas",
    tags=["Assinaturas"]
)


@router.post("/")
def criar_assinatura(
    dados: AssinaturaCreate,
    db: Session = Depends(get_db),
    empresa_id: int = Depends(get_current_empresa)
):
    """
    Cria assinatura com cálculo automático de vencimento
    """

    # 🔍 valida cliente
    cliente = db.query(Cliente).filter(
        Cliente.id == dados.cliente_id,
        Cliente.empresa_id == empresa_id
    ).first()

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    # 🔍 valida plano
    plano = db.query(Plano).filter(
        Plano.id == dados.plano_id,
        Plano.empresa_id == empresa_id
    ).first()

    if not plano:
        raise HTTPException(status_code=404, detail="Plano não encontrado")

    # 📅 regras de negócio
    data_inicio = date.today()
    data_fim = data_inicio + timedelta(days=plano.duracao_dias)

    assinatura = Assinatura(
        cliente_id=dados.cliente_id,
        plano_id=dados.plano_id,
        data_inicio=data_inicio,
        data_fim=data_fim,
        status="ativa",
        empresa_id=empresa_id
    )

    db.add(assinatura)
    db.commit()
    db.refresh(assinatura)

    return assinatura


@router.get("/")
def listar_assinaturas(
    db: Session = Depends(get_db),
    empresa_id: int = Depends(get_current_empresa)
):
    """
    Lista assinaturas da empresa
    """

    return db.query(Assinatura).filter(
        Assinatura.empresa_id == empresa_id
    ).all()


@router.get("/{assinatura_id}")
def buscar_assinatura(
    assinatura_id: int,
    db: Session = Depends(get_db),
    empresa_id: int = Depends(get_current_empresa)
):
    """
    Busca assinatura específica
    """

    assinatura = db.query(Assinatura).filter(
        Assinatura.id == assinatura_id,
        Assinatura.empresa_id == empresa_id
    ).first()

    if not assinatura:
        raise HTTPException(status_code=404, detail="Assinatura não encontrada")

    return assinatura


@router.put("/{assinatura_id}/cancelar")
def cancelar_assinatura(
    assinatura_id: int,
    db: Session = Depends(get_db),
    empresa_id: int = Depends(get_current_empresa)
):
    """
    Cancela assinatura
    """

    assinatura = db.query(Assinatura).filter(
        Assinatura.id == assinatura_id,
        Assinatura.empresa_id == empresa_id
    ).first()

    if not assinatura:
        raise HTTPException(status_code=404, detail="Assinatura não encontrada")

    assinatura.status = "cancelada"

    db.commit()
    db.refresh(assinatura)

    return assinatura