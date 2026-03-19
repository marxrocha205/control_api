from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.repositories import cliente_repository


def criar_cliente_service(db: Session, dados: dict, empresa_id: int):
    """
    Regra de negócio:
    - valida duplicidade
    - vincula empresa
    """

    dados["empresa_id"] = empresa_id

    return cliente_repository.criar_cliente(db, dados)


def listar_clientes_service(db: Session, empresa_id: int):
    return cliente_repository.listar_clientes(db, empresa_id)


def buscar_cliente_service(db: Session, cliente_id: int, empresa_id: int):
    cliente = cliente_repository.buscar_cliente(db, cliente_id, empresa_id)

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    return cliente