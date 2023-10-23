from fastapi import HTTPException
from pydantic import BaseModel, constr, EmailStr

app = FastAPI()

database = {}

class User(BaseModel):
   id: int
   name: constr(min_length=1, max_length=50)
   email: EmailStr
   age: int

  #API GET - Crear usuario

@app.post("/users")
def create_user(user: User):
      # Comprovamos si el el id introducido esta ya en uso
      if user.id in database:
         # Si el usuario con el id introducido ya existe, devolvemos un error
         raise HTTPException(
               status_code=400, detail="El Usuario con el id introducido ya existe")
      # Comprovamos si el el email introducido esta ya en uso
      if user.email in database:
         # Si el usuario con el email introducido ya existe, devolvemos un error
         raise HTTPException(
               status_code=400, detail="El Usuario con el email introducido ya existe")
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
def get_user(user_id: int = None):
      # Recuperamos el usuario de nuestra base de datos en memoria
      user = database.get(user_id)
      # Si hemos encontrado el usuario, lo develolvemos como respuesta
      if user:
         return user
      # En caso de no encontrarlo, devolvemos un error con codio 404
      raise HTTPException(
         status_code=404, detail="Usuario no encontrado")

#ACTUALIZAR USUARIO
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
      # Comprovamos si el usuario con el id pasado existe.
      if user_id in database:
         # En caso de existir actualizamos el usuaro con los nuevos datos.
         database[user_id] = user
         # Devolvemos un mensaje para informar de que se ha actualizado correctamente.
         return {"message": "Usuario actualizado correctamente"}
      # En caso de no encontrarlo, devolvemos un error con codio 404
      raise HTTPException(
         status_code=404, detail="Usuario no encontrado")

#ELIMINAR USUARIO
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
      # Comprovamos si el usuario con el id pasado existe.
    if user_id in database:
         # Elimina el usuario de la base de datos simulada
        del database[user_id]
         # Devolvemos un mensaje para informar de que se ha borrado correctamente.
        return {"message": "Usuario eliminado correctamente"}
      # En caso de no encontrarlo, devolvemos un error con codio 404
    raise HTTPException(
      status_code=404, detail="Usuario no encontrado")