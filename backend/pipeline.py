import time
from database.database import create_tables, save_to_db
from scrapers.tech710 import scrape_tech710
from scrapers.mexx import scrape_mexx

PRODUCT_CATALOG = [
    "rtx 5050",
    "ryzen 5 5600",
]

def run_etl():
    """
    Executes the full Extract, Transform, Load (ETL) process.
    """
    print("🤖 Starting ETL Pipeline...")
    print("====================================")
    
    create_tables()
    
    for item in PRODUCT_CATALOG:
        print(f"\n--- 🔍 PROCESSING: {item.upper()} ---")
        
        # --- EXTRACT & LOAD: MEXX ---
        mexx_results = scrape_mexx(item, limit=3)
        save_to_db(item, mexx_results, "Mexx")
        
        print("⏳ Sleeping for 3 seconds to avoid bans...")
        time.sleep(3)
        
        # --- EXTRACT & LOAD: 710 TECH ---
        tech710_results = scrape_tech710(item, limit=3)
        save_to_db(item, tech710_results, "710 Tech")
        
        print("⏳ Sleeping for 3 seconds to avoid bans...")
        time.sleep(3)
        
    print("\n✅ ETL Pipeline finished successfully. Database is up to date!")

if __name__ == "__main__":
    run_etl()