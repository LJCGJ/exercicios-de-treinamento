# CRUD do catálogo de produtos

## Endpoints

- POST /products — cria um novo produto
- GET /products — lista os produtos
- GET /products/{product_id} — consulta um produto específico
- PUT /products/{product_id} — atualiza um produto
- DELETE /products/{product_id} — remove um produto

## Regras de negócio
- O nome, descrição, preço e quantidade em estoque são obrigatórios.
- O preço deve ser maior que zero.
- O estoque deve ser maior ou igual a zero.
- Produtos inexistentes devem resultar em 404.

## Respostas esperadas
- Criação bem-sucedida retorna 201.
- Atualização bem-sucedida retorna 200.
- Remoção bem-sucedida retorna 200 com mensagem de confirmação.
- Erros de validação retornam 422.
- Recurso inexistente retorna 404.
