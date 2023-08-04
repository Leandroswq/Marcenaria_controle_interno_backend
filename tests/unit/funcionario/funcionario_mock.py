from src.models.tables.funcionario_models import (
    FuncionarioWithoutIdModel,
    FuncionarioModel,
)
from typing import List


def generate_funcionarios(size) -> List[FuncionarioModel]:
    data = [
        FuncionarioModel(
            funcionario_id=1,
            nome="John",
            sobre_nome="Doe",
            funcao="Gerente",
            telefone="12345678901",
        ),
        FuncionarioModel(
            funcionario_id=2,
            nome="Jane",
            sobre_nome="Smith",
            funcao="Assistente",
            telefone="9876543210",
        ),
    ]
    return data[0:size]


def generate_funcionarios_without_id(size) -> List[FuncionarioWithoutIdModel]:
    data = [
        FuncionarioWithoutIdModel(
            nome="John",
            sobre_nome="Doe",
            funcao="Gerente",
            telefone="12345678901",
        ),
        FuncionarioWithoutIdModel(
            nome="Jane",
            sobre_nome="Smith",
            funcao="Assistente",
            telefone="9876543210",
        ),
    ]
    return data[0:size]
