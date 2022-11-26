from fastapi import FastAPI
from pydantic import BaseModel
from models import peopledatabase
from mongoengine import connect
import json

connect(db="misiontic", host="localhost", port=27017)

app = FastAPI()

#people = peopledatabase.objects().to_json()

#lista = json.loads(people)

#lista=[] # Lista = Estructura de datos

#Objeto persona
class Personas(BaseModel):
    cedula:str
    nombres:str
    apellidos:str
    edad:int

@app.get("/selectperson") 
def mostrar():
    
    people = peopledatabase.objects().to_json()
    return json.loads(people)

@app.post("/insertperson") 
def guardar(datos:Personas): 
    tempo = peopledatabase()
    tempo.cedula=datos.cedula
    tempo.nombres=datos.nombres
    tempo.apellidos=datos.apellidos
    tempo.edad=datos.edad
    tempo.save()
    #lista.append(datos)
    
    people = peopledatabase.objects().to_json()
    return json.loads(people)

@app.put("/updateperson") 
def actualizar(datos:Personas):

    peopledatabase.objects(cedula=datos.cedula).update_one(nombres=datos.nombres,apellidos=datos.apellidos,edad=datos.edad,)

    return {"Mensaje": "Registro actualizado"}
   
    """estado=False
    for item in lista:
        if item.cedula == datos.cedula:
            lista.remove(item)
            lista.append(datos)
            estado=True
            break 
"""

@app.delete("/deleteperson")
def eliminar(cedula:str):
    peopledatabase.objects(cedula=cedula).delete()
    return {"Mensaje": "Eliminado"}
 
    """estado=False
    for item in lista:
        if item.cedula == cedula:
            lista.remove(item)
            estado=True
            break 

    if estado==True:
        return lista
    else:
        return {"Mensaje": "Registro no encontrado"}"""