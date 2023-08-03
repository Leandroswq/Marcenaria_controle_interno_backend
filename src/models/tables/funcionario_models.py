from pydantic import BaseModel, Field
from typing import Optional, List
from src.models.http.response_model import response_model_factory


class FuncionarioWithoutIdModel(BaseModel):
    nome: str
    sobre_nome: Optional[str] = None
    funcao: str
    telefone: str = Field(..., example="12345678901")

    def __str__(self):
        return (
            f"Funcionario nome={self.nome}, sobre_nome={self.sobre_nome}, "
            f"funcao={self.funcao}"
        )


class FuncionarioUpdatedModel(BaseModel):
    nome: Optional[str] = None
    sobre_nome: Optional[str] = None
    funcao: Optional[str] = None
    telefone: Optional[str] = Field(..., example="12345678901")


class FuncionarioModel(BaseModel):
    funcionario_id: int
    nome: str
    sobre_nome: Optional[str] = None
    funcao: str
    telefone: str = Field(..., example="12345678901")

    def __repr__(self):
        return (
            f"Funcionario id={self.funcionario_id}, nome={self.nome}, sobre_nome={self.sobre_nome}, "
            f"funcao={self.funcao}"
        )


FuncionarioModelResponse = response_model_factory(List[FuncionarioModel])
