from fastapi import FastAPI
from pydantic import BaseModel
#from typing import Optional

#uvicorn pydantic_1:app --reload
#http://127.0.0.1:8000/docs

app = FastAPI()

class Usuario(BaseModel):
    id: int
    nome: str #nome: Optional[str] - campo opcional
    senha: str

#http://127.0.0.1:8000/usuario
@app.post("/usuario")
#se não utilizasse pydantic esta função precisaria receber os 3 parâmetros do usuário
def main(usuario: Usuario):
    return usuario

#simulando banco de dados
lista = [
    Usuario(id=1, nome='João', senha='senha1'),
    Usuario(id=2, nome='Marcos', senha='senha2'),
    Usuario(id=3, nome='Pedro', senha='senha3'),
]

#http://127.0.0.1:8000/newUser
@app.post("/newUser")
def main(usuario: Usuario):
    lista.append(usuario)
    return "usuário cadastrado"

#http://127.0.0.1:8000/usuarioListar
@app.get('/usuarioListar')
def main():
    return lista