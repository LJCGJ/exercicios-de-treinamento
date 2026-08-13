# Progresso 05 - Apresentação final

## Objetivo
Preparar o material final para apresentação oral e visual da aula.

## Conteúdo principal
- Arquitetura de agentes com IA
- Skills como especialização de comportamento
- Subagentes organizando tarefas
- Processamento de CSV
- Geração de resumo em texto
- Documentação por Mermaid

## Estrutura da apresentação
1. Introdução do problema
2. Arquitetura proposta
3. Agentes e skills
4. Fluxo de execução
5. Resultado prático
6. Conclusão

## Pontos-chave para falar
- A solução foi pensada como prova de conceito didática.
- O agente orquestrador coordena as etapas.
- O agente de CSV analisa o conteúdo do arquivo.
- A skill define o comportamento certo para cada tarefa.
- A documentação em Mermaid facilita a explicação visual.
- O projeto foi validado com teste automatizado e execução real.

## Evidência final
- `python -m pytest -q` → `1 passed`
- `python csv_api_sender/agent_cli.py exemplo.csv --output-dir artifacts` → execução concluída com sucesso

## Observação final
Esse material foi organizado em arquivos separados para documentar o progresso da aula e facilitar a apresentação final ao professor.
