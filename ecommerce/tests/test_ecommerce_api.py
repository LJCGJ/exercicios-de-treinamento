import pytest
from fastapi.testclient import TestClient

from ecommerce.app import app, configure_database

ADMIN_API_KEY = "super-secret-key"


@pytest.fixture(autouse=True)
def reset_database(tmp_path):
    configure_database(str(tmp_path / "products.db"))
    yield


client = TestClient(app)


def auth_headers():
    return {"X-API-Key": ADMIN_API_KEY}


def test_create_product():
    response = client.post(
        "/products",
        json={
            "name": "Notebook Gamer",
            "description": "Notebook para jogos e produtividade",
            "category": "Eletrônicos",
            "price": 4999.90,
            "stock": 12,
        },
        headers=auth_headers(),
    )

    assert response.status_code == 201
    body = response.json()
    assert body["name"] == "Notebook Gamer"
    assert body["category"] == "Eletrônicos"
    assert body["price"] == 4999.90
    assert body["stock"] == 12
    assert "id" in body


def test_list_products():
    client.post(
        "/products",
        json={
            "name": "Mouse sem fio",
            "description": "Mouse ergonômico",
            "category": "Acessórios",
            "price": 129.99,
            "stock": 50,
        },
        headers=auth_headers(),
    )

    response = client.get("/products", headers=auth_headers())

    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, list)
    assert len(payload) >= 1


def test_get_product_by_id():
    created = client.post(
        "/products",
        json={
            "name": "Mouse sem fio",
            "description": "Mouse ergonômico",
            "category": "Acessórios",
            "price": 129.99,
            "stock": 50,
        },
        headers=auth_headers(),
    ).json()

    response = client.get(f"/products/{created['id']}", headers=auth_headers())

    assert response.status_code == 200
    assert response.json()["id"] == created["id"]


def test_update_product():
    created = client.post(
        "/products",
        json={
            "name": "Teclado mecânico",
            "description": "Teclado com switches azuis",
            "category": "Periféricos",
            "price": 399.00,
            "stock": 20,
        },
        headers=auth_headers(),
    ).json()

    response = client.put(
        f"/products/{created['id']}",
        json={
            "name": "Teclado mecânico RGB",
            "description": "Teclado com switches azuis e iluminação",
            "category": "Periféricos",
            "price": 449.00,
            "stock": 15,
        },
        headers=auth_headers(),
    )

    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "Teclado mecânico RGB"
    assert body["category"] == "Periféricos"
    assert body["price"] == 449.00
    assert body["stock"] == 15


def test_delete_product():
    created = client.post(
        "/products",
        json={
            "name": "Monitor 27",
            "description": "Monitor Full HD",
            "category": "Eletrônicos",
            "price": 899.00,
            "stock": 6,
        },
        headers=auth_headers(),
    ).json()

    response = client.delete(f"/products/{created['id']}", headers=auth_headers())

    assert response.status_code == 200
    assert response.json()["message"] == "Product deleted successfully"

    follow_up = client.get(f"/products/{created['id']}", headers=auth_headers())
    assert follow_up.status_code == 404


def test_get_missing_product_returns_404():
    response = client.get("/products/non-existent-id", headers=auth_headers())

    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"


def test_database_persists_across_requests():
    first = client.post(
        "/products",
        json={
            "name": "Câmera digital",
            "description": "Câmera para fotos e vídeos",
            "category": "Eletrônicos",
            "price": 2199.00,
            "stock": 4,
        },
        headers=auth_headers(),
    ).json()

    second = client.get(f"/products/{first['id']}", headers=auth_headers())

    assert second.status_code == 200
    assert second.json()["name"] == "Câmera digital"
    assert second.json()["category"] == "Eletrônicos"


def test_requires_api_key_for_mutations():
    response = client.post(
        "/products",
        json={
            "name": "Tablet",
            "description": "Tablet para trabalho",
            "category": "Eletrônicos",
            "price": 1999.00,
            "stock": 10,
        },
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid API key"
