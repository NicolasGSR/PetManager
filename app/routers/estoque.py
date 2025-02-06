from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import database, models, schemas

router = APIRouter(prefix="/estoque", tags=["Estoque"])

@router.get("/")
def listar_estoque(db: Session = Depends(database.SessionLocal)):
    return db.query(models.ItemEstoque).all()

@router.post("/")
def adicionar_item(nome: str, quantidade: int, db: Session = Depends(database.SessionLocal)):
    item = models.ItemEstoque(nome=nome, quantidade=quantidade)
    db.add(item)
    db.commit()
    return item