# Guia rápido de setup

## Pré-requisitos
- Python 3.11+
- PowerShell (Windows) ou bash (Linux/Mac)

## Instalação em 3 passos

### 1. Ambiente virtual
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Dependências
```powershell
python -m pip install -r requirements.txt
```

### 3. Executar a API
```powershell
python -m uvicorn ecommerce.app:app --reload
```

## Acessar
- Documentação Swagger: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health

## Executar testes
```powershell
python -m pytest -q ecommerce/tests/test_ecommerce_api.py
```

## Configuração de ambiente (opcional)
Crie um arquivo `.env` na raiz do projeto:

```powershell
ECOMMERCE_DB=ecommerce.db
ECOMMERCE_API_KEY=sua-chave-secreta
```

Consulte `.env.example` para mais detalhes.
