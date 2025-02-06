from pydantic import BaseModel

class PacienteBase(BaseModel):
    nome: str
    especie: str
    idade: int

class PacienteCreate(PacienteBase):
    pass

class PacienteResponse(PacienteBase):
    id: int
    class Config:
        orm_mode = True