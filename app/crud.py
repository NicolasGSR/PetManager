from sqlalchemy.orm import Session
from app import models, schemas

def get_pacientes(db: Session):
    return db.query(models.Paciente).all()

def create_paciente(db: Session, paciente: schemas.PacienteCreate):
    db_paciente = models.Paciente(**paciente.dict())
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente