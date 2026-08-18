from __future__ import annotations

import os
import sqlite3
from typing import List
from uuid import uuid4

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

DATABASE_PATH = os.getenv("ECOMMERCE_DB", "ecommerce.db")

app = FastAPI(
    title="E-commerce Catalog API",
    version="1.0.0",
    description="API REST para gerenciamento do catálogo de produtos de um e-commerce.",
)


class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, description="Nome do produto")
    description: str = Field(..., min_length=1, description="Descrição do produto")
    price: float = Field(..., gt=0, description="Preço do produto")
    stock: int = Field(..., ge=0, description="Quantidade em estoque")


class ProductCreate(ProductBase):
    """Schema de entrada para criação de produtos."""


class ProductUpdate(ProductBase):
    """Schema de entrada para atualização de produtos."""


class Product(ProductBase):
    id: str = Field(..., description="Identificador único do produto")


def configure_database(path: str = DATABASE_PATH) -> None:
    global DATABASE_PATH
    DATABASE_PATH = path

    connection = sqlite3.connect(DATABASE_PATH)
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS products (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
        """
    )
    connection.commit()
    connection.close()


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


class ProductStore:
    """Persistência do catálogo em SQLite."""

    def create(self, payload: ProductCreate) -> Product:
        product_id = str(uuid4())
        with get_connection() as connection:
            connection.execute(
                "INSERT INTO products (id, name, description, price, stock) VALUES (?, ?, ?, ?, ?)",
                (product_id, payload.name, payload.description, payload.price, payload.stock),
            )
            connection.commit()

        return self.get(product_id)

    def list(self) -> List[Product]:
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT id, name, description, price, stock FROM products ORDER BY name"
            ).fetchall()

        return [Product.model_validate(dict(row)) for row in rows]

    def get(self, product_id: str) -> Product:
        with get_connection() as connection:
            row = connection.execute(
                "SELECT id, name, description, price, stock FROM products WHERE id = ?",
                (product_id,),
            ).fetchone()

        if row is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found",
            )

        return Product.model_validate(dict(row))

    def update(self, product_id: str, payload: ProductUpdate) -> Product:
        self.get(product_id)

        with get_connection() as connection:
            connection.execute(
                "UPDATE products SET name = ?, description = ?, price = ?, stock = ? WHERE id = ?",
                (payload.name, payload.description, payload.price, payload.stock, product_id),
            )
            connection.commit()

        return self.get(product_id)

    def delete(self, product_id: str) -> None:
        self.get(product_id)

        with get_connection() as connection:
            connection.execute("DELETE FROM products WHERE id = ?", (product_id,))
            connection.commit()


configure_database()
store = ProductStore()


@app.get("/health")
def health_check() -> dict:
    """Retorna o status da aplicação."""
    return {"status": "ok"}


@app.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(payload: ProductCreate) -> Product:
    """Cria um novo produto no catálogo."""
    return store.create(payload)


@app.get("/products", response_model=List[Product])
def list_products() -> List[Product]:
    """Lista todos os produtos cadastrados."""
    return store.list()


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: str) -> Product:
    """Consulta um produto específico pelo identificador."""
    return store.get(product_id)


@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: str, payload: ProductUpdate) -> Product:
    """Atualiza os dados de um produto existente."""
    return store.update(product_id, payload)


@app.delete("/products/{product_id}")
def delete_product(product_id: str) -> dict:
    """Remove um produto do catálogo."""
    store.delete(product_id)
    return {"message": "Product deleted successfully"}
