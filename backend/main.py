from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/precios")
def get_prices():

    conexion = sqlite3.connect("database/prices.db")
    
    conexion.row_factory = sqlite3.Row 
    
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM price_history")
    
    raw_data = cursor.fetchall()

    conexion.close()

    price_list = [dict(fila) for fila in raw_data]

    return price_list