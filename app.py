# app.py

from fastapi import FastAPI
from pydantic import BaseModel
import json, os, numpy as np
from sentence_transformers import SentenceTransformer, util
import time

app = FastAPI()

# Cargar modelo
modelo = SentenceTransformer("all-MiniLM-L6-v2")

# Cargar comandos y vectores
with open("comandos.json") as f:
    comandos = json.load(f)

titulos = [cmd["titulo"] for cmd in comandos]
vectores_path = "data/vectores.npy"

if os.path.exists(vectores_path):
    vectores = np.load(vectores_path)
else:
    vectores = modelo.encode(titulos)
    np.save(vectores_path, vectores)

class Pregunta(BaseModel):
    texto: str

@app.post("/preguntar")
def preguntar(data: Pregunta):
    start = time.time()
    vector_pregunta = modelo.encode([data.texto])[0]
    similitudes = util.cos_sim(vector_pregunta, vectores)[0]
    idx = int(np.argmax(similitudes))
    similitud = float(similitudes[idx])
    cmd = comandos[idx]
    tinf = time.time() - start
    return {
        "titulo": cmd["titulo"],
        "comando": cmd["comando"],
        "similitud": similitud,
        "tiempo": tinf
    }
