from fastapi.testclient import TestClient
from fastapi import status
from src.app import app

client = TestClient(app)


# Testar a rota de inserção de cliente
def test_insert_cliente():
    data = {
        "nome": "John Doe",
        "telefone": "62999999999",
        "empresa": "ACME Inc.",
        "e_empresa": True,
    }
    response = client.post("/cliente/", json=data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"detail": "Inserido com sucesso"}


# Testar a rota de busca de todos os clientes
def test_select_all_clientes():
    response = client.get("/cliente")
    print(response.json(), "=====================")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json()["data"], list)


# Testar a rota que busca de cliente por nome
def test_select_cliente_by_nome():
    nome = "John Doe"
    response = client.get("cliente/nome/", params={"nome": nome})
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json()["data"], list)


# Testar a rota de busca de cliente por ID
def test_select_cliente_by_id():
    cliente_id = 1
    response = client.get(f"/cliente/{cliente_id}")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json()["data"], list)


# Testar a rota de atualização de dados do cliente
def test_update_cliente():
    cliente_id = 1
    data = {
        "nome": "John Doe",
        "telefone": "62888888888",
        "empresa": "ACME Inc.",
        "e_empresa": True,
    }
    response = client.put(f"cliente/{cliente_id}", json=data)
    print(response.json())
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"detail": "Atualizado com sucesso"}


# Testar a rota de exclusão de cliente
def test_delete_cliente():
    cliente_id = 5
    response = client.delete(f"cliente/{cliente_id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not response.text
