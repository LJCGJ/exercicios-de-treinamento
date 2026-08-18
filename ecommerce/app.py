from __future__ import annotations

from typing import Dict, List, Optional
from uuid import uuid4

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="E-commerce Catalog API", version="1.0.0")


class ProductBase(BaseModel):
    name: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    id: str


products: Dict[str, Product] = {}


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(payload: ProductCreate) -> Product:
    product_id = str(uuid4())
    product = Product(id=product_id, **payload.model_dump())
    products[product_id] = product
    return product


@app.get("/products", response_model=List[Product])
def list_products() -> List[Product]:
    return list(products.values())


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: str) -> Product:
    product = products.get(product_id)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product


@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: str, payload: ProductUpdate) -> Product:
    product = products.get(product_id)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    updated = Product(id=product_id, **payload.model_dump())
    products[product_id] = updated
    return updated


@app.delete("/products/{product_id}")
def delete_product(product_id: str) -> dict:
    if product_id not in products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    del products[product_id]
    return {"message": "Product deleted successfully"}
