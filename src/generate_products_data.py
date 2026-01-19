import pandas as pd
import random
from datetime import datetime, timedelta
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
OUTPUT_FILE = BASE_DIR / "sources" / "products.csv"

START_DATE = datetime(2023, 1, 1)
END_DATE = datetime(2023, 12, 31)

PRODUCTS = [
    {"product_id": 101, "product_name": "Wireless Mouse", "category": "Electronics", "unit_cost": 12.50, "unit_price": 29.99, "supplier": "TechPro Solutions"},
    {"product_id": 102, "product_name": "Bluetooth Headphones", "category": "Electronics", "unit_cost": 45.00, "unit_price": 89.99, "supplier": "AudioMax Inc"},
    {"product_id": 103, "product_name": "USB-C Cable 2m", "category": "Accessories", "unit_cost": 8.00, "unit_price": 19.99, "supplier": "CableTech Ltd"},
    {"product_id": 104, "product_name": "Laptop Stand", "category": "Office", "unit_cost": 25.00, "unit_price": 59.99, "supplier": "ErgoWorks Co"},
    {"product_id": 105, "product_name": "Mechanical Keyboard", "category": "Electronics", "unit_cost": 75.00, "unit_price": 149.99, "supplier": "KeyMaster Corp"},
    {"product_id": 106, "product_name": "Mouse Pad XL", "category": "Accessories", "unit_cost": 14.00, "unit_price": 34.99, "supplier": "DeskGear Inc"},
    {"product_id": 107, "product_name": "27 inch Monitor", "category": "Electronics", "unit_cost": 125.00, "unit_price": 249.99, "supplier": "DisplayTech Ltd"},
    {"product_id": 108, "product_name": "Webcam HD 1080p", "category": "Electronics", "unit_cost": 85.00, "unit_price": 199.99, "supplier": "VisionPro Systems"},
    {"product_id": 109, "product_name": "Desk Organizer", "category": "Office", "unit_cost": 32.00, "unit_price": 79.99, "supplier": "OfficePlus Co"},
    {"product_id": 110, "product_name": "LED Desk Lamp", "category": "Office", "unit_cost": 18.00, "unit_price": 44.99, "supplier": "LightWorks Inc"}
]


def random_date():
    delta = END_DATE - START_DATE
    random_days = random.randint(0, delta.days)
    return START_DATE + timedelta(days=random_days)


def generate_data():
    records = []
    
    for product in PRODUCTS:
        records.append({
            "product_id": product["product_id"],
            "product_name": product["product_name"],
            "category": product["category"],
            "unit_cost": product["unit_cost"],
            "unit_price": product["unit_price"],
            "supplier": product["supplier"],
            "created_date": random_date().strftime("%Y-%m-%d")
        })
    
    df = pd.DataFrame(records)
    df = df.sort_values("product_id").reset_index(drop=True)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Generated {len(df)} products to {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_data()
