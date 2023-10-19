from fastapi import FastAPI
import requests
#uvicorn parametros:app --reload
#http://127.0.0.1:8000/docs

app = FastAPI()

#http://127.0.0.1:8000/teste/1
@app.get("/teste/{id}")
def main(id: int): #se não for especificado : int, id será string
    return {'valor': id}

#exemplo
usuarios = [(1, 'João', 'senha123'), (2, 'Pedro', 'senha456')]

#http://127.0.0.1:8000/usuario/2
#[2,"Pedro","senha456"]
@app.get("/usuario/{id}")
def user(id: int):
    for i in usuarios:
        if i[0] == id:
            return i
        
    return "Usuário inexistente"