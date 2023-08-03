from sqlalchemy import Column, String, Integer, CheckConstraint
from src.infra.db.settings.base import Base


class FuncionarioEntity(Base):
    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    sobre_nome = Column(String(100))
    funcao = Column(String(50), nullable=False)
    telefone = Column(String(11), nullable=False)

    __table_args__ = (
        CheckConstraint(
            "LENGTH(telefone) = 11", name="ck_funcionarios_telefone_length"
        ),
    )

    def __repr__(self):
        return f"Funcionario [id={self.id}, nome={self.nome}, sobre nome={self.sobre_nome}, funcao={self.funcao}]"
