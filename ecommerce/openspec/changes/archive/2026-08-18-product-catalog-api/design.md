## Context

A solução precisa entregar uma API RESTful para catalogar produtos de um e-commerce em um ambiente simples e didático. O projeto atual não possui uma estrutura de backend de catálogo, então a abordagem mais adequada é criar uma API leve em FastAPI com armazenamento em memória para atender ao objetivo de aula e permitir testes rápidos.

## Goals / Non-Goals

**Goals:**
- Expor endpoints para criação, leitura, atualização e remoção de produtos.
- Validar entradas obrigatórias e dados consistentes.
- Manter comportamento previsível para testes automatizados.
- Deixar a API pronta para evoluir com armazenamento persistente e integração com banco de dados.

**Non-Goals:**
- Não será implementado autenticação de usuários neste ciclo.
- Não será incluída gestão de estoque avançada, categorias ou pedidos.
- Não será implementado banco de dados relacional nesta fase.

## Decisions

### 1. Use FastAPI as the API layer
FastAPI é a melhor opção para este projeto porque já está presente nas dependências e oferece rotas HTTP, documentação automática e validação de payloads com facilidade.

**Alternatives considered:**
- Flask: funcional, mas menos integrado com validação de dados e documentação automática.
- Node.js/Express: possível, mas não se alinha ao stack atual do laboratório.

### 2. Persist data in memory for the initial implementation
Para manter o laboratório simples e focado em comportamento, os produtos serão armazenados em memória em uma estrutura de dicionário indexada por ID.

**Rationale:**
- Reduz complexidade da implementação.
- Permite validação do fluxo CRUD rapidamente.
- Mantém a proposta de aula objetiva e acessível.

**Alternatives considered:**
- Banco SQLite: mais realista, mas cria overhead sem necessidade em uma aula introdutória.
- Arquivo JSON: mais simples, mas menos prático para operações de atualização e remoção em APIs.

### 3. Keep a simple REST contract
Os endpoints seguirão convenções REST comuns para facilitar uso por frontend, testes e integração futura.

**Endpoints expected:**
- POST /products
- GET /products
- GET /products/{product_id}
- PUT /products/{product_id}
- DELETE /products/{product_id}

**Rationale:**
- Padronização clara para quem consome a API.
- Menos ambiguidades em testes e documentação.

### 4. Validate required fields on input
Os dados obrigatórios deverão ser validados antes da criação e da atualização para evitar inconsistências no catálogo.

**Rationale:**
- Evita criação de produtos incompletos.
- Mantém os requisitos de negócio explícitos.

## Risks / Trade-offs

- [State loss on restart] → Because the API stores data in memory, data disappears after a server restart. Mitigation: add persistent storage in a later phase.
- [No authentication] → This keeps the laboratory simple but prevents real-world admin authorization. Mitigation: add auth and RBAC in a follow-up change.
- [Limited validation scope] → The initial version validates core fields, but not product duplication rules or advanced pricing constraints. Mitigation: expand validation as requirements mature.

## Migration Plan

1. Implement the FastAPI app and product models.
2. Add CRUD endpoints with basic validation.
3. Add automated tests covering creation, list, retrieve, update and delete cases.
4. Validate API behavior with FastAPI test client.
5. If needed, evolve storage to SQLite or a database-backed solution in a later change.

## Open Questions

- Should product IDs be UUIDs or numeric sequential identifiers in the final production version?
- Should duplicate names be allowed or rejected by business rule?
- Should the API later support product categories and stock movement history?
