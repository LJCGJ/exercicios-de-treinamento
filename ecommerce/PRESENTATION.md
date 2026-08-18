# Roteiro de apresentação — E-commerce Catalog API

## Duração: 5-10 minutos

---

## Slide 1: Introdução
**"E-commerce Catalog API"**

> Um projeto de backend profissional desenvolvido com FastAPI, SQLite e boas práticas de engenharia.

**Objetivo:** Demonstrar como estruturar uma API realista de e-commerce com regras de negócio, autenticação e testes automatizados.

---

## Slide 2: Stack e Arquitetura

```
Cliente HTTP
    ↓
FastAPI (Rotas & Validação)
    ↓
SQLite (Persistência)
    ↓
Modelo de Produto
    ↓
Endpoints CRUD
```

**Tecnologias:**
- Python 3.11+ — linguagem base
- FastAPI — framework web
- SQLite — banco de dados local
- Pydantic — validação de dados
- pytest — testes automatizados

---

## Slide 3: O que foi implementado

✅ **CRUD completo** de produtos  
✅ **Persistência em SQLite** — dados permanecem após reiniciar  
✅ **Categoria por produto** — regra de negócio adicional  
✅ **Autenticação por API Key** — proteção para operações sensíveis  
✅ **Validação com Pydantic** — regras claras de negócio  
✅ **Testes automatizados** — 8 testes passando  
✅ **Documentação Swagger** — interativa e pronta para uso  

---

## Slide 4: Endpoints principais

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | /products | Cria novo produto |
| GET | /products | Lista todos os produtos |
| GET | /products/{id} | Consulta produto específico |
| PUT | /products/{id} | Atualiza produto |
| DELETE | /products/{id} | Remove produto |

**Autenticação:** Todos os endpoints exigem cabeçalho `X-API-Key`.

---

## Slide 5: Exemplo prático

### Criar um produto
```bash
curl -X POST http://127.0.0.1:8000/products \
  -H "X-API-Key: super-secret-key" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Notebook Gamer",
    "description": "Notebook para trabalho e jogos",
    "category": "Eletrônicos",
    "price": 4999.90,
    "stock": 5
  }'
```

**Resposta (201):**
```json
{
  "id": "uuid-aqui",
  "name": "Notebook Gamer",
  "description": "Notebook para trabalho e jogos",
  "category": "Eletrônicos",
  "price": 4999.9,
  "stock": 5
}
```

---

## Slide 6: Estrutura do projeto

```
ecommerce/
├── app.py                    # Aplicação principal
├── requirements.txt          # Dependências
├── README.md                 # Documentação
├── QUICK-START.md            # Guia rápido
├── .env.example              # Configuração de exemplo
├── docs/                     # Documentação organizada
├── tests/                    # Testes automatizados
├── openspec/                 # Histórico de desenvolvimento
└── .gitignore                # Arquivos ignorados no git
```

**Destaque:** Documentação separada por contexto mantém o projeto organizado.

---

## Slide 7: Testes automatizados

```powershell
python -m pytest -q ecommerce/tests/test_ecommerce_api.py
```

**Resultado:**
```
8 passed in 0.92s
```

**O que é testado:**
- CRUD de produtos
- Persistência em SQLite
- Autenticação e autorização
- Validação de payloads
- Categorias

---

## Slide 8: Diferencial do projeto

🎯 **Realista:** Usa SQLite ao invés de memória  
🔐 **Seguro:** Autentica operações com API key  
📚 **Bem documentado:** Swagger + markdown  
🧪 **Testado:** Suite automatizada com cobertura  
🏗️ **Profissional:** Estrutura pronta para GitHub e produção  
🎓 **Didático:** Código claro e comentado  

---

## Slide 9: Próximas evoluções

- [ ] Autenticação JWT
- [ ] Filtros e busca avançada
- [ ] Imagens e thumbnails
- [ ] Promoções e descontos
- [ ] Painel administrativo
- [ ] Deploy em nuvem (AWS, Azure, etc)

---

## Slide 10: Conclusão

**"Este projeto demonstra como estruturar um backend de e-commerce de forma profissional e realista, mantendo o código limpo, bem testado e pronto para apresentação e evolução."**

---

## Roteiro de fala

1. **Apresentação (30s):** Explique o que é o projeto e por que foi criado.
2. **Stack (1min):** Mostre o diagrama de arquitetura.
3. **Funcionalidades (1min):** Liste o que foi implementado.
4. **Exemplo prático (2min):** Faça uma requisição ao vivo usando o Swagger.
5. **Testes (1min):** Execute a suíte de testes.
6. **Estrutura (1min):** Mostre como o projeto está organizado.
7. **Diferencial (1min):** Destaque o que torna este projeto especial.
8. **Perguntas (1min):** Abra espaço para dúvidas.

---

## Dicas para apresentar ao vivo

- Inicie a API antes da apresentação: `python -m uvicorn ecommerce.app:app --reload`
- Abra o Swagger em http://127.0.0.1:8000/docs
- Crie um produto e mostre a resposta
- Execute os testes: `python -m pytest -q ecommerce/tests/test_ecommerce_api.py`
- Mostre o banco SQLite: `sqlite3 ecommerce.db ".tables"`
