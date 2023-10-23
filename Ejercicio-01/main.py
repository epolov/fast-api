from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

database = {}

class User(BaseModel):
  id: int
  name: str
  email: str
  age: int

  #API GET - Crear usuario

@app.post("/users")
def create_user(user: User):
  # Simulamos la creacion del usuario en la base de datos
  database[user.id] = user
  # Devolvemos un mensaje para hacer saber que el usuario se ha creado correctamente
  return {"message": "Usuario creado correctamente"}

#API GET - Consulta usuarios bd

@app.get("/users")
def get_all_users():
  # Devolvemos la lista de todos los usuarios en la db fake de memoria
  return list(database.values())

#Obtener usuario por ID

@app.get("/users/{user_id}")
def get_user(user_id: int):
    # Recuperamos el usuario de nuestra base de datos en memoria usando path params
    user = database.get(user_id)
    # Si hemos encontrado el usuario, lo develolvemos como respuesta
    if user:
        return user
    # En caso de no encontrarlo, develovemos este mensaje
    return {"error": "Usuario no encontrado"}

#ACTUALIZAR USUARIO
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    # Comprovamos si el usuario con el id pasado existe.
    if user_id in database:
      # En caso de existir actualizamos el usuaro con los nuevos datos.
      database[user_id] = user
      # Devolvemos un mensaje para informar de que se ha actualizado correctamente.
      return {"message": "Usuario actualizado correctamente"}
    # En caso de no encontrar el usuario, devolvemos esete mensaje
    return {"error": "Usuario no encontrado"}

#ELIMINAR USUARIO
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
  # Comprovamos si el usuario con el id pasado existe.
  if user_id in database:
    # Elimina el usuario de la base de datos simulada
    del database[user_id]
    # Devolvemos un mensaje para informar de que se ha borrado correctamente.
    return {"message": "Usuario eliminado correctamente"}
  # En caso de no encontrar el usuario, devolvemos esete mensaje
  return {"error": "Usuario no encontrado"}