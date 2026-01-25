import pandas as pd
from pathlib import Path
from sqlalchemy import text
from db_config import get_engine

BASE_DIR = Path(__file__).parent.parent
SOURCES_DIR = BASE_DIR / "sources"


def load_products():
    csv_path = SOURCES_DIR / "products.csv"
    
    if not csv_path.exists():
        print(f"Products file not found: {csv_path}")
        print("Run 'python generate_products_data.py' first.")
        return False
    
    df = pd.read_csv(csv_path)
    engine = get_engine()
    

    with engine.connect() as conn:
        conn.execute(text("DELETE FROM sales WHERE TRUE;"))  
        conn.execute(text("DELETE FROM products WHERE TRUE;"))
        conn.commit()
    
    df.to_sql("products", engine, if_exists="append", index=False)
    print(f"Loaded {len(df)} products to PostgreSQL")
    return True


def load_customers():
    csv_path = SOURCES_DIR / "customers.csv"
    
    if not csv_path.exists():
        print(f"Customers file not found: {csv_path}")
        print("Run 'python generate_customers_data.py' first.")
        return False
    
    df = pd.read_csv(csv_path)
    engine = get_engine()
    
    with engine.connect() as conn:
        conn.execute(text("DELETE FROM sales WHERE TRUE;"))  
        conn.execute(text("DELETE FROM customers WHERE TRUE;"))
        conn.commit()
    
    df.to_sql("customers", engine, if_exists="append", index=False)
    print(f"Loaded {len(df)} customers to PostgreSQL")
    return True


def load_sales():
    csv_path = SOURCES_DIR / "sales_data.csv"
    
    if not csv_path.exists():
        print(f"Sales file not found: {csv_path}")
        print("Run 'python generate_sales_data.py' first.")
        return False
    
    df = pd.read_csv(csv_path)
    engine = get_engine()
    

    with engine.connect() as conn:
        conn.execute(text("DELETE FROM sales WHERE TRUE;"))
        conn.commit()
    
    df.to_sql("sales", engine, if_exists="append", index=False)
    print(f"Loaded {len(df)} sales records to PostgreSQL")
    return True


def load_all():
    print("=" * 50)
    print("Loading data to PostgreSQL: products, customers, sales")
    print("=" * 50)
  
    if not load_products():
        return
    
    if not load_customers():
        return
    
    if not load_sales():
        return
    
    print("=" * 50)
    print("All data loaded successfully!")
    print("=" * 50)


def get_table_counts():
    engine = get_engine()
    
    with engine.connect() as conn:
        products_count = conn.execute(text("SELECT COUNT(*) FROM products")).scalar()
        customers_count = conn.execute(text("SELECT COUNT(*) FROM customers")).scalar()
        sales_count = conn.execute(text("SELECT COUNT(*) FROM sales")).scalar()
    
    print(f"\nTable row counts:")
    print(f"  - products:  {products_count}")
    print(f"  - customers: {customers_count}")
    print(f"  - sales:     {sales_count}")

if __name__ == "__main__":
    load_all()
    get_table_counts()
