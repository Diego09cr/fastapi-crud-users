# API de Usuários e Filmes

API REST construída com FastAPI.

## Rotas
- GET /usuarios — lista todos os usuários
- GET /usuarios/{id} — busca usuário por id
- POST /usuarios — cria novo usuário
- GET /filmes — lista todos os filmes
- GET /filmes/{id} — busca filme por id

## Como rodar
pip install fastapi uvicorn
python -m uvicorn main:app --reload