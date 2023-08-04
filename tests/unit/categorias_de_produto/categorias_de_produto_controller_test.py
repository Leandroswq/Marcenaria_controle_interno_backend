import pytest
from src.controllers.categorias_de_produto_controller import (
    CategoriaDeProdutoController,
)
from src.models.tables.categorias_de_produto_models import (
    CategoriaDeProdutoModelResponse,
)
from src.interfaces.categorias_de_produto_interfaces import (
    CategoriaDeProdutoServiceInterface,
)
from typing import List
from src.models.http.response_model import (
    Update_response_model,
    Delete_response_model,
    Insert_response_model,
)
from src.models.http.request_model import HttpRequestModel
from utilities.dict_utilities import compare_dicts
from tests.unit.categorias_de_produto.categorias_de_produto_mock import (
    generate_categorias_de_produto,
    generate_categorias_de_produto_without_id,
)


@pytest.fixture
def controller_service(mocker):
    mock_service = mocker.Mock(spec=CategoriaDeProdutoServiceInterface)
    categoria_de_produto_controller = CategoriaDeProdutoController(service=mock_service)
    return categoria_de_produto_controller, mock_service


def test_insert_categoria_de_produto(controller_service):
    categoria_de_produto_controller, mock_service = controller_service
    categoria_de_produto_data = generate_categorias_de_produto_without_id(1)[0]
    request = HttpRequestModel(body=categoria_de_produto_data)

    mock_service.insert_categoria_de_produto.return_value = None

    response = categoria_de_produto_controller.insert_categoria_de_produto(request)

    mock_service.insert_categoria_de_produto.assert_called_once_with(
        data=categoria_de_produto_data
    )

    assert isinstance(response, Insert_response_model)
    assert response.detail == "Inserido com sucesso"


def test_select_categoria_de_produto_by_id(controller_service):
    categoria_de_produto_controller, mock_service = controller_service
    categoria_id = 1
    request = HttpRequestModel(path_params=[categoria_id])

    mock_service.select_categoria_de_produto_by_id.return_value = (
        generate_categorias_de_produto(1)
    )

    response = categoria_de_produto_controller.select_categoria_de_produto_by_id(
        request
    )
    mock_service.select_categoria_de_produto_by_id.assert_called_once()

    assert isinstance(response, CategoriaDeProdutoModelResponse)
    assert response.detail == "Operação efetuada com sucesso"
    assert isinstance(response.data, List)
    assert len(response.data) == 1
    assert compare_dicts(
        response.data[0].__dict__,
        generate_categorias_de_produto(1)[0].__dict__,
    )


def test_select_categoria_de_produto_by_nome(controller_service):
    categoria_de_produto_controller, mock_service = controller_service
    nome = "Eletrônicos"
    request = HttpRequestModel(query_params={"nome": nome})

    mock_service.select_categoria_de_produto_by_nome.return_value = (
        generate_categorias_de_produto(1)
    )

    response = categoria_de_produto_controller.select_categoria_de_produto_by_nome(
        request
    )
    mock_service.select_categoria_de_produto_by_nome.assert_called_once_with(
        categoria=nome
    )

    assert isinstance(response, CategoriaDeProdutoModelResponse)
    assert response.detail == "Operação efetuada com sucesso"
    assert isinstance(response.data, List)
    assert len(response.data) == 1
    assert compare_dicts(
        response.data[0].__dict__,
        generate_categorias_de_produto(1)[0].__dict__,
    )


def test_select_all_categorias_de_produto(controller_service):
    categoria_de_produto_controller, mock_service = controller_service

    mock_service.select_all_categorias_de_produto.return_value = (
        generate_categorias_de_produto(2)
    )

    request = HttpRequestModel()
    response = categoria_de_produto_controller.select_all_categorias_de_produto(
        request=request
    )

    mock_service.select_all_categorias_de_produto.assert_called_once()

    assert isinstance(response, CategoriaDeProdutoModelResponse)
    assert response.detail == "Operação efetuada com sucesso"
    assert isinstance(response.data, List)
    assert len(response.data) == 2

    assert_data = generate_categorias_de_produto(2)
    for i, categoria_de_produto in enumerate(response.data):
        assert compare_dicts(response.data[i].__dict__, assert_data[i].__dict__)


def test_update_categoria_de_produto(controller_service):
    categoria_de_produto_controller, mock_service = controller_service
    categoria_id = 1
    categoria_de_produto_data = generate_categorias_de_produto_without_id(1)[0]

    request = HttpRequestModel(
        path_params=[categoria_id], body=categoria_de_produto_data
    )

    mock_service.update_categoria_de_produto.return_value = None

    response = categoria_de_produto_controller.update_categoria_de_produto(
        request=request
    )

    mock_service.update_categoria_de_produto.assert_called_once_with(
        categoria_id=categoria_id, data=categoria_de_produto_data
    )

    assert isinstance(response, Update_response_model)
    assert response.detail == "Atualizado com sucesso"


def test_delete_categoria_de_produto(controller_service):
    categoria_de_produto_controller, mock_service = controller_service
    categoria_id = 1
    request = HttpRequestModel(path_params=[categoria_id])

    mock_service.update_categoria_de_produto.return_value = None

    response = categoria_de_produto_controller.delete_categoria_de_produto(
        request=request
    )

    mock_service.delete_categoria_de_produto.assert_called_once_with(
        categoria_id=categoria_id
    )

    assert response is None
