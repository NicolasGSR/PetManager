from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter(prefix="/pacientes", tags=["Pacientes"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.PacienteResponse])
def listar_pacientes(db: Session = Depends(get_db)):
    return crud.get_pacientes(db)

@router.post("/", response_model=schemas.PacienteResponse)
def criar_paciente(paciente: schemas.PacienteCreate, db: Session = Depends(get_db)):
    return crud.create_paciente(db, paciente)