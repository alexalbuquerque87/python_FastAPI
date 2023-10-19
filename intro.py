#1. pip install fastapi
#2. pip install uvicorn ->caso utilize uvicorn

from fastapi import FastAPI
#para rodar o servidor:
#uvicorn nome_da_aplicação:variável --reload
#--reload recarrega o servidor automaticamente
#neste exemplo ficaria:
#uvicorn intro:app --reload

#variável app poderia ser qualquer outra, mas por padrão é app
app = FastAPI()

#http://127.0.0.1:8000/
@app.get("/")
def root():
    return{'mensagem': 'home'}

#http://127.0.0.1:8000/cadastro
@app.get("/cadastro")
def cadastro():
    return{'mensagem': 'cadastro'}

