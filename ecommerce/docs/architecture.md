# Arquitetura do projeto

## Visão geral

A solução é um backend simples em FastAPI focado em operações CRUD do catálogo de produtos.

## Componentes principais

- `app.py`: aplicação principal com rotas e lógica da API
- `agents.md`: regras e contexto para agentes e IA
- `docs/`: documentação separada por tema para progressive disclosure
- `openspec/`: especificações, proposta e histórico do workflow de desenvolvimento
- `tests/`: testes automatizados da API

## Fluxo de funcionamento

1. o cliente envia uma requisição HTTP para um endpoint da API
2. o FastAPI valida o payload usando Pydantic
3. a aplicação manipula o catálogo em memória
4. a resposta é retornada no formato JSON padrão
5. os testes validam o comportamento esperado

## Limitações da arquitetura atual

- os dados ficam em memória e são perdidos ao reiniciar o processo
- não há autenticação nem autorização
- não há persistência em banco de dados
- foco em didática e clareza ao invés de produção completa

## Evolução natural

Em um próximo ciclo, este projeto pode evoluir para:

- banco SQLite ou PostgreSQL
- autenticação JWT
- catálogo com categorias, imagens e promoções
- painel administrativo separado
- integração com frontend e testes E2E
