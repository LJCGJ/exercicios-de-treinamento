# Arquitetura do projeto

## Visão geral

A solução é um backend em FastAPI focado em gestão de catálogo de produtos com regras de negócio bem definidas e persistência em banco de dados.

## Componentes principais

- `app.py`: aplicação principal com rotas, modelos e lógica do catálogo
- `agents.md`: contexto das boas práticas de IA e documentação do projeto
- `docs/`: documentação por tema para manter o projeto organizado
- `openspec/`: proposta, especificação e histórico de desenvolvimento
- `tests/`: testes automatizados da API

## Fluxo de funcionamento

1. o cliente envia uma requisição HTTP para um endpoint
2. o FastAPI valida o payload e a autenticação por cabeçalho
3. a camada de persistência acessa o banco SQLite
4. a resposta é retornada em JSON padronizado
5. a suíte de testes valida o comportamento esperado

## Estrutura técnica

- `ProductBase`: modelo base com nome, descrição, categoria, preço e estoque
- `ProductCreate`: criação de produtos
- `ProductUpdate`: atualização de produtos
- `ProductStore`: operações de CRUD em SQLite
- `validate_api_key`: dependência para verificar `X-API-Key`

## Evolução natural

Em um próximo ciclo, este projeto pode evoluir para:

- autenticação JWT
- painel administrativo
- filtros e buscas avançadas
- imagens, promoções e categorias hierárquicas
- integração com frontend e deploy em nuvem
