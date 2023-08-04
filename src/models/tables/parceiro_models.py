from pydantic import BaseModel, Field
from typing import Optional, List
from src.models.http.response_model import response_model_factory


class ParceiroWithoutIdModel(BaseModel):
    nome: str
    sobre_nome: Optional[str] = None
    empresa: Optional[str] = None
    e_empresa: Optional[bool] = False
    telefone: str = Field(..., example="12345678901")

    def __str__(self):
        return (
            f"Parceiro nome={self.nome}, sobre_nome={self.sobre_nome}, "
            f"empresa={self.empresa}, e_empresa={self.e_empresa}"
        )


class ParceiroUpdatedModel(BaseModel):
    nome: Optional[str] = None
    sobre_nome: Optional[str] = None
    empresa: Optional[str] = None
    e_empresa: Optional[bool] = None
    telefone: Optional[str] = Field(..., example="12345678901")


class ParceiroModel(BaseModel):
    parceiro_id: int
    nome: str
    sobre_nome: Optional[str] = None
    empresa: Optional[str] = None
    e_empresa: Optional[bool] = False
    telefone: str = Field(..., example="12345678901")

    def __repr__(self):
        return (
            f"Parceiro id={self.parceiro_id}, nome={self.nome}, sobre_nome={self.sobre_nome}, "
            f"empresa={self.empresa}, e_empresa={self.e_empresa}"
        )


ParceiroModelResponse = response_model_factory(List[ParceiroModel])
