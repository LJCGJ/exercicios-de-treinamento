## Why

O e-commerce precisa de um catálogo de produtos confiável para permitir que administradores cadastrem, consultem, atualizem e removam itens de forma consistente. Sem essa capacidade, a gestão do inventário fica manual e propensa a erros, o que impacta diretamente a operação e a experiência do cliente.

## What Changes

- Criar uma API RESTful para gerenciamento de produtos no catálogo.
- Permitir cadastro de novos produtos com validação de dados obrigatórios.
- Permitir consulta de produtos por identificação e listagem do catálogo.
- Permitir atualização parcial ou completa dos dados do produto.
- Permitir remoção segura de produtos do catálogo.
- Definir contratos de resposta consistentes para operações de sucesso e erro.
- Preparar a base para extensão futura com estoque, categorias e preços por loja.

## Capabilities

### New Capabilities
- `product-catalog`: gerenciamento completo do catálogo de produtos, incluindo criação, leitura, atualização e exclusão.

### Modified Capabilities
- Nenhuma. Esta mudança introduz uma nova capacidade de negócio e não altera uma capability existente.

## Impact

- Nova API REST em backend de e-commerce.
- Estrutura de dados de produtos e validações de domínio.
- Possível integração com frontend, painel administrativo e serviços de inventário.
- Requisitos de testes automatizados para endpoints e fluxo básico de cadastro e manutenção.
