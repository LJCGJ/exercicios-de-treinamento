# CRUD do catálogo de produtos

## Endpoints

- POST /products — cria um novo produto
- GET /products — lista todos os produtos
- GET /products/{product_id} — consulta um produto específico
- PUT /products/{product_id} — atualiza um produto
- DELETE /products/{product_id} — remove um produto

## Autenticação

Todas as rotas de catálogo exigem o cabeçalho:

```http
X-API-Key: super-secret-key
```

Se a chave estiver ausente ou incorreta, a API retorna 401.

## Regras de negócio
- nome, descrição, categoria, preço e estoque são obrigatórios
- preço deve ser maior que zero
- estoque deve ser maior ou igual a zero
- categoria deve conter valor válido e não vazio
- produto inexistente deve resultar em 404
- payload inválido deve resultar em 422

## Respostas esperadas
- criação bem-sucedida retorna 201
- leitura bem-sucedida retorna 200
- atualização bem-sucedida retorna 200
- remoção bem-sucedida retorna 200 com mensagem de confirmação
- erros de validação retornam 422
- recurso inexistente retorna 404
- autenticação inválida retorna 401
