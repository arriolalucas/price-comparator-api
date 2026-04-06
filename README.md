# 🖥️ Motor de Análisis de Hardware

Un sistema automatizado (ETL) y API para rastrear, comparar y analizar precios de componentes de hardware en el mercado argentino.

## 🚀 Arquitectura del Proyecto

Este repositorio es un Monorepo que actualmente contiene la lógica del Backend:
* **Scrapers:** Extracción de datos en tiempo real de tiendas (Mexx, Tech710).
* **Pipeline ETL:** Limpieza y carga automatizada a una base de datos SQLite.
* **API REST:** Servidor construido con FastAPI para consultar los historiales de precio.

## 🛠️ Tecnologías Utilizadas
* Python 3.x
* FastAPI & Uvicorn
* SQLite3
* BeautifulSoup & Requests

## ⚙️ Instalación y Uso Local

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/arriolalucas/price-comparator-api.git](https://github.com/arriolalucas/price-comparator-api.git)
   cd tu-repositorio/backend

2. **Crear y activar el entorno virtual:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # En Windows

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt

4. **Ejecutar el Pipeline ETL (Actualizar base de datos):**
   ```bash
   python pipeline.py

5. **Levantar la API:**
   ```bash
   uvicorn main:app --reload
