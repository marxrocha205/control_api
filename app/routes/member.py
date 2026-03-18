from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.member import Aluno
from app.schemas.member import AlunoCreate

router = APIRouter(
    prefix="/alunos",
    tags=["Alunos"]
)


@router.post("/")
def criar_aluno(aluno: AlunoCreate, db: Session = Depends(get_db)):

    novo_aluno = Aluno(**aluno.dict())

    db.add(novo_aluno)

    db.commit()

    db.refresh(novo_aluno)

    return novo_aluno


@router.get("/")
def listar_alunos(db: Session = Depends(get_db)):

    return db.query(Aluno).all()


@router.get("/{aluno_id}")
def buscar_aluno(aluno_id: int, db: Session = Depends(get_db)):

    return db.query(Aluno).filter(
        Aluno.id == aluno_id
    ).first()


@router.delete("/{aluno_id}")
def deletar_aluno(aluno_id: int, db: Session = Depends(get_db)):

    aluno = db.query(Aluno).filter(
        Aluno.id == aluno_id
    ).first()

    db.delete(aluno)

    db.commit()

    return {"message": "Aluno removido"}