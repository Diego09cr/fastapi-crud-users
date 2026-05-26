from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class UsuarioNovo(BaseModel):
    nome: str
    email: str

filmes = [
    {"id": 1, "titulo": "O Hobbit", "ano": 2012},
    {"id": 2, "titulo": "A Revolução dos Bichos", "ano": 1999},
]

usuarios = [
    {"id": 1, "nome": "Diego", "email": "diego@email.com"},
    {"id": 2, "nome": "Ana", "email": "ana@email.com"},
    {"id": 3, "nome": "Carlos", "email": "carlos@email.com"},
]

@app.get("/saudacao/{nome}")
def saudacao(nome):
    return {"mensagem": f"Olá, {nome}!"}

@app.get("/filmes")
def listar_filmes():
    return filmes

@app.get("/filmes/{id}")
def buscar_por_id(id):
    for filme in filmes:
        if filme["id"] == int(id):
            return filme
    raise HTTPException(status_code=404, detail="Filme não encontrado")
        
@app.get("/usuarios")
def allusu():
    return usuarios

@app.get("/usuarios/{id}")
def buscar_id(id):
    for identi in usuarios:
        if identi["id"] ==  int(id):
            return identi
    raise HTTPException(status_code=404, detail="Usuário não encontrado")
        
@app.get("/usuarios/{id}/email")
def get_email(id):
    for identi in usuarios:
        if identi["id"] ==  int(id):
            return {"email": identi["email"]}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.post("/usuarios")
def cria_usu(usuario: UsuarioNovo):
    novo ={
        "id": len(usuarios) + 1,
        "nome": usuario.nome,
        "email": usuario.email
    }
    usuarios.append(novo)
    return novo

@app.put("/usuarios/{id}")
def att_user(id, usuario: UsuarioNovo):
    pessoa = buscar_id(id)
    pessoa["nome"] = usuario.nome
    pessoa["email"] = usuario.email
    return pessoa

@app.delete("/usuarios/{id}")
def tchau_user(id):
    pessoa = buscar_id(id)
    usuarios.remove(pessoa)
    return {"mensagem": "Usuário excluído com sucesso"}