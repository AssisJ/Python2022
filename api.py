from fastapi import  FastAPI
from typing import  List
from classes import ModelInput, ModelOutput, APIModelBackEnd

app = FastAPI(title="API for clasification day", version='1.0')

@app.post("/predict", response_model=List[ModelOutput])
async def predict_(Inputs: List[ModelInput]):
    '''Endpoint de predicion de la api'''
    #lista vacia para las respuestas
    response = []
    #iteracion por todas las entradas que brindamos
    for Input in Inputs:
        #llamamos a nuestra clase en el backend para predecir
        #ponemos Input.nombre_atributo
        Model = APIModelBackEnd(Input.IDENTIFICACION, Input.TIMECREATED,Input.HOUR, Input.ORIGIN, Input.PROGRAMA)
        response.append(Model.predict()[0])
        
    #Retornamos la lista con todas las predicciones hechas, si se hizo mas de una request de la api 
    return response