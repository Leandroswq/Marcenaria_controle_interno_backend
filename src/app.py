from fastapi import FastAPI
from src.routers.cliente_router import router as cliente_router
from src.routers.funcionario_router import router as funcionario_router
from src.routers.parceiro_router import router as parceiro_router
from src.routers.categorias_de_produto_router import (
    router as categoria_de_produto_router,
)

app = FastAPI()
app.include_router(cliente_router, prefix="/cliente", tags=["Cliente"])
app.include_router(funcionario_router, prefix="/funcionario", tags=["Funcionario"])
app.include_router(parceiro_router, prefix="/parceiro", tags=["Parceiro"])
app.include_router(
    categoria_de_produto_router,
    prefix="/categoria-de-produto",
    tags=["Categorias de produtos"],
)
