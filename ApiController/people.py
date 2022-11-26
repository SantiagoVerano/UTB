from fastapi import FastAPI
from models import peopledatabase
from mongoengine import connect

app = FastAPI()

connect(db="misiontic", host="localhost", port=27017)

@app.get("/viewpeople") 
def mostrar():
    peopleView = peopledatabase.objects().to_json()
    print(peopleView)