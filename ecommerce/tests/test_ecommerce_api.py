import pytest
from fastapi.testclient import TestClient

from ecommerce.app import app, configure_database


@pytest.fixture(autouse=True)
def reset_database(tmp_path):
    configure_database(str(tmp_path / "products.db"))
    yield


client = TestClient(app)


def test_create_product():
    response = client.post(
        "/products",
        json={
            "name": "Notebook Gamer",
            "description": "Notebook para jogos e produtividade",
            "price": 4999.90,
            "stock": 12,
        },
    )

    assert response.status_code == 201
    body = response.json()
    assert body["name"] == "Notebook Gamer"
    assert body["price"] == 4999.90
    assert body["stock"] == 12
    assert "id" in body


def test_list_products():
    client.post(
        "/products",
        json={
            "name": "Mouse sem fio",
            "description": "Mouse ergonômico",
            "price": 129.99,
            "stock": 50,
        },
    )

    response = client.get("/products")

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
            "price": 129.99,
            "stock": 50,
        },
    ).json()

    response = client.get(f"/products/{created['id']}")

    assert response.status_code == 200
    assert response.json()["id"] == created["id"]


def test_update_product():
    created = client.post(
        "/products",
        json={
            "name": "Teclado mecânico",
            "description": "Teclado com switches azuis",
            "price": 399.00,
            "stock": 20,
        },
    ).json()

    response = client.put(
        f"/products/{created['id']}",
        json={
            "name": "Teclado mecânico RGB",
            "description": "Teclado com switches azuis e iluminação",
            "price": 449.00,
            "stock": 15,
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "Teclado mecânico RGB"
    assert body["price"] == 449.00
    assert body["stock"] == 15


def test_delete_product():
    created = client.post(
        "/products",
        json={
            "name": "Monitor 27",
            "description": "Monitor Full HD",
            "price": 899.00,
            "stock": 6,
        },
    ).json()

    response = client.delete(f"/products/{created['id']}")

    assert response.status_code == 200
    assert response.json()["message"] == "Product deleted successfully"

    follow_up = client.get(f"/products/{created['id']}")
    assert follow_up.status_code == 404


def test_get_missing_product_returns_404():
    response = client.get("/products/non-existent-id")

    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"


def test_database_persists_across_requests():
    first = client.post(
        "/products",
        json={
            "name": "Câmera digital",
            "description": "Câmera para fotos e vídeos",
            "price": 2199.00,
            "stock": 4,
        },
    ).json()

    second = client.get(f"/products/{first['id']}")

    assert second.status_code == 200
    assert second.json()["name"] == "Câmera digital"
