from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from enum import Enum

class NomeGrupo(str, Enum):
    operacoes = "Operações matemáticas simples enum"
    teste = "Teste Hello Word"
    
description = f"""
    API desenvolvida durante a aula 2, contendo endpoints de exemplo e soma
    
    - /teste: retorna uma mensagem de sucesso
    - /soma/numero1/numero2: recebe dois números e retorna a soma
"""

app = FastAPI(
    title="API da Aula 2",
    description=description,
    summary="API desenvolvida durante a aula de Construção de APIs para IA",
    version="0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Wagner Hélio da Silva Filho",
        "url": "http://github.com/wagnerhelio/",
        "email": "wagner.whsf@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

#Exemplo 1 : Teste de API
@app.get(
    path="/teste",
    summary="Retorna mensagem de teste", 
    description="Retorna uma mensagem de exemplo para testar e verificar se deu certo",
    tags=[NomeGrupo.teste]
    )
def hello_world():
    #return {"mensagem":"Hello Word"}
    return {"mensagem":"Mudei a mensagem"}

#Exemplo 2 : Operações Matematicas
@app.post(
    path="/v1/soma/{numero1}/{numero2}",
    summary="Soma dois números inteiros",
    description="Recebe dois números inteiros e retorna a soma",
    tags=[NomeGrupo.operacoes]
    )

def soma(numero1: int, numero2: int):
    total = numero1 + numero2
    #return {"resultado": total}
    return {"resultado": total, "warning": "Esta versão será descontinuada em breve utilize a mais recente"}

# Formato 3 : Recebendo os numeros no corpo da requsição
@app.post(
    path="/v2/soma",
    summary="Soma dois números inteiros v2",
    description="Recebe dois números inteiros e retorna a soma",
    tags=[NomeGrupo.operacoes]
    )

def soma_formato2(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total,"warning": "Esta versão será descontinuada em breve utilize a mais recente"}

# Formato 4 : Recebendo os numeros no corpo da requsição

class Numero(BaseModel):
        numero1: int
        numero2: int
        numero3: int = 0
class Resultado(BaseModel):
        resultado: int 
                
@app.post( 
    path="/v3/soma",
    response_model=Resultado,
    summary="Soma dois números inteiros v3",
    description="Recebe dois números inteiros e retorna a soma",
    tags=[NomeGrupo.operacoes]
    )

def soma_formato3(numero: Numero):
    total = numero.numero1 + numero.numero2 + numero.numero3
    return{"resultado": total,"warning": "Parabens, está utilizando a versão mais recente!"}