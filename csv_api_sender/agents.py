from __future__ import annotations

import csv
from pathlib import Path
from typing import Any


class CSVAnalysisAgent:
    """Agente que lê um arquivo CSV e extrai informações úteis."""

    def analyze(self, file_path: str | Path) -> dict[str, Any]:
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

        with file_path.open("r", encoding="utf-8", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)
            columns = reader.fieldnames or []

        return {
            "filename": file_path.name,
            "columns": columns,
            "rows_count": len(rows),
            "preview": rows[:5],
        }


class DocumentationAgent:
    """Agente que gera um relatório em texto a partir da análise."""

    def generate_report(self, analysis: dict[str, Any], output_dir: str | Path = "artifacts") -> dict[str, Any]:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        report_path = output_dir / "resumo_csv.txt"
        summary_lines = [
            "Resumo do arquivo CSV",
            "====================",
            f"Arquivo: {analysis['filename']}",
            f"Colunas: {', '.join(analysis['columns']) if analysis['columns'] else 'Nenhuma'}",
            f"Linhas: {analysis['rows_count']}",
            "",
            "Prévia dos dados:",
        ]

        for row in analysis.get("preview", []):
            summary_lines.append(str(row))

        report_path.write_text("\n".join(summary_lines), encoding="utf-8")

        return {
            "path": str(report_path),
            "summary": "Relatório gerado com sucesso.",
        }


class CoordinatorAgent:
    """Agente orquestrador que conecta subagentes."""

    def __init__(self) -> None:
        self.analysis_agent = CSVAnalysisAgent()
        self.documentation_agent = DocumentationAgent()

    def run(self, file_path: str | Path, output_dir: str | Path = "artifacts") -> dict[str, Any]:
        analysis = self.analysis_agent.analyze(file_path)
        report = self.documentation_agent.generate_report(analysis, output_dir)

        return {
            "subagents": [
                {"agent": "CSVAnalysisAgent", "status": "ok"},
                {"agent": "DocumentationAgent", "status": "ok"},
            ],
            "analysis": analysis,
            "report": report,
            "response_text": (
                f"Arquivo {analysis['filename']} processado com sucesso. "
                f"Foram identificadas {len(analysis['columns'])} colunas e {analysis['rows_count']} linhas. "
                f"Relatório salvo em {report['path']}."
            ),
        }
