#FASTAPI - UVICORN
#pip install fastapi 
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

#Estructura de datos
class Mensaje(BaseModel):
    id: Optional[int] = None
    user: str
    mensaje: str


web = FastAPI()

#Base de datos simulada
mensajes_db = []

@web.post("/mensajes/", response_model=Mensaje)
def crear_mensaje(mensaje : Mensaje):
    mensaje.id = len(mensajes_db) +1
    mensajes_db.append(mensaje)
    return mensaje

@web.get("/mensajes/{mensaje_id}", response_model=Mensaje)
def obtener_mensaje(mensaje_id: int):
    for mensaje in mensajes_db:
        if mensaje.id == mensaje_id:
            return mensaje
    raise HTTPException(status_code=404, detail="Mensaje no encontrado")

@web.get("/mensajes/", response_model=list[Mensaje])
def listar_mensaje():
    return mensajes_db

@web.put("/mensajes/{mensaje_id}", response_model=Mensaje)
def actualizar_mensaje(mensaje_id: int, mensaje_actualizado: Mensaje):
    for index, mensaje in enumerate(mensajes_db):
        if mensaje.id == mensaje_id:
            mensajes_db[index] = mensaje_actualizado
            return mensaje_actualizado
    raise HTTPException(status_code=404, detail="Mensaje no encontrado")

@web.delete("/mensajes/{mensaje_id}", response_model=dict)
def eliminar_mensaje(mensaje_id: int):
    for index, mensaje in enumerate(mensajes_db):
        if mensaje.id == mensaje_id:
            del mensajes_db[index]
            return {"detail": "Mensaje eliminado"}
    raise HTTPException(status_code=404, detail="Mensaje no encontrado")
   



