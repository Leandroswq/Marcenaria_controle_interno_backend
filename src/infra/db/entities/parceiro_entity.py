from sqlalchemy import Column, Integer, String, Boolean, VARCHAR, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ParceiroEntity(Base):
    __tablename__ = "parceiros"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    sobre_nome = Column(String(100))
    empresa = Column(String(50), nullable=True)
    e_empresa = Column(Boolean, nullable=False, default=False)
    telefone = Column(VARCHAR(11), nullable=False)

    def __repr__(self):
        return f"Funcionario [id={self.id}, nome={self.nome}, sobre nome={self.sobre_nome}]"
