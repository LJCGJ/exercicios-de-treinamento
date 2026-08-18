# Visão geral do projeto

## Objetivo
O projeto implementa um catálogo de produtos para um e-commerce simples, com foco em uma API REST para operações essenciais de CRUD.

## Stack principal
- Python
- FastAPI
- Pydantic
- pytest

## Fluxo principal
1. O administrador envia dados do produto.
2. A API valida os campos obrigatórios.
3. O produto é armazenado em memória.
4. O cliente acessa os endpoints para consultar, alterar ou remover itens.

## Limites do laboratório
- Dados ficam em memória e são perdidos ao reiniciar a aplicação.
- Não há autenticação.
- O foco está em clareza e didática.
