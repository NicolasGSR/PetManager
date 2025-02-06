from fastapi import FastAPI
from app.routers import pacientes, auth, estoque

app = FastAPI()

app.include_router(pacientes.router)
app.include_router(auth.router)
app.include_router(estoque.router)

@app.get("/")
def root():
    return {"message": "VetManager API is running 🚀"}