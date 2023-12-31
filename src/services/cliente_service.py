from typing import List
from src.interfaces.cliente_interfaces import (
    ClienteRepositoryInterface,
    ClienteServiceInterface,
)
from src.models.tables.cliente_models import ClienteModel, ClienteWithoutIdModel
from src.infra.db.repositories.cliente_repository import ClienteRepository
from src.validation.cliente_validations import (
    validate_cliente,
    validate_cliente_optional_fields,
)
from src.validation.common_validations import string_validate


class ClienteService(ClienteServiceInterface):
    def __init__(self, repository: ClienteRepositoryInterface = ClienteRepository()):
        self.__repository = repository

    def insert_cliente(self, data: ClienteWithoutIdModel) -> None:
        validate_cliente(data=data.__dict__, id_is_required=False)

        self.__repository.insert_cliente(
            nome=data.nome,
            sobre_nome=data.sobre_nome,
            telefone=data.telefone,
            empresa=data.empresa,
            e_empresa=data.e_empresa,
        )

    def select_cliente_by_nome(self, nome: str) -> List[ClienteModel]:
        string_validate(nome, max_len=100)
        clientes = self.__repository.select_cliente_by_nome(nome=nome)

        return clientes

    def select_cliente_by_id(self, cliente_id: int) -> List[ClienteModel]:
        clientes = self.__repository.select_cliente_by_id(cliente_id=cliente_id)

        return clientes

    def select_all_clientes(self) -> List[ClienteModel]:
        clientes = self.__repository.select_all_clientes()
        return clientes

    def update_cliente(self, cliente_id: int, data: dict) -> None:
        validate_cliente_optional_fields(data=data)
        data["id"] = cliente_id
        self.__repository.update_cliente(data=data)

    def delete_cliente(self, cliente_id: int) -> None:
        self.__repository.delete_cliente(cliente_id)
