# Agentes e regras do projeto

## Objetivo
Este projeto tem como foco demonstrar o uso de OpenSpec, Spec-Driven Development e documentação em camadas para um sistema de e-commerce simples.

## Regras gerais
- Mantenha o sistema enxuto e didático.
- Priorize comportamento observável e testes automatizados.
- Documente decisões técnicas em arquivos separados, evitando poluir o principal arquivo de contexto.
- Faça mudanças pequenas e verificáveis.

## O que fazer
- Criar e manter a API de catálogo de produtos.
- Documentar requisitos, design e tarefas com OpenSpec.
- Escrever testes para validar os comportamentos do sistema.
- Usar arquivos de documentação separados para casos de uso e decisões.

## O que não fazer
- Não adicionar autenticação ou autorização no primeiro ciclo, salvo quando explicitamente requisitado.
- Não misturar implementação com documentação de requisitos.
- Não criar arquitetura complexa sem necessidade para o laboratório.
- Não alterar comportamento que já foi validado sem atualizar os testes.

## Perguntas úteis antes de mudar
- O requisito altera o contrato externo da API?
- A mudança impacta comportamento visível do cliente ou do sistema?
- A funcionalidade deve ser persistente ou apenas demonstrativa?
- Precisa de novos testes antes da implementação?

## Documentação por caso de uso
- [docs/overview.md](docs/overview.md)
- [docs/crud-api.md](docs/crud-api.md)
- [docs/testing.md](docs/testing.md)
