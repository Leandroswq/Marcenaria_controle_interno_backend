from pydantic import BaseModel, Field
from typing import Optional, List
from src.models.http.response_model import response_model_factory


class ClienteWithoutIdModel(BaseModel):
    nome: str
    sobre_nome: Optional[str] = None
    telefone: str = Field(..., example="12345678901")
    empresa: Optional[str] = None
    e_empresa: bool = Field(..., example=True)

    def __str__(self):
        return (
            f"Cliente nome={self.nome}, sobre_nome={self.sobre_nome}, "
            f"telefone={self.telefone}, empresa={self.empresa}"
        )


class ClienteUpdatedModel(BaseModel):
    nome: Optional[str] = None
    sobre_nome: Optional[str] = None
    telefone: Optional[str] = None
    empresa: Optional[str] = None
    e_empresa: Optional[bool] = None


class ClienteModel(BaseModel):
    client_id: int
    nome: str = "teste"
    sobre_nome: Optional[str] = None
    telefone: str
    empresa: Optional[str] = None
    e_empresa: bool = Field(..., example=True)

    def __repr__(self):
        return (
            f"Cliente id = [id={self.client_id}, nome={self.nome}, sobre_nome={self.sobre_nome}, "
            f"telefone={self.telefone}, empresa={self.empresa}"
        )


class ClienteUpdateModel:
    client_id: int
    nome: Optional[str]
    sobre_nome: Optional[str] = None
    telefone: Optional[str]
    empresa: Optional[str] = None
    e_empresa: bool = Field(..., example=True)


ClienteModelResponse = response_model_factory(List[ClienteModel])
