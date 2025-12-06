import requests
from datetime import datetime

BASE_URL = "http://127.0.0.1:8000/api"  # если FastAPI запускается на localhost:8000

def test_get_products():
    resp = requests.get(f"{BASE_URL}/products")
    print("GET /products:", resp.status_code, resp.json())

def test_add_price():
    payload = {
        "product_id": 1,
        "price": 550,
        "source_id": "AD002",
        "date": datetime.now().isoformat()  # текущая дата
    }
    resp = requests.post(f"{BASE_URL}/prices", json=payload)
    print("POST /prices:", resp.status_code, resp.json())

def test_get_prices():
    resp = requests.get(f"{BASE_URL}/prices", params={"product_id": 1})
    print("GET /prices?product_id=1:", resp.status_code, resp.json())

if __name__ == "__main__":
    test_get_products()
    test_add_price()
    test_get_prices()
