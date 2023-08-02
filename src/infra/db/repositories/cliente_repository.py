from typing import List
from src.infra.db.entities.cliente_entity import ClienteEntity
from src.interfaces.cliente_interfaces import ClienteRepositoryInterface
from src.models.tables.cliente_models import ClienteModel
from src.infra.db.settings.connection import DBConnectionHandler


class ClienteRepository(ClienteRepositoryInterface):
    def __init__(self, database=DBConnectionHandler):
        self.__database = database

    def insert_cliente(
        self,
        *,
        nome: str,
        sobre_nome: str,
        telefone: str,
        empresa: str,
        e_empresa: bool,
    ) -> None:
        with self.__database() as database:
            try:
                new_registry = ClienteEntity(
                    nome=nome,
                    sobre_nome=sobre_nome,
                    telefone=telefone,
                    empresa=empresa,
                    e_empresa=e_empresa,
                )
                database.session.add(new_registry)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def select_cliente_by_id(self, cliente_id: int) -> List[ClienteModel]:
        with self.__database() as database:
            try:
                cliente = (
                    database.session.query(ClienteEntity)
                    .where(ClienteEntity.id == cliente_id)
                    .first()
                )
                if cliente:
                    return [
                        ClienteModel(
                            client_id=cliente.id,
                            nome=cliente.nome,
                            sobre_nome=cliente.sobre_nome,
                            telefone=cliente.telefone,
                            empresa=cliente.empresa,
                            e_empresa=cliente.e_empresa,
                        )
                    ]
                else:
                    return []
            except Exception as exception:
                database.session.rollback()
                raise exception

    def select_cliente_by_nome(self, nome: str) -> List[ClienteModel]:
        with self.__database() as database:
            try:
                clientes = (
                    database.session.query(ClienteEntity)
                    .where(ClienteEntity.nome == nome)
                    .all()
                )
                return [
                    ClienteModel(
                        client_id=cliente.id,
                        nome=cliente.nome,
                        sobre_nome=cliente.sobre_nome,
                        telefone=cliente.telefone,
                        empresa=cliente.empresa,
                        e_empresa=cliente.e_empresa,
                    )
                    for cliente in clientes
                ]
            except Exception as exception:
                database.session.rollback()
                raise exception

    def select_all_clientes(self) -> List[ClienteModel]:
        with self.__database() as database:
            try:
                clientes = database.session.query(ClienteEntity).all()
                return [
                    ClienteModel(
                        client_id=cliente.id,
                        nome=cliente.nome,
                        sobre_nome=cliente.sobre_nome,
                        telefone=cliente.telefone,
                        empresa=cliente.empresa,
                        e_empresa=cliente.e_empresa,
                    )
                    for cliente in clientes
                ]
            except Exception as exception:
                database.session.rollback()
                raise exception

    def update_cliente(self, data: dict) -> None:
        with self.__database() as database:
            try:
                cliente = (
                    database.session.query(ClienteEntity)
                    .where(ClienteEntity.id == data["id"])
                    .first()
                )
                if cliente:
                    for key, value in data.items():
                        setattr(cliente, key, value)
                    database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def delete_cliente(self, cliente_id: int) -> None:
        with self.__database() as database:
            try:
                cliente = (
                    database.session.query(ClienteEntity)
                    .where(ClienteEntity.id == cliente_id)
                    .first()
                )
                if cliente:
                    database.session.delete(cliente)
                    database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception