import pandas as pd
import random
from datetime import datetime, timedelta
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
OUTPUT_FILE = BASE_DIR / "sources" / "sales_data.csv"
CUSTOMERS_FILE = BASE_DIR / "sources" / "customers.csv"

START_DATE = datetime(2024, 1, 1)
END_DATE = datetime.now()
NUM_RECORDS = 500
PRODUCTS = {
    101: 29.99,
    102: 89.99,
    103: 19.99,
    104: 59.99,
    105: 149.99,
    106: 34.99,
    107: 249.99,
    108: 199.99,
    109: 79.99,
    110: 44.99
}

PAYMENT_METHODS = ["Credit Card", "Credit Card", "Credit Card", "Debit Card", "Online", "Cash"]

FREQUENT_CUSTOMERS = list(range(501, 520))
REGULAR_CUSTOMERS = list(range(520, 601))


def random_date():
    delta = END_DATE - START_DATE
    random_days = random.randint(0, delta.days)
    return START_DATE + timedelta(days=random_days)


def load_customer_countries():
    customers_df = pd.read_csv(CUSTOMERS_FILE)
    return dict(zip(customers_df["customer_id"], customers_df["country"]))


def generate_data():
    customer_countries = load_customer_countries()
    records = []
    
    for i in range(NUM_RECORDS):
        order_id = 1001 + i
        order_date = random_date().strftime("%Y-%m-%d")
        
        if random.random() < 0.4:
            customer_id = random.choice(FREQUENT_CUSTOMERS)
        else:
            customer_id = random.choice(REGULAR_CUSTOMERS)
        
        product_id = random.choice(list(PRODUCTS.keys()))
        quantity = random.randint(1, 10)
        unit_price = PRODUCTS[product_id]
        total_amount = round(quantity * unit_price, 2)
        payment_method = random.choice(PAYMENT_METHODS)
        country = customer_countries[customer_id]
        
        records.append({
            "order_id": order_id,
            "order_date": order_date,
            "customer_id": customer_id,
            "product_id": product_id,
            "quantity": quantity,
            "unit_price": unit_price,
            "total_amount": total_amount,
            "payment_method": payment_method,
            "country": country
        })
    
    df = pd.DataFrame(records)
    df = df.sort_values("order_date").reset_index(drop=True)
    df["order_id"] = range(1001, 1001 + len(df))
    
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Generated {len(df)} records to {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_data()
