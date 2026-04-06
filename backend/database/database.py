import sqlite3
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "prices.db")

def create_tables():
    """
    Initializes the database and creates the main table if it doesn't exist.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS price_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            search_term TEXT NOT NULL,
            title TEXT NOT NULL,
            price REAL NOT NULL,
            store TEXT NOT NULL,
            scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("🗄️ Database and tables initialized successfully.")

def save_to_db(search_term: str, products: list, store_name: str):
    """
    Receives a list of product dictionaries and saves them into the database.
    """
    if not products:
        print(f"⚠️ No products to save for {store_name}.")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    records_to_insert = []
    for item in products:
        records_to_insert.append((
            search_term, 
            item["title"], 
            item["price"], 
            store_name, 
            current_time
        ))
        
    cursor.executemany('''
        INSERT INTO price_history (search_term, title, price, store, scraped_at)
        VALUES (?, ?, ?, ?, ?)
    ''', records_to_insert)
    
    conn.commit()
    conn.close()
    print(f"💾 Successfully saved {len(products)} records from {store_name} into the DB.")