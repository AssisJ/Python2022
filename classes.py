from pydantic import BaseModel as PydanticBaseModel
from pydantic import Field, ValidationError
from typing import Literal
import joblib
import pandas as pd
import datetime as dt
import os
import numpy as np
from fastapi import HTTPException

class ModelInput(PydanticBaseModel):
    '''
    Clase que define las entradas del modelo
    '''
        
    IDENTIFICACION: int = Field(description = 'Identificacion de la persona', ge = 1000000 , le= 1000000000)    
    TIMECREATED: int = Field(description = 'Altura de la persona', ge = 10000000000 , le= 10000000000)
    HOUR: int = Field(description = "Hora de acceso promedio", ge=0 , le=23)
    ORIGIN: Literal["web","cli"]
    PROGRAMA: Literal['INGENIERÍA AMBIENTAL', 'LICENCIATURA EN EDUCACIÓN INFANTIL',
       'INGENIERÍA MECÁNICA', 'QUÍMICA', 'ADMINISTRACIÓN EN SALUD','ACUICULTURA', 'DPTO DE INGENIERÍA AMBIENTAL',
       'LIC EN LITERATURA Y LENGUA CASTELLANA', 'INGENIERÍA DE ALIMENTOS','MEDICINA VETERINARIA Y ZOOTECNIA', 'INGENIERÍA DE SISTEMAS',
       'DEPARTAMENTO DE INGENIERIA DE ALIMENTOS', 'MATEMÁTICAS','DEPARTAMENTO DE QUÍMICA',
        'ADMINIS. EN FINANZAS Y NEGOCIOS INTERNAC','FÍSICA', 'GEOGRAFÍA',
       'INGENIERÍA INDUSTRIAL', 'DPTO CIENCIAS ADMINISTRATIVAS',
       'INGENIERÍA AGRONÓMICA', 'DEPARTAMENTO DE CIENCIAS PECUARÍAS',
       'DEPARTAMENTO DE GEOGRAFÍA Y MEDIO AMBIEN',
       'LIC EN LENGUAS EXTRAN CON ENFA EN INGLES',
       'DEPARTAMENTO DE IDIOMAS EXTRANJEROS',
       'DEPARTAMENTO DE INFORMÁTICA EDUCATIVA',
       'LICENCIATURA EN EDUCACION INFANTIL', 'ENFERMERÍA',
       'DPTO DE ING DE SISTEMAS Y TELECOMUNICACI', 'DERECHO',
       'LICENCIATURA EN INFORMATICA','TECNOLOGÍA EN REGENCIA DE FARMACIA',
       'DEPARTAMENTO DE MATEMÁTICAS Y ESTADÍSTIC',
       'LIC. EDUCACIÓN FÍSICA RECREACIÓN Y DEPOR', 'ESTADÍSTICA',
       'LIC EN CIENCIAS NATURALES Y EDU AMBIENTA', 'BACTERIOLOGÍA',
       'CINTIA', 'DEPARTAMENTO DE SALUD PÚBLICA', 'BIOLOGÍA',
       'DEPARTAMENTO DE BIOLOGÍA', 'DIPLOMADO ETHICAL HACKING',
       'DEPARTAMENTO DE REGENCÍA Y FARMACIA',
       'DEPARTAMENTO DE INGENIERÍA MECÁNICA', 'LIC EN CIENCIAS SOCIALES',
       'LIC EN INFORMÁTICA', 'DEPARTAMENTO DE PSICOPEDAGOGÍA',
       'BACTERIOLOGIA', 'LIC EN EDUC BÁSICA CON ENF HUM LENG CAST',
       'LIC EN EDUCACION ARTISTICA',
       'LICENCIATURA EN INFORMÁTICA Y MEDIOS AUD',
       'DPTO DE ING AGRONÓMICA Y DESARROLL RURAL',
       'DPTO INGENIERÍA INDUSTRIAL', 'ING SISTEMAS',
       'DEPARTAMENTO DE FÍSICA Y ELECTRÓNICA',
       'DEPARTAMENTO DE CIENCIAS JURÍDICAS',
       'DEPARTAMENTO DE INGENIERÍA INDUSTRIAL',
       'DEPARTAMENTO DE ENFERMERÍA', 'DEPARTAMENTO DE BACTERIOLOGÍA',
       'DPTO DE ING. AMBIENTAL', 'DPTO DE CIENCIAS NATURALES',
       'LIC EN EDUC BÁSICA CON ENF EN HUMAN INGL',
       'ADMINISTRACIÓN EN FINANZAS Y NEGOCIOS INTERNACIONALES',
       'DPTO DE CULTURA FÍSICA, RECREAC Y DEPORT', 'ENFERMERIA',
       'DEPARTAMENTO DE ARTES', 'FUNCIONARIOS TEMPORALES',
       'DEPARTAMENTO DE CIENCIAS ACUÍCOLAS',
       'DEPARTAMENTO DE ESPAÑOL Y LITERATURA', 'DPTO PSICOPEDAGOGÍA',
       'REGENCIA DE FARMACIA', 'REGENCIA Y FARMACIA', 'QUIMICA',
       'DEPARTAMENTO DE MATEMATICAS Y ESTADISTICAS',
       'DEPARTAMENTO DE INFORMATICA',
       'DEPARTAMENTO DE MATEMÁTICAS Y ESTADÍS',
       'DEPARTAMENTO DE CIENCIAS SOCIALES', 'CIENCIAS',
       'LICENCIATURA EN EDUCACIÓN INFANTIL ', 'DPTO DE BIOLOGÍA',
       'INGENIERÍA AGRONOMICA', 'LIC. EN INFORMÁTICA ',
       'MEDICINA VETERINARIA', 'LIC. EN INFORMATICA',
       'LICENCIATURA EN INGLES',
       'DPTO DE ING DE SISTEMAS Y TELECOMUNICACIONES', 'ESTADÍ\xadSTICA',
       'LIC. EN INFORMATICA Y MEDIOS AUDIOVISUALES',
       'INGENIERIA AGRONOMICA', 'DPTO BACTEROLOGÍA',
       'INGENIERIA AMBIENTAL',
       'ADMINIS. EN FINANZAS Y NEGOCIOS INTERNACIONALES',
       'ADMON FINANZAS Y NEGOCIOS INTERNACIONALES',
       'TEC PROF EN MANEJO Y CONSERV DE PROD AGR', 'ACUICULURA',
       'BIOLOGIA', 'DPTO DE CULTURA FÍSICA, RECREAC Y DEPORTES', 'FISICA',
       'LIC EN EDUC BÁSICA CON ENF EN CIEN SOCIA',
       'LIC EN CIENCIAS NATURALES Y EDU AMBIENTAL',
       'ADMINISTRACION EN SALUD',
       'OFICINA DE BIBLIOTECAS Y RECURSOS EDUCATIVOS',
       'IDIOMAS EXTRANJEROS CON ENFASIS EN INGLES', 'LIC. EN INFORMÁTICA',
       'PRUEBAS', 'INGENIERÍA DE ALIMENTO', 'QUÍ\xadMICA',
       'INGENIERÍA AGRONOMICA ', 'CIENCIAS ADMINISTRATIVAS',
       'DIVISION DE BIBLIOTECAS Y RECURSOS EDUCATIVOS BIBLIOTECA CENTRAL "MISAEL DIAZ URZOLA"',
       'QUIMICA ', 'DECANATURA/GESTOR DE CALIDAD',
       'DPTO MEDICINA VETERINARIA Y ZOOTECNIA',
       'DPTO INGENIERÍA AMBIENTAL', 'GEOGRAFIA', 'INGENIERÍA AGRONOMIA',
       'LIC. EDUCACIÓN BÁSICA ÉNFASIS ARTÍSTICA', 'VETERINARIA',
       'ADMINISTRACIÓN EN FINANZAS Y NEGOCIOS INTERNACIONALES ',
       'DIVISION DE POSTGRADOS Y EDUCACION CONTINUADA',
       'FUNCIONARIOS ADM. PLANTA', 'INGENIERIA AMBIENTAL ',
       'DEPARTAMENTO DE INGENIERIA AMBIENTAL',
       'DPTO DE GEOGRAFIA Y MEDIO AMBIENTE', 'ING AMBIENTAL']
    
    
    class Config:
        schema_extra = {
            "Example": {
                'IDENTIFICACION':50521243 ,
                'TIMECREATED': 1659331482,
                'HOUR':12,
                'ORIGIN': "web",
                'PROGRAMA':'ING AMBIENTAL'
            }
        }
