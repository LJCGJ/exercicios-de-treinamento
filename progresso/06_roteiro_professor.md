# Progresso 06 - Roteiro do professor

## Objetivo
Alinhar o projeto ao roteiro enviado pelo professor para garantir que o entregável siga os requisitos da aula.

## Roteiro do professor

### 1) Projeto console .NET
O professor pediu primeiro a criação de um projeto console em .NET que:
- lê um CSV;
- monta um payload;
- envia para um endpoint de outra API.

### 2) Agentes
Foi solicitado um agente de arquitetura para:
- analisar a base de código;
- identificar componentes chaves;
- sugerir melhorias de arquitetura;
- gerar diagramas visuais para explicar a estrutura.

### 3) Prompt file
Foi solicitado um prompt file com:
- uso do agente criado anteriormente;
- definição do modelo cloud opus 4.6;
- frontmatter completo;
- texto de uso: explorar o projeto e gerar arquitetura usando C4 model com Mermaid e ADRs.

### 4) Diagramas Mermaid
O professor pediu uma skill para documentação em Mermaid, com:
- invocação de subagent antes de gerar contexto;
- análise do projeto;
- criação dos diagramas com base no contexto.

### 5) Parâmetros user-invocable
Foi solicitado adicionar parâmetros:
- user-invocable: false
- disable-model-invocation: false

### 6) Plugin xUnit
Também foi mencionado o plugin:
- csharp-dotnet-development
- uso do slash command do plugin para criar testes xUnit para um método selecionado.

## Situação atual do projeto
### Concluído
- Projeto Python com API de upload de CSV.
- Arquitetura com agentes e subagentes.
- Skills e prompts.
- Documentação Mermaid.
- Exemplo de plugin .NET com xUnit.
- Registro de progresso em arquivos separados.

### Ainda pendente para alinhar ao roteiro do professor
- Projeto console .NET real que lê CSV e envia payload para API.
- Prompt file com frontmatter completo conforme instrução do professor.
- Possível criação de skill específica para Mermaid com subagent.
- Ajuste final de documentação para refletir o roteiro exato do professor.

## Observação
O trabalho atual já cobre grande parte dos conceitos que o professor pediu, mas a etapa principal que ainda falta é a implementação do console .NET enviando dados para API, para fechar exatamente o fluxo do roteiro.
