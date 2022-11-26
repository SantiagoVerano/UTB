import requests
import os

url = "http://127.0.0.1"

def mostrar():
  # Get
  res = requests.get(url+"/selectperson")

  if (res.status_code == 200):
      for item in res.json():
          print("Cedula",item["cedula"])
          print("Nombres",item["nombres"])
          print("Apellidos",item["apellidos"])
          print("Edad",item["edad"])
          print("------------------------------------------------")
  else:
      print("Error comunicación con el servidor")

def insertar(persona):
  # POST
  res = requests.post(url+"/insertperson",json=persona)

  print(res.json())

def actualizar(persona):
  # Put

  res = requests.put(url+"/updateperson",json=persona)

  print(res.json())

def eliminar(cedula):
  # Delete
  res = requests.delete(url+f"/deleteperson?cedula={cedula}")

  print(res.json())

print("MENU")
print("--------------------")
print("1. Inserta")
print("2. Mostar")
print("3. Actualizar")
print("4. Eliminar")
print("5. Salir")

option = int(input("¿Que desea hace? "))

while option != 5:
    os.system ("cls")

    print("MENU")
    print("--------------------")
    print("1. Insertar")
    print("2. Mostrar")
    print("3. Actualizar")
    print("4. Eliminar")
    print("5. Salir")

    if option==1:
      print("Ingresar los siguientes datos: ")
      persona = {
        "cedula": input("¿Cedula? "),
        "nombres": input("¿Nombres? "),
        "apellidos": input("¿Apellidos? "),
        "edad": int(input("¿Edad? "))
      }

      insertar(persona)
    elif option==2:
      mostrar()
    elif option==3:
      print("Ingresar los siguientes datos para actualizar: ")
      persona = {
        "cedula": input("¿Cedula? "),
        "nombres": input("¿Nombres? "),
        "apellidos": input("¿Apellidos? "),
        "edad": int(input("¿Edad? "))
      }

      actualizar(persona)
    elif option==4:
      eliminar(input("¿Cedula a eliminar?"))
    else:
      print("Opción no valida")

    option = int(input("¿Que desea hace? "))
        
    print("Bye Bye Bye")