class ModelOutput(PydanticBaseModel):
    '''
    Clase que define la salida del modelo
    '''
    
    DAY: Literal['LUNES','MARTES','MIERCOLES','JUEVES','VIERNES','SABADO','DOMINGO']
    
    class Config:
        schema_extra = {
            "Example": {
                'DAY': 'MARTES'
            }
        }
        
class APIModelBackEnd():
    '''
    Esta clase maneja el back end de nuestro modelo de Machine Learning para la API en FastAPI
    '''
    
    def __init__(self,IDENTIFICACION,TIMECREATED,HOUR,ORIGIN,PROGRAMA):
        
        '''
        Este método se usa al instanciar las clases

        Aquí, hacemos que pida los mismos parámetros que tenemos en ModelInput.

        Para más información del __init__ method, pueden leer en línea en sitios cómo 

        https://www.udacity.com/blog/2021/11/__init__-in-python-an-overview.html

        '''
        
        
        self.IDENTIFICACION = IDENTIFICACION
        self.TIMECREATED = TIMECREATED
        self.HOUR = HOUR
        self.ORIGIN = ORIGIN
        self.PROGRAMA = PROGRAMA
        
    def _load_model(self, model_name:str = "ModelRF.pkl"):
            self.model = joblib.load(model_name)
        
    def _prepare_data(self):
            '''
            Clase de preparar lo datos.
            Este método convierte las entradas en los datos que tenían en X_train y X_test.

            Miren el orden de las columnas de los datos antes de su modelo.
            Tienen que recrear ese orden, en un dataframe de una fila.

            '''
            col=[
                "IDENTIFICACION",
                "TIMECREATED",
                "HOUR",
                'ORIGIN_cli',
                 'ORIGIN_web',
                 'PROGRAMA_ACUICULTURA',
                 'PROGRAMA_ACUICULURA',
                 'PROGRAMA_ADMINIS. EN FINANZAS Y NEGOCIOS INTERNAC',
                 'PROGRAMA_ADMINIS. EN FINANZAS Y NEGOCIOS INTERNACIONALES',
                 'PROGRAMA_ADMINISTRACION EN SALUD',
                 'PROGRAMA_ADMINISTRACIÓN EN FINANZAS Y NEGOCIOS INTERNACIONALES',
                 'PROGRAMA_ADMINISTRACIÓN EN FINANZAS Y NEGOCIOS INTERNACIONALES ',
                 'PROGRAMA_ADMINISTRACIÓN EN SALUD',
                 'PROGRAMA_ADMON FINANZAS Y NEGOCIOS INTERNACIONALES',
                 'PROGRAMA_BACTERIOLOGIA',
                 'PROGRAMA_BACTERIOLOGÍA',
                 'PROGRAMA_BIOLOGIA',
                 'PROGRAMA_BIOLOGÍA',
                 'PROGRAMA_CIENCIAS',
                 'PROGRAMA_CIENCIAS ADMINISTRATIVAS',
                 'PROGRAMA_CINTIA',
                 'PROGRAMA_DECANATURA/GESTOR DE CALIDAD',
                 'PROGRAMA_DEPARTAMENTO DE ARTES',
                 'PROGRAMA_DEPARTAMENTO DE BACTERIOLOGÍA',
                 'PROGRAMA_DEPARTAMENTO DE BIOLOGÍA',
                 'PROGRAMA_DEPARTAMENTO DE CIENCIAS ACUÍCOLAS',
                 'PROGRAMA_DEPARTAMENTO DE CIENCIAS JURÍDICAS',
                 'PROGRAMA_DEPARTAMENTO DE CIENCIAS PECUARÍAS',
                 'PROGRAMA_DEPARTAMENTO DE CIENCIAS SOCIALES',
                 'PROGRAMA_DEPARTAMENTO DE ENFERMERÍA',
                 'PROGRAMA_DEPARTAMENTO DE ESPAÑOL Y LITERATURA',
                 'PROGRAMA_DEPARTAMENTO DE FÍSICA Y ELECTRÓNICA',
                 'PROGRAMA_DEPARTAMENTO DE GEOGRAFÍA Y MEDIO AMBIEN',
                 'PROGRAMA_DEPARTAMENTO DE IDIOMAS EXTRANJEROS',
                 'PROGRAMA_DEPARTAMENTO DE INFORMATICA',
                 'PROGRAMA_DEPARTAMENTO DE INFORMÁTICA EDUCATIVA',
                 'PROGRAMA_DEPARTAMENTO DE INGENIERIA AMBIENTAL',
                 'PROGRAMA_DEPARTAMENTO DE INGENIERIA DE ALIMENTOS',
                 'PROGRAMA_DEPARTAMENTO DE INGENIERÍA INDUSTRIAL',
                 'PROGRAMA_DEPARTAMENTO DE INGENIERÍA MECÁNICA',
                 'PROGRAMA_DEPARTAMENTO DE MATEMATICAS Y ESTADISTICAS',
                 'PROGRAMA_DEPARTAMENTO DE MATEMÁTICAS Y ESTADÍS',
                 'PROGRAMA_DEPARTAMENTO DE MATEMÁTICAS Y ESTADÍSTIC',
                 'PROGRAMA_DEPARTAMENTO DE PSICOPEDAGOGÍA',
                 'PROGRAMA_DEPARTAMENTO DE QUÍMICA',
                 'PROGRAMA_DEPARTAMENTO DE REGENCÍA Y FARMACIA',
                 'PROGRAMA_DEPARTAMENTO DE SALUD PÚBLICA',
                 'PROGRAMA_DERECHO',
                 'PROGRAMA_DIPLOMADO ETHICAL HACKING',
                 'PROGRAMA_DIVISION DE BIBLIOTECAS Y RECURSOS EDUCATIVOS BIBLIOTECA CENTRAL "MISAEL DIAZ URZOLA"',
                 'PROGRAMA_DIVISION DE POSTGRADOS Y EDUCACION CONTINUADA',
                 'PROGRAMA_DPTO BACTEROLOGÍA',
                 'PROGRAMA_DPTO CIENCIAS ADMINISTRATIVAS',
                 'PROGRAMA_DPTO DE BIOLOGÍA',
                 'PROGRAMA_DPTO DE CIENCIAS NATURALES',
                 'PROGRAMA_DPTO DE CULTURA FÍSICA, RECREAC Y DEPORT',
                 'PROGRAMA_DPTO DE CULTURA FÍSICA, RECREAC Y DEPORTES',
                 'PROGRAMA_DPTO DE GEOGRAFIA Y MEDIO AMBIENTE',
                 'PROGRAMA_DPTO DE ING AGRONÓMICA Y DESARROLL RURAL',
                 'PROGRAMA_DPTO DE ING DE SISTEMAS Y TELECOMUNICACI',
                 'PROGRAMA_DPTO DE ING DE SISTEMAS Y TELECOMUNICACIONES',
                 'PROGRAMA_DPTO DE ING. AMBIENTAL',
                 'PROGRAMA_DPTO DE INGENIERÍA AMBIENTAL',
                 'PROGRAMA_DPTO INGENIERÍA AMBIENTAL',
                 'PROGRAMA_DPTO INGENIERÍA INDUSTRIAL',
                 'PROGRAMA_DPTO MEDICINA VETERINARIA Y ZOOTECNIA',
                 'PROGRAMA_DPTO PSICOPEDAGOGÍA',
                 'PROGRAMA_ENFERMERIA',
                 'PROGRAMA_ENFERMERÍA',
                 'PROGRAMA_ESTADÍSTICA',
                 'PROGRAMA_ESTADÍ\xadSTICA',
                 'PROGRAMA_FISICA',
                 'PROGRAMA_FUNCIONARIOS ADM. PLANTA',
                 'PROGRAMA_FUNCIONARIOS TEMPORALES',
                 'PROGRAMA_FÍSICA',
                 'PROGRAMA_GEOGRAFIA',
                 'PROGRAMA_GEOGRAFÍA',
                 'PROGRAMA_IDIOMAS EXTRANJEROS CON ENFASIS EN INGLES',
                 'PROGRAMA_ING AMBIENTAL',
                 'PROGRAMA_ING SISTEMAS',
                 'PROGRAMA_INGENIERIA AGRONOMICA',
                 'PROGRAMA_INGENIERIA AMBIENTAL',
                 'PROGRAMA_INGENIERIA AMBIENTAL ',
                 'PROGRAMA_INGENIERÍA AGRONOMIA',
                 'PROGRAMA_INGENIERÍA AGRONOMICA',
                 'PROGRAMA_INGENIERÍA AGRONOMICA ',
                 'PROGRAMA_INGENIERÍA AGRONÓMICA',
                 'PROGRAMA_INGENIERÍA AMBIENTAL',
                 'PROGRAMA_INGENIERÍA DE ALIMENTO',
                 'PROGRAMA_INGENIERÍA DE ALIMENTOS',
                 'PROGRAMA_INGENIERÍA DE SISTEMAS',
                 'PROGRAMA_INGENIERÍA INDUSTRIAL',
                 'PROGRAMA_INGENIERÍA MECÁNICA',
                 'PROGRAMA_LIC EN CIENCIAS NATURALES Y EDU AMBIENTA',
                 'PROGRAMA_LIC EN CIENCIAS NATURALES Y EDU AMBIENTAL',
                 'PROGRAMA_LIC EN CIENCIAS SOCIALES',
                 'PROGRAMA_LIC EN EDUC BÁSICA CON ENF EN CIEN SOCIA',
                 'PROGRAMA_LIC EN EDUC BÁSICA CON ENF EN HUMAN INGL',
                 'PROGRAMA_LIC EN EDUC BÁSICA CON ENF HUM LENG CAST',
                 'PROGRAMA_LIC EN EDUCACION ARTISTICA',
                 'PROGRAMA_LIC EN INFORMÁTICA',
                 'PROGRAMA_LIC EN LENGUAS EXTRAN CON ENFA EN INGLES',
                 'PROGRAMA_LIC EN LITERATURA Y LENGUA CASTELLANA',
                 'PROGRAMA_LIC. EDUCACIÓN BÁSICA ÉNFASIS ARTÍSTICA',
                 'PROGRAMA_LIC. EDUCACIÓN FÍSICA RECREACIÓN Y DEPOR',
                 'PROGRAMA_LIC. EN INFORMATICA',
                 'PROGRAMA_LIC. EN INFORMATICA Y MEDIOS AUDIOVISUALES',
                 'PROGRAMA_LIC. EN INFORMÁTICA',
                 'PROGRAMA_LIC. EN INFORMÁTICA ',
                 'PROGRAMA_LICENCIATURA EN EDUCACION INFANTIL',
                 'PROGRAMA_LICENCIATURA EN EDUCACIÓN INFANTIL',
                 'PROGRAMA_LICENCIATURA EN EDUCACIÓN INFANTIL ',
                 'PROGRAMA_LICENCIATURA EN INFORMATICA',
                 'PROGRAMA_LICENCIATURA EN INFORMÁTICA Y MEDIOS AUD',
                 'PROGRAMA_LICENCIATURA EN INGLES',
                 'PROGRAMA_MATEMÁTICAS',
                 'PROGRAMA_MEDICINA VETERINARIA',
                 'PROGRAMA_MEDICINA VETERINARIA Y ZOOTECNIA',
                 'PROGRAMA_OFICINA DE BIBLIOTECAS Y RECURSOS EDUCATIVOS',
                 'PROGRAMA_PRUEBAS',
                 'PROGRAMA_QUIMICA',
                 'PROGRAMA_QUIMICA ',
                 'PROGRAMA_QUÍMICA',
                 'PROGRAMA_QUÍ\xadMICA',
                 'PROGRAMA_REGENCIA DE FARMACIA',
                 'PROGRAMA_REGENCIA Y FARMACIA',
                 'PROGRAMA_TEC PROF EN MANEJO Y CONSERV DE PROD AGR',
                 'PROGRAMA_TECNOLOGÍA EN REGENCIA DE FARMACIA',
                 'PROGRAMA_VETERINARIA']
            df2 = pd.DataFrame(columns=col,data=[[*[0]*len(col)]])
            df2['IDENTIFICACION'] = self.IDENTIFICACION
            df2['TIMECREATED'] = self.TIMECREATED
            df2['HOUR'] = self.HOUR

            columO = [x for x in df2.columns if "ORIGIN_" in x and str(self.ORIGIN) == x.split('_')[-1]]
            df2[columO] = 1
            columP = [x for x in df2.columns if "PROGRAMA_" in x and str(self.PROGRAMA) == x.split('_')[-1]]
            df2[columP] = 1
            return df2
    
    def predict(self, y_name: str = 'DAY'):
            '''
            Clase para predecir.
            Carga el modelo, prepara los datos y predice.

            prediction = pd.DataFrame(self.model.predict(X)).rename(columns={0:y_name})

            '''

            self._load_model()
            X = self._prepare_data()
            prediction = pd.DataFrame(self.model.predict(X)).rename(columns={0: y_name})
            return prediction.to_dict(orient='records')