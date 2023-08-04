from pydantic import BaseModel, Field
from typing import Optional, List
from src.models.http.response_model import response_model_factory


class CategoriaDeProdutoWithoutIdModel(BaseModel):
    categoria: str

    def __str__(self):
        return f"CategoriaDeProduto categoria={self.categoria}"


class CategoriaDeProdutoUpdatedModel(BaseModel):
    categoria: Optional[str] = None


class CategoriaDeProdutoModel(BaseModel):
    categoria_id: int
    categoria: str

    def __repr__(self):
        return f"CategoriaDeProduto id={self.id}, categoria={self.categoria}"


CategoriaDeProdutoModelResponse = response_model_factory(List[CategoriaDeProdutoModel])
