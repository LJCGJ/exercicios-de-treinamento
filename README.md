# Exercícios de IA e projetos de aula

Este repositório reúne exemplos práticos de desenvolvimento com IA, agentes e APIs, com foco em aprendizado e apresentação acadêmica.

## Visão geral

O projeto principal em desenvolvimento é a API de catálogo de e-commerce, localizada em [ecommerce](ecommerce), com FastAPI, SQLite, autenticação por API key, validação de payloads e testes automatizados.

Também há uma base inicial de exemplo de processamento de CSV e agentes em [csv_api_sender](csv_api_sender), que serviu como introdução didática ao tema de IA aplicada.

## Estrutura do repositório

```text
exercicios-aula-ia/
├── ecommerce/
│   ├── app.py
│   ├── README.md
│   ├── agents.md
│   ├── CONTRIBUTING.md
│   ├── LICENSE
│   ├── requirements.txt
│   ├── docs/
│   ├── openspec/
│   └── tests/
├── csv_api_sender/
│   ├── app.py
│   ├── agents.py
│   ├── agent_cli.py
│   └── __init__.py
├── agents/
├── skills/
├── docs/
├── tests/
├── README.md
├── requirements.txt
├── exemplo.csv
└── artifacts/
```

## Projeto principal

### E-commerce Catalog API

A API de catálogo foi construída para demonstrar uma solução mais profissional e realista, incluindo:

- CRUD completo de produtos
- persistência em SQLite
- categoria por produto
- autenticação por `X-API-Key`
- validação com Pydantic
- documentação Swagger automática
- testes automatizados com pytest
- padrão de projeto pronto para apresentação e portfólio

Documentação detalhada: [ecommerce/README.md](ecommerce/README.md)

## Como executar

### 1. Ambiente virtual

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Dependências

```powershell
python -m pip install -r requirements.txt
```

### 3. Executar a API do e-commerce

```powershell
python -m uvicorn ecommerce.app:app --host 127.0.0.1 --port 8000 --reload
```

### 4. Acessar a documentação

```text
http://127.0.0.1:8000/docs
```

## Testes

```powershell
python -m pytest -q ecommerce/tests/test_ecommerce_api.py
```

## Objetivo didático

Este repositório demonstra como um projeto pode evoluir de um exemplo simples de IA para uma solução com estrutura mais madura, documentação organizada e arquitetura alinhada ao uso real em produtos digitais.

## Status

A API do e-commerce está funcional, validada por testes e pronta para demonstração acadêmica e apresentação em GitHub.

## Links úteis

- [ecommerce/README.md](ecommerce/README.md)
- [ecommerce/docs/overview.md](ecommerce/docs/overview.md)
- [ecommerce/docs/architecture.md](ecommerce/docs/architecture.md)
- [ecommerce/docs/crud-api.md](ecommerce/docs/crud-api.md)
- [ecommerce/docs/testing.md](ecommerce/docs/testing.md)
- [ecommerce/agents.md](ecommerce/agents.md)
