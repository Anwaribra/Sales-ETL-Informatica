from sqlalchemy import text
from db_config import get_engine


CREATE_PRODUCTS_TABLE = """
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    unit_cost DECIMAL(10, 2) NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    supplier VARCHAR(100) NOT NULL,
    created_date DATE NOT NULL
);
"""

CREATE_CUSTOMERS_TABLE = """
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    country VARCHAR(50) NOT NULL,
    city VARCHAR(100) NOT NULL,
    registration_date DATE NOT NULL,
    customer_segment VARCHAR(20) NOT NULL
);
"""

CREATE_SALES_TABLE = """
CREATE TABLE IF NOT EXISTS sales (
    order_id INTEGER PRIMARY KEY,
    order_date DATE NOT NULL,
    customer_id INTEGER NOT NULL REFERENCES customers(customer_id),
    product_id INTEGER NOT NULL REFERENCES products(product_id),
    quantity INTEGER NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    total_amount DECIMAL(12, 2) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL
);
"""

# Create indexes 
CREATE_INDEXES = """
CREATE INDEX IF NOT EXISTS idx_sales_order_date ON sales(order_date);
CREATE INDEX IF NOT EXISTS idx_sales_customer_id ON sales(customer_id);
CREATE INDEX IF NOT EXISTS idx_sales_product_id ON sales(product_id);
CREATE INDEX IF NOT EXISTS idx_sales_country ON sales(country);
CREATE INDEX IF NOT EXISTS idx_customers_country ON customers(country);
CREATE INDEX IF NOT EXISTS idx_customers_segment ON customers(customer_segment);
CREATE INDEX IF NOT EXISTS idx_products_category ON products(category);
"""


def create_tables():
    engine = get_engine()
    
    with engine.connect() as conn:
        print("Creating products table...")
        conn.execute(text(CREATE_PRODUCTS_TABLE))
        
        print("Creating customers table...")
        conn.execute(text(CREATE_CUSTOMERS_TABLE))
        
        print("Creating sales table...")
        conn.execute(text(CREATE_SALES_TABLE))

        print("Creating indexes...")
        for index_stmt in CREATE_INDEXES.strip().split(";"):
            if index_stmt.strip():
                conn.execute(text(index_stmt))
        conn.commit()
    
    print("All tables created successfully!")


def drop_tables():
    engine = get_engine()
    
    with engine.connect() as conn:
        print("Dropping tables...")
        conn.execute(text("DROP TABLE IF EXISTS sales CASCADE;"))
        conn.execute(text("DROP TABLE IF EXISTS customers CASCADE;"))
        conn.execute(text("DROP TABLE IF EXISTS products CASCADE;"))
        conn.commit()
    
    print("All tables dropped.")


if __name__ == "__main__":
    create_tables()
