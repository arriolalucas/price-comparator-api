import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def scrape_mexx(search_term: str, limit: int = 5):
    """
    Scrapes product data from Mexx.
    Returns a list of dictionaries containing title, price, and condition.
    """
    formatted_search = search_term.replace(" ", "+")
    url = f"https://www.mexx.com.ar/buscar/?p={formatted_search}"
    
    print(f"🚀 Fetching data from Mexx for: {search_term.upper()}...")
    
    response = requests.get(url, headers=HEADERS)
    extracted_products = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        product_cards = soup.find_all("div", class_="card-ecommerce")
        
        for card in product_cards:
            if len(extracted_products) >= limit:
                break
                
            try:
                title = card.find("h4", class_="card-title").text.strip()
                title_lower = title.lower()
                blacklist = ["pc", "armada", "computadora", "combo", "notebook", "kit"]
                
                if any(word in title_lower for word in blacklist):
                    continue
                
                price_box = card.find("div", class_="price")
                price_raw = price_box.find("h4").text.strip()
                price_split = price_raw.split("\n")[0] 
                clean_price = float(price_split.replace("$", "").replace(".", "").strip())
                
                extracted_products.append({
                    "title": title,
                    "price": clean_price,
                })
                
            except AttributeError:
                continue
                
        return extracted_products
        
    return []

# ==========================================
# TESTING LOCAL (Diagnóstico)
# ==========================================
if __name__ == "__main__":
    
    test_results = scrape_mexx("rtx 3050", limit=3)
    
    print("\n--- RESULTS ---")
    for item in test_results:
        print(item)