import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from csv_api_sender.agents import CoordinatorAgent


def main() -> None:
    parser = argparse.ArgumentParser(description="Processa um CSV usando arquitetura de agentes.")
    parser.add_argument("file_path", help="Caminho do arquivo CSV")
    parser.add_argument("--output-dir", default="artifacts", help="Diretório para salvar o relatório")
    args = parser.parse_args()

    result = CoordinatorAgent().run(args.file_path, args.output_dir)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
