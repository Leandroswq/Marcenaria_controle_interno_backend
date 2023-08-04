from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CategoriaDeProdutoEntity(Base):
    __tablename__ = "categorias_de_produto"

    id = Column(Integer, primary_key=True, autoincrement=True)
    categoria = Column(String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"<CategoriaDeProduto(id={self.id}, categoria='{self.categoria}')>"
