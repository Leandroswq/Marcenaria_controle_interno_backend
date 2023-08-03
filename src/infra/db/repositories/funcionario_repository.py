from typing import List
from src.infra.db.entities.funcionario_entity import FuncionarioEntity
from src.interfaces.funcionario_interfaces import FuncionarioRepositoryInterface
from src.models.tables.funcionario_models import FuncionarioModel
from src.infra.db.settings.connection import DBConnectionHandler
from sqlalchemy import func, or_


class FuncionarioRepository(FuncionarioRepositoryInterface):
    def __init__(self, database=DBConnectionHandler):
        self.__database = database

    def insert_funcionario(
        self,
        *,
        nome: str,
        sobre_nome: str,
        funcao: str,
        telefone: str,
    ) -> None:
        with self.__database() as database:
            try:
                new_registry = FuncionarioEntity(
                    nome=nome,
                    sobre_nome=sobre_nome,
                    funcao=funcao,
                    telefone=telefone,
                )
                database.session.add(new_registry)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def select_funcionario_by_id(self, funcionario_id: int) -> List[FuncionarioModel]:
        with self.__database() as database:
            try:
                funcionario = (
                    database.session.query(FuncionarioEntity)
                    .filter(FuncionarioEntity.id == funcionario_id)
                    .first()
                )
                if funcionario:
                    return [
                        FuncionarioModel(
                            funcionario_id=funcionario.id,
                            nome=funcionario.nome,
                            sobre_nome=funcionario.sobre_nome,
                            funcao=funcionario.funcao,
                            telefone=funcionario.telefone,
                        )
                    ]
                else:
                    return []
            except Exception as exception:
                database.session.rollback()
                raise exception

    def select_funcionario_by_nome(self, nome: str) -> List[FuncionarioModel]:
        with self.__database() as database:
            try:
                funcionarios = (
                    database.session.query(FuncionarioEntity)
                    .filter(
                        or_(
                            func.concat(
                                FuncionarioEntity.nome,
                                " ",
                                FuncionarioEntity.sobre_nome,
                            ).contains(nome),
                            FuncionarioEntity.nome.contains(nome),
                        )
                    )
                    .all()
                )
                return [
                    FuncionarioModel(
                        funcionario_id=funcionario.id,
                        nome=funcionario.nome,
                        sobre_nome=funcionario.sobre_nome,
                        funcao=funcionario.funcao,
                        telefone=funcionario.telefone,
                    )
                    for funcionario in funcionarios
                ]
            except Exception as exception:
                database.session.rollback()
                raise exception

    def select_all_funcionarios(self) -> List[FuncionarioModel]:
        with self.__database() as database:
            try:
                funcionarios = database.session.query(FuncionarioEntity).all()
                return [
                    FuncionarioModel(
                        funcionario_id=funcionario.id,
                        nome=funcionario.nome,
                        sobre_nome=funcionario.sobre_nome,
                        funcao=funcionario.funcao,
                        telefone=funcionario.telefone,
                    )
                    for funcionario in funcionarios
                ]
            except Exception as exception:
                database.session.rollback()
                raise exception

    def update_funcionario(self, data: dict) -> None:
        with self.__database() as database:
            try:
                funcionario = (
                    database.session.query(FuncionarioEntity)
                    .filter(FuncionarioEntity.id == data["id"])
                    .first()
                )
                if funcionario:
                    for key, value in data.items():
                        setattr(funcionario, key, value)
                    database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def delete_funcionario(self, funcionario_id: int) -> None:
        with self.__database() as database:
            try:
                funcionario = (
                    database.session.query(FuncionarioEntity)
                    .filter(FuncionarioEntity.id == funcionario_id)
                    .first()
                )
                if funcionario:
                    database.session.delete(funcionario)
                    database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
