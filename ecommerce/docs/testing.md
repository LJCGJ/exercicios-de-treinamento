# Testes da API

## Objetivo
Garantir que cada operação do catálogo funcione conforme a regra de negócio, incluindo autenticação e persistência.

## Cobertura atual
- criação de produto com dados válidos
- listagem de produtos em ordem consistente
- consulta por ID
- atualização de produto
- remoção de produto
- rejeição de requisições sem chave de API
- rejeição de chave inválida
- persistência em banco SQLite

## Estratégia
Usar o cliente de testes do FastAPI para simular requisições HTTP e verificar status, payload e comportamento em casos de sucesso e erro.

## Execução

```powershell
python -m pytest -q ecommerce/tests/test_ecommerce_api.py
```

## Observação
O projeto mantém uma suíte enxuta, mas suficiente para validar os principais comportamentos do sistema e servir como evidência de qualidade para apresentação acadêmica.