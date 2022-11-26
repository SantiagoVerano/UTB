from django.http import HttpResponse
import requests

from django.shortcuts import render

url = "http://127.0.0.1"
"""
def mostrar(request):
    res = requests.get(url+"/selectperson")

    if (res.status_code == 200):
        return HttpResponse(res.json())
    else:
        return HttpResponse("Error comuniacion con el servidor")

"""
    
def mostrar(request):
    #get
    res = requests.get(url+"/selectperson")

    if (res.status_code == 200):
        return render(request,"mostrar.html",context={"datos":res.json()})
    else:
        return HttpResponse("Error de comunicacion con el servidor")


def guardar(request):
    persona={
        "cedula":request.GET["cedula"],
        "nombres":request.GET["nombres"],
        "apellidos":request.GET["apellidos"],
        "edad":request.GET["edad"]
    }
    
    #post
    res = requests.post(url+"/insertperson",json=persona)

    if (res.status_code == 200):
        return HttpResponse("OK") #render(request,"mostrar.html",context={"datos":res.json()})
        
    else:
        return HttpResponse("Error de comunicacion con el servidor")

def actualizar(request):

    persona={
        "cedula":request.GET["cedula"],
        "nombres":request.GET["nombres"],
        "apellidos":request.GET["apellidos"],
        "edad":request.GET["edad"]
    }

    #put
    res = requests.put(url+"/updateperson",json=persona)

    if (res.status_code == 200):
        return HttpResponse("OK")
        
    else:
        return HttpResponse("Error de comunicacion con el servidor")

def eliminar(request):
    #delete
    res = requests.delete(url+"/deleteperson?cedula="+request.GET["cedula"])

    if (res.status_code == 200):
        return HttpResponse("OK")
    else:
        return HttpResponse("Error de comunicacion con el servidor")

