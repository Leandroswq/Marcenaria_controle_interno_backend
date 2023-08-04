from typing import List
from src.infra.db.entities.parceiro_entity import ParceiroEntity
from src.interfaces.parceiro_interfaces import ParceiroRepositoryInterface
from src.models.tables.parceiro_models import ParceiroModel
from src.infra.db.settings.connection import DBConnectionHandler
from sqlalchemy import func, or_
from sqlalchemy.exc import NoResultFound
from src.errors.http_erros import NotFoundException


class ParceiroRepository(ParceiroRepositoryInterface):
    def __init__(self, database=DBConnectionHandler):
        self.__database = database

    def insert_parceiro(
        self,
        *,
        nome: str,
        sobre_nome: str,
        empresa: str,
        e_empresa: bool,
        telefone: str,
    ) -> None:
        with self.__database() as database:
            try:
                new_registry = ParceiroEntity(
                    nome=nome,
                    sobre_nome=sobre_nome,
                    empresa=empresa,
                    e_empresa=e_empresa,
                    telefone=telefone,
                )
                database.session.add(new_registry)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def select_parceiro_by_id(self, parceiro_id: int) -> List[ParceiroModel]:
        with self.__database() as database:
            try:
                parceiro = (
                    database.session.query(ParceiroEntity)
                    .filter(ParceiroEntity.id == parceiro_id)
                    .one()
                )
                if parceiro:
                    return [
                        ParceiroModel(
                            parceiro_id=parceiro.id,
                            nome=parceiro.nome,
                            sobre_nome=parceiro.sobre_nome,
                            empresa=parceiro.empresa,
                            e_empresa=parceiro.e_empresa,
                            telefone=parceiro.telefone,
                        )
                    ]
                else:
                    return []
            except NoResultFound:
                raise NotFoundException()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def select_parceiro_by_nome(self, nome: str) -> List[ParceiroModel]:
        with self.__database() as database:
            try:
                parceiros = (
                    database.session.query(ParceiroEntity)
                    .filter(
                        or_(
                            func.concat(
                                ParceiroEntity.nome,
                                " ",
                                ParceiroEntity.sobre_nome,
                            ).contains(nome),
                            ParceiroEntity.nome.contains(nome),
                        )
                    )
                    .all()
                )
                return [
                    ParceiroModel(
                        parceiro_id=parceiro.id,
                        nome=parceiro.nome,
                        sobre_nome=parceiro.sobre_nome,
                        empresa=parceiro.empresa,
                        e_empresa=parceiro.e_empresa,
                        telefone=parceiro.telefone,
                    )
                    for parceiro in parceiros
                ]
            except Exception as exception:
                database.session.rollback()
                raise exception

    def select_all_parceiros(self) -> List[ParceiroModel]:
        with self.__database() as database:
            try:
                parceiros = database.session.query(ParceiroEntity).all()
                return [
                    ParceiroModel(
                        parceiro_id=parceiro.id,
                        nome=parceiro.nome,
                        sobre_nome=parceiro.sobre_nome,
                        empresa=parceiro.empresa,
                        e_empresa=parceiro.e_empresa,
                        telefone=parceiro.telefone,
                    )
                    for parceiro in parceiros
                ]
            except Exception as exception:
                database.session.rollback()
                raise exception

    def update_parceiro(self, data: dict) -> None:
        with self.__database() as database:
            try:
                parceiro = (
                    database.session.query(ParceiroEntity)
                    .filter(ParceiroEntity.id == data["id"])
                    .one()
                )
                if parceiro:
                    for key, value in data.items():
                        setattr(parceiro, key, value)
                    database.session.commit()
            except NoResultFound:
                raise NotFoundException()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def delete_parceiro(self, parceiro_id: int) -> None:
        with self.__database() as database:
            try:
                parceiro = (
                    database.session.query(ParceiroEntity)
                    .filter(ParceiroEntity.id == parceiro_id)
                    .first()
                )
                if parceiro:
                    database.session.delete(parceiro)
                    database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
