from typing import List
from src.interfaces.parceiro_interfaces import (
    ParceiroRepositoryInterface,
    ParceiroServiceInterface,
)
from src.models.tables.parceiro_models import (
    ParceiroModel,
    ParceiroWithoutIdModel,
)
from src.infra.db.repositories.parceiro_repository import ParceiroRepository
from src.validation.parceiro_validations import (
    validate_parceiro,
    validate_parceiro_optional_fields,
)
from src.validation.common_validations import string_validate


class ParceiroService(ParceiroServiceInterface):
    def __init__(self, repository: ParceiroRepositoryInterface = ParceiroRepository()):
        self.__repository = repository

    def insert_parceiro(self, data: ParceiroWithoutIdModel) -> None:
        validate_parceiro(data=data.__dict__, id_is_required=False)

        self.__repository.insert_parceiro(
            nome=data.nome,
            sobre_nome=data.sobre_nome,
            empresa=data.empresa,
            e_empresa=data.e_empresa,
            telefone=data.telefone,
        )

    def select_parceiro_by_nome(self, nome: str) -> List[ParceiroModel]:
        string_validate(nome, max_len=100)
        parceiros = self.__repository.select_parceiro_by_nome(nome=nome)
        return parceiros

    def select_parceiro_by_id(self, parceiro_id: int) -> List[ParceiroModel]:
        parceiros = self.__repository.select_parceiro_by_id(parceiro_id=parceiro_id)
        return parceiros

    def select_all_parceiros(self) -> List[ParceiroModel]:
        parceiros = self.__repository.select_all_parceiros()
        return parceiros

    def update_parceiro(self, parceiro_id: int, data: dict) -> None:
        validate_parceiro_optional_fields(data=data)
        data["id"] = parceiro_id
        self.__repository.update_parceiro(data=data)

    def delete_parceiro(self, parceiro_id: int) -> None:
        self.__repository.delete_parceiro(parceiro_id)
