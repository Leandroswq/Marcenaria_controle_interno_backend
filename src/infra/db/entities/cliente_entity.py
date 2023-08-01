from sqlalchemy import Column, String, Integer, Boolean
from src.infra.db.settings.base import Base


class ClienteEntity(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    sobre_nome = Column(String(100))
    telefone = Column(String(11), nullable=False)
    empresa = Column(String(50))
    e_empresa = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"Cliente [id={self.id}, nome={self.nome}, sobre nome={self.sobre_nome}]"
