# E-commerce Catalog API

[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Pytest](https://img.shields.io/badge/Pytest-8.3.3-0A9EDC?logo=pytest&logoColor=white)](https://pytest.org/)
[![OpenSpec](https://img.shields.io/badge/OpenSpec-Spec%20Driven-6C63FF)](https://github.com/Fission-AI/OpenSpec)

API RESTful para gestão do catálogo de produtos de um e-commerce, com persistência em banco de dados, validação de payloads, autenticação por chave de API e documentação pronta para apresentação.

## Visão geral

Este projeto demonstra uma evolução realista de backend em Python, destacando:

- arquitetura em FastAPI
- persistência em SQLite
- regras de negócio para catálogo
- autenticação simples para operações sensíveis
- documentação organizada por contexto
- testes automatizados para validar o comportamento

## Objetivo do projeto

O objetivo principal é mostrar como um catálogo de produtos pode evoluir de uma solução didática para uma estrutura mais profissional, mantendo clareza de desenvolvimento e boa organização para GitHub e apresentação acadêmica.

## Arquitetura

```mermaid
flowchart LR
    Client[Cliente / Admin / Frontend] --> API[FastAPI]
    API --> Store[ProductStore]
    Store --> DB[(SQLite)]
    API --> Auth[Validar X-API-Key]
    API --> Tests[Testes pytest]
```

## Funcionalidades implementadas

- cadastro de produtos
- listagem de produtos
- consulta por identificador
- atualização de produto
- remoção de produto
- persistência em SQLite
- categoria do produto
- autenticação para operações de escrita e leitura sensíveis
- endpoints de health check e documentação Swagger

## Stack tecnológica

- Python 3.11+
- FastAPI
- Pydantic
- SQLite
- pytest
- OpenSpec

## Estrutura do projeto

```text
ecommerce/
├── app.py
├── __init__.py
├── agents.md
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── docs/
│   ├── overview.md
│   ├── architecture.md
│   ├── crud-api.md
│   ├── testing.md
│   └── api-examples.md
├── openspec/
│   ├── config.yaml
│   └── changes/
│       └── 2026-08-18-product-catalog-api/
├── tests/
│   └── test_ecommerce_api.py
└── e-commerce.db
```

## Como executar

1. Crie o ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

3. Inicie a API:

```powershell
python -m uvicorn ecommerce.app:app --host 127.0.0.1 --port 8000 --reload
```

4. Acesse a documentação interativa do Swagger:

```text
http://127.0.0.1:8000/docs
```

## Endpoints principais

| Método | Endpoint | Descrição |
|---|---|---|
| GET | /health | Verifica o status da API |
| POST | /products | Cria um novo produto |
| GET | /products | Lista todos os produtos |
| GET | /products/{product_id} | Consulta um produto por ID |
| PUT | /products/{product_id} | Atualiza um produto |
| DELETE | /products/{product_id} | Remove um produto |

## Autenticação

As operações de acesso ao catálogo exigem o cabeçalho:

```http
X-API-Key: super-secret-key
```

A chave pode ser configurada com a variável de ambiente:

```powershell
$env:ECOMMERCE_API_KEY="sua-chave"
```

## Regras de negócio

- nome, descrição, categoria, preço e estoque são obrigatórios
- preço deve ser maior que zero
- estoque deve ser maior ou igual a zero
- produto inexistente deve retornar 404
- payload inválido deve retornar 422
- chave de API inválida ou ausente deve retornar 401

## Exemplos de payload

### Criar produto

```json
{
  "name": "Notebook Gamer",
  "description": "Notebook para jogos e produtividade",
  "category": "Eletrônicos",
  "price": 4999.9,
  "stock": 12
}
```

### Atualizar produto

```json
{
  "name": "Notebook Gamer Pro",
  "description": "Notebook com melhor desempenho",
  "category": "Eletrônicos",
  "price": 5499.9,
  "stock": 8
}
```

## Testes

Execute a suíte automatizada:

```powershell
python -m pytest -q ecommerce/tests/test_ecommerce_api.py
```

Resultado verificado:

```text
8 passed in 0.92s
```

## Workflow OpenSpec

O projeto foi estruturado com o fluxo de Spec-Driven Development:

1. proposta da mudança
2. especificação de requisitos
3. desenho técnico
4. checklist de implementação
5. aplicação da mudança
6. arquivamento do change

## Documentação complementar

- [docs/overview.md](docs/overview.md)
- [docs/architecture.md](docs/architecture.md)
- [docs/crud-api.md](docs/crud-api.md)
- [docs/testing.md](docs/testing.md)
- [docs/api-examples.md](docs/api-examples.md)
- [docs/roadmap.md](docs/roadmap.md)
- [agents.md](agents.md)

## Status do projeto

Status atual: funcional, validado por testes automatizados, pronto para demonstração acadêmica e apresentação em GitHub.

## Roadmap

- [x] persistência com banco de dados
- [x] autenticação por API key
- [x] categorias de produtos
- [ ] painel administrativo
- [ ] integração com frontend
- [ ] publicação em container e deploy

## Contribuição

Contribuições são bem-vindas. Para colaborar:

1. faça um fork do projeto
2. crie uma branch para sua feature
3. implemente e teste a mudança
4. abra um pull request com descrição clara

Consulte [CONTRIBUTING.md](CONTRIBUTING.md) para mais detalhes.

## Licença

Este projeto está disponível sob a licença MIT. Consulte [LICENSE](LICENSE).
