from typing import List
from src.interfaces.funcionario_interfaces import (
    FuncionarioRepositoryInterface,
    FuncionarioServiceInterface,
)
from src.models.tables.funcionario_models import (
    FuncionarioModel,
    FuncionarioWithoutIdModel,
)
from src.infra.db.repositories.funcionario_repository import FuncionarioRepository
from src.validation.funcionario_validations import (
    validate_funcionario,
    validate_funcionario_optional_fields,
)
from src.validation.common_validations import string_validate


class FuncionarioService(FuncionarioServiceInterface):
    def __init__(
        self, repository: FuncionarioRepositoryInterface = FuncionarioRepository()
    ):
        self.__repository = repository

    def insert_funcionario(self, data: FuncionarioWithoutIdModel) -> None:
        validate_funcionario(data=data.__dict__, id_is_required=False)

        self.__repository.insert_funcionario(
            nome=data.nome,
            sobre_nome=data.sobre_nome,
            funcao=data.funcao,
            telefone=data.telefone,
        )

    def select_funcionario_by_nome(self, nome: str) -> List[FuncionarioModel]:
        string_validate(nome, max_len=100)
        funcionarios = self.__repository.select_funcionario_by_nome(nome=nome)

        return funcionarios

    def select_funcionario_by_id(self, funcionario_id: int) -> List[FuncionarioModel]:
        funcionarios = self.__repository.select_funcionario_by_id(
            funcionario_id=funcionario_id
        )

        return funcionarios

    def select_all_funcionarios(self) -> List[FuncionarioModel]:
        funcionarios = self.__repository.select_all_funcionarios()
        return funcionarios

    def update_funcionario(self, funcionario_id: int, data: dict) -> None:
        validate_funcionario_optional_fields(data=data)
        data["id"] = funcionario_id
        self.__repository.update_funcionario(data=data)

    def delete_funcionario(self, funcionario_id: int) -> None:
        self.__repository.delete_funcionario(funcionario_id)
