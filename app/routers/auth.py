from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database, models, schemas
from passlib.context import CryptContext
from jose import JWTError, jwt

router = APIRouter(prefix="/auth", tags=["Autenticação"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register")
def register(username: str, password: str, db: Session = Depends(database.SessionLocal)):
    hashed_password = pwd_context.hash(password)
    db_user = models.Usuario(username=username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    return {"message": "Usuário criado com sucesso"}