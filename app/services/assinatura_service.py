# Responsável pela lógica automática de assinaturas

from datetime import date
from sqlalchemy.orm import Session

from app.models.assinatura import Assinatura


def atualizar_status_assinaturas(db: Session):
    """
    Atualiza assinaturas vencidas automaticamente
    """

    hoje = date.today()

    assinaturas = db.query(Assinatura).all()

    for assinatura in assinaturas:

        # Se passou da data e ainda está ativa
        if assinatura.data_fim < hoje and assinatura.status == "ativa":
            assinatura.status = "vencida"

    db.commit()


def buscar_vencendo_hoje(db: Session):
    """
    Retorna assinaturas que vencem hoje
    """

    hoje = date.today()

    return db.query(Assinatura).filter(
        Assinatura.data_fim == hoje,
        Assinatura.status == "ativa"
    ).all()


def buscar_vencidas(db: Session):
    """
    Retorna assinaturas já vencidas
    """

    return db.query(Assinatura).filter(
        Assinatura.status == "vencida"
    ).all()