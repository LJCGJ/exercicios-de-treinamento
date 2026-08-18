# Exemplos de uso da API

## Criar produto

```bash
curl -X POST "http://127.0.0.1:8000/products" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Notebook Gamer",
    "description": "Notebook para jogos e produtividade",
    "price": 4999.9,
    "stock": 12
  }'
```

## Listar produtos

```bash
curl "http://127.0.0.1:8000/products"
```

## Consultar produto por ID

```bash
curl "http://127.0.0.1:8000/products/{product_id}"
```

## Atualizar produto

```bash
curl -X PUT "http://127.0.0.1:8000/products/{product_id}" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Notebook Gamer Pro",
    "description": "Notebook com melhor desempenho",
    "price": 5499.9,
    "stock": 8
  }'
```

## Excluir produto

```bash
curl -X DELETE "http://127.0.0.1:8000/products/{product_id}"
```
