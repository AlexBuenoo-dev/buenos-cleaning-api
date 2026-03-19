# Buenos Cleaning API

API backend desenvolvida com FastAPI para gestão de produtos, estoque e vendas.

## Tecnologias

- Python
- FastAPI
- SQLAlchemy
- SQLite

## Funcionalidades

- CRUD completo de produtos
- Controle de estoque
- Sistema de vendas com validação de estoque
- Consulta de produtos por ID

## Como rodar o projeto

```bash
# clonar repositório
git clone https://github.com/AlexBuenoo-dev/buenos-cleaning-api.git

# entrar na pasta
cd buenos-cleaning-api

# criar ambiente virtual
python -m venv venv

# ativar ambiente
venv\Scripts\activate

# instalar dependências
pip install -r requirements.txt

# rodar servidor
uvicorn app.main:app --reload

## Acesse a API

http://127.0.0.1:8000

http://127.0.0.1:8000/docs

## Autor

Desenvolvido por Alex Bueno 