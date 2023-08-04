import pytest
from src.errors.http_erros import ValidationException
from src.services.categorias_de_produto_service import CategoriaDeProdutoService
from src.models.tables.categorias_de_produto_models import (
    CategoriaDeProdutoModel,
)
from utilities.dict_utilities import compare_dicts
from tests.unit.categorias_de_produto.categorias_de_produto_mock import (
    generate_categorias_de_produto,
    generate_categorias_de_produto_without_id,
)


@pytest.fixture
def service_repository(mocker):
    mock_repository = mocker.Mock()
    service = CategoriaDeProdutoService(repository=mock_repository)

    return service, mock_repository


def test_insert_categoria_de_produto(service_repository):
    (
        service,
        mock_repository,
    ) = service_repository
    categoria_de_produto_data = generate_categorias_de_produto_without_id(1)[0]

    assert service.insert_categoria_de_produto(data=categoria_de_produto_data) is None

    categoria_de_produto_data = generate_categorias_de_produto_without_id(1)[0]
    mock_repository.insert_categoria_de_produto.assert_called_once_with(
        categoria=categoria_de_produto_data.categoria,
    )


def test_insert_categoria_de_produto_invalid_data(
    service_repository,
):
    (
        service,
        mock_repository,
    ) = service_repository
    categoria_de_produto_data = generate_categorias_de_produto_without_id(1)[0]
    categoria_de_produto_data.categoria = ""
    with pytest.raises(ValidationException):
        service.insert_categoria_de_produto(data=categoria_de_produto_data)


def test_select_categoria_de_produto_by_id(service_repository):
    (
        service,
        mock_repository,
    ) = service_repository
    categoria_de_produto_id = 1

    mock_response = generate_categorias_de_produto(1)

    mock_repository.select_categoria_de_produto_by_id.return_value = mock_response

    categorias_de_produto = service.select_categoria_de_produto_by_id(
        categoria_id=categoria_de_produto_id
    )

    mock_repository.select_categoria_de_produto_by_id.assert_called_once_with(
        categoria_id=categoria_de_produto_id
    )

    assert isinstance(categorias_de_produto, list)
    assert all(
        isinstance(categoria, CategoriaDeProdutoModel)
        for categoria in categorias_de_produto
    )
    assert compare_dicts(
        categorias_de_produto[0].__dict__, generate_categorias_de_produto(1)[0].__dict__
    )


def test_select_categoria_de_produto_by_nome(service_repository):
    (
        service,
        mock_repository,
    ) = service_repository
    mock_repository.select_categoria_de_produto_by_nome.return_value = (
        generate_categorias_de_produto(2)
    )

    nome = "Eletrônicos"
    categorias_de_produto = service.select_categoria_de_produto_by_nome(categoria=nome)

    mock_repository.select_categoria_de_produto_by_nome.assert_called_once_with(
        nome=nome
    )

    assert isinstance(categorias_de_produto, list)
    assert all(
        isinstance(categoria, CategoriaDeProdutoModel)
        for categoria in categorias_de_produto
    )
    assert len(categorias_de_produto) == 2

    categorias_de_produto_response = generate_categorias_de_produto(2)

    for i, categoria in enumerate(categorias_de_produto):
        assert compare_dicts(
            categoria.__dict__, categorias_de_produto_response[i].__dict__
        )


def test_select_categoria_de_produto_by_nome_invalid_data(
    service_repository,
):
    (
        service,
        mock_repository,
    ) = service_repository
    with pytest.raises(ValidationException):
        service.select_categoria_de_produto_by_nome(categoria=5)


def test_select_all_categorias_de_produto(service_repository):
    (
        service,
        mock_repository,
    ) = service_repository

    mock_repository.select_all_categorias_de_produto.return_value = (
        generate_categorias_de_produto(2)
    )

    categorias_de_produto = service.select_all_categorias_de_produto()

    mock_repository.select_all_categorias_de_produto.assert_called_once()

    assert isinstance(categorias_de_produto, list)
    assert all(
        isinstance(categoria, CategoriaDeProdutoModel)
        for categoria in categorias_de_produto
    )
    assert len(categorias_de_produto) == 2

    categorias_de_produto_response = generate_categorias_de_produto(2)
    for i, categoria in enumerate(categorias_de_produto):
        assert compare_dicts(
            categoria.__dict__, categorias_de_produto_response[i].__dict__
        )


def test_update_categoria_de_produto(service_repository):
    (
        service,
        mock_repository,
    ) = service_repository
    categoria_de_produto_data = generate_categorias_de_produto_without_id(1)[0].__dict__
    categoria_de_produto_id = 1

    assert (
        service.update_categoria_de_produto(
            data=categoria_de_produto_data, categoria_id=categoria_de_produto_id
        )
        is None
    )

    mock_repository.update_categoria_de_produto.assert_called_once_with(
        categoria_id=categoria_de_produto_id,
        categoria=categoria_de_produto_data["categoria"],
    )

    data = generate_categorias_de_produto_without_id(1)[0].__dict__
    data["id"] = categoria_de_produto_id
    assert compare_dicts(categoria_de_produto_data, data)


def test_update_categoria_de_produto_invalid_data(
    service_repository,
):
    (
        service,
        mock_repository,
    ) = service_repository
    categoria_de_produto_data = generate_categorias_de_produto_without_id(1)[0]
    categoria_de_produto_data.categoria = ""
    with pytest.raises(ValidationException):
        service.update_categoria_de_produto(
            data=categoria_de_produto_data.__dict__, categoria_id=1
        )


def test_delete_categoria_de_produto(service_repository):
    (
        service,
        mock_repository,
    ) = service_repository
    categoria_de_produto_id = 1

    assert (
        service.delete_categoria_de_produto(categoria_id=categoria_de_produto_id)
        is None
    )

    mock_repository.delete_categoria_de_produto.assert_called_once()
