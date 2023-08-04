from sqlalchemy import Column, Integer, String, Boolean, VARCHAR, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, Field
from typing import Optional, List
from src.models.http.response_model import response_model_factory

Base = declarative_base()


class ParceiroORM(Base):
    __tablename__ = "parceiros"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    sobre_nome = Column(String(100))
    empresa = Column(String(50), nullable=True)
    e_empresa = Column(Boolean, nullable=False, default=False)
    telefone = Column(VARCHAR(11), nullable=False)


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
