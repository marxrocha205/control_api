from sqlalchemy.orm import Session
from app.models.cliente import Cliente


def criar_cliente(db: Session, dados: dict):
    cliente = Cliente(**dados)
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente


def listar_clientes(db: Session, empresa_id: int):
    return db.query(Cliente).filter(
        Cliente.empresa_id == empresa_id
    ).all()


def buscar_cliente(db: Session, cliente_id: int, empresa_id: int):
    return db.query(Cliente).filter(
        Cliente.id == cliente_id,
        Cliente.empresa_id == empresa_id
    ).first()