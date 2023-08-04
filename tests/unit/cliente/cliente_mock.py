from typing import List
from src.models.tables.cliente_models import ClienteWithoutIdModel, ClienteModel


def generate_clientes(size) -> List[ClienteModel]:
    data = [
        ClienteModel(
            client_id=1,
            nome="John",
            sobre_nome="Doe",
            telefone="12345678901",
            empresa="Example Corp",
            e_empresa=True,
        ),
        ClienteModel(
            client_id=2,
            nome="Jane",
            sobre_nome="Smith",
            telefone="9876543210",
            empresa="Test Inc",
            e_empresa=False,
        ),
    ]
    return data[0:size]


def generate_clientes_without_id(size) -> List[ClienteWithoutIdModel]:
    data = [
        ClienteWithoutIdModel(
            nome="John",
            sobre_nome="Doe",
            telefone="12345678901",
            empresa="Example Corp",
            e_empresa=True,
        ),
        ClienteWithoutIdModel(
            nome="Jane",
            sobre_nome="Smith",
            telefone="9876543210",
            empresa="Test Inc",
            e_empresa=False,
        ),
    ]
    return data[0:size]
