# Visão geral do projeto

## Objetivo
O projeto implementa um catálogo de produtos para um e-commerce com foco em operações REST, validação de regras de negócio e persistência real.

## Stack principal
- Python
- FastAPI
- Pydantic
- SQLite
- pytest

## Fluxo principal
1. O cliente envia uma requisição HTTP para a API.
2. A aplicação valida os campos e a autenticação.
3. O produto é armazenado em SQLite.
4. O cliente acessa os endpoints para consultar, alterar ou remover itens.

## Características atuais
- catálogo com categoria por produto
- autenticação por header `X-API-Key`
- persistência além da memória
- suporte a testes automatizados em ambiente realista

## Diferencial do projeto
O sistema foi estruturado para ser mais profissional do que um laboratório simples, mantendo boa organização e documentação para fins de apresentação e evolução futura.