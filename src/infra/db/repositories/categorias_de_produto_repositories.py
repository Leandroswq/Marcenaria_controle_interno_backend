from typing import List
from src.infra.db.entities.categoria_de_produto_entity import CategoriaDeProdutoEntity
from src.interfaces.categorias_de_produto_interfaces import (
    CategoriaDeProdutoRepositoryInterface,
)
from src.models.tables.categorias_de_produto_models import CategoriaDeProdutoModel
from src.infra.db.settings.connection import DBConnectionHandler
from sqlalchemy.exc import NoResultFound
from src.errors.http_erros import NotFoundException, ConflictError
from sqlalchemy.exc import IntegrityError


class CategoriaDeProdutoRepository(CategoriaDeProdutoRepositoryInterface):
    def __init__(self, database=DBConnectionHandler):
        self.__database = database

    def insert_categoria_de_produto(self, categoria: str) -> None:
        with self.__database() as database:
            try:
                new_registry = CategoriaDeProdutoEntity(categoria=categoria)
                database.session.add(new_registry)
                database.session.commit()
            except IntegrityError as exception:
                database.session.rollback()
                raise ConflictError(detail=str(exception.orig))
            except Exception as exception:
                database.session.rollback()
                raise exception

    def select_categoria_de_produto_by_id(
        self, categoria_id: int
    ) -> List[CategoriaDeProdutoModel]:
        with self.__database() as database:
            try:
                categoria = (
                    database.session.query(CategoriaDeProdutoEntity)
                    .filter(CategoriaDeProdutoEntity.id == categoria_id)
                    .one()
                )
                if categoria:
                    return [
                        CategoriaDeProdutoModel(
                            categoria_id=categoria.id,
                            categoria=categoria.categoria,
                        )
                    ]
                else:
                    return []
            except NoResultFound:
                raise NotFoundException()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def select_categoria_de_produto_by_nome(
        self, nome: str
    ) -> List[CategoriaDeProdutoModel]:
        with self.__database() as database:
            try:
                categorias = (
                    database.session.query(CategoriaDeProdutoEntity)
                    .filter(CategoriaDeProdutoEntity.categoria.contains(nome))
                    .all()
                )
                return [
                    CategoriaDeProdutoModel(
                        categoria_id=categoria.id,
                        categoria=categoria.categoria,
                    )
                    for categoria in categorias
                ]
            except Exception as exception:
                database.session.rollback()
                raise exception

    def select_all_categorias_de_produto(self) -> List[CategoriaDeProdutoModel]:
        with self.__database() as database:
            try:
                categorias = database.session.query(CategoriaDeProdutoEntity).all()
                return [
                    CategoriaDeProdutoModel(
                        categoria_id=categoria.id,
                        categoria=categoria.categoria,
                    )
                    for categoria in categorias
                ]
            except Exception as exception:
                database.session.rollback()
                raise exception

    def update_categoria_de_produto(self, categoria_id: int, categoria: str) -> None:
        with self.__database() as database:
            try:
                categoria_entity = (
                    database.session.query(CategoriaDeProdutoEntity)
                    .filter(CategoriaDeProdutoEntity.id == categoria_id)
                    .one()
                )
                if categoria_entity:
                    categoria_entity.categoria = categoria
                    database.session.commit()
                else:
                    raise NotFoundException()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def delete_categoria_de_produto(self, categoria_id: int) -> None:
        with self.__database() as database:
            try:
                categoria_entity = (
                    database.session.query(CategoriaDeProdutoEntity)
                    .filter(CategoriaDeProdutoEntity.id == categoria_id)
                    .first()
                )
                if categoria_entity:
                    database.session.delete(categoria_entity)
                    database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
