from fastapi import FastAPI
from src.routers.cliente_router import router as cliente_router

app = FastAPI()
app.include_router(cliente_router, prefix="/cliente", tags=["cliente"])
