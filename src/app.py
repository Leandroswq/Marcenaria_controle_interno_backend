from fastapi import FastAPI
from src.routers.cliente_router import router as cliente_router
from src.routers.funcionario_router import router as funcionario_router
from src.routers.parceiro_router import router as parceiro_router

app = FastAPI()
app.include_router(cliente_router, prefix="/cliente", tags=["Cliente"])
app.include_router(funcionario_router, prefix="/funcionario", tags=["Funcionario"])
app.include_router(parceiro_router, prefix="/parceiro", tags=["Parceiro"])
