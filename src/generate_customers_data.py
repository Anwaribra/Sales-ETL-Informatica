import pandas as pd
import random
from datetime import datetime, timedelta
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
OUTPUT_FILE = BASE_DIR / "sources" / "customers.csv"

START_DATE = datetime(2023, 1, 1)
END_DATE = datetime.now()
NUM_CUSTOMERS = 100

COUNTRIES_DATA = {
    "US": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"],
    "UK": ["London", "Manchester", "Birmingham", "Leeds", "Glasgow", "Liverpool", "Bristol", "Sheffield", "Edinburgh", "Cardiff"],
    "Germany": ["Berlin", "Munich", "Hamburg", "Frankfurt", "Cologne", "Stuttgart", "Dusseldorf", "Leipzig", "Dresden", "Nuremberg"],
    "Egypt": ["Cairo", "Alexandria", "Giza", "Luxor", "Aswan", "Hurghada", "Sharm El Sheikh", "Port Said", "Suez", "Mansoura"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman", "Ras Al Khaimah", "Fujairah", "Al Ain", "Umm Al Quwain", "Khor Fakkan", "Dibba"]
}

NAMES_BY_COUNTRY = {
    "US": ["James Wilson", "Michael Brown", "David Johnson", "Sarah Davis", "Robert Miller", "Jennifer Taylor", "William Martinez", "Emily Anderson", "Daniel Garcia", "Jessica Thomas"],
    "UK": ["Emma Thompson", "Oliver Smith", "Charlotte Wilson", "Grace Roberts", "Sophia Moore", "Lucy Morris", "Hannah Edwards", "Amelia Wright", "Lily Mitchell", "Daisy Cooper"],
    "Germany": ["Hans Mueller", "Sophie Weber", "Thomas Schmidt", "Lukas Fischer", "Felix Wagner", "Anna Becker", "Max Hoffman", "Julia Richter", "Leon Meyer", "Paul Schulz"],
    "Egypt": ["Ahmed Hassan", "Mohamed Salah", "Nour Ibrahim", "Amira Mahmoud", "Youssef Ali", "Hassan Mostafa", "Mariam Fathy", "Rania Adel", "Dina Ezzat", "Salma Kamal"],
    "UAE": ["Fatima Al-Rashid", "Khalid Omar", "Layla Ahmed", "Sara Khalil", "Aisha Rahman", "Ali Nasser", "Mona Tarek", "Zainab Youssef", "Hana Khaled", "Mahmoud Hany"]
}

SEGMENTS = ["Premium", "Premium", "Standard", "Standard", "Standard", "Basic", "Basic", "Basic", "Basic", "Basic"]
DOMAINS = {"US": "email.com", "UK": "email.co.uk", "Germany": "email.de", "Egypt": "email.eg", "UAE": "email.ae"}


def random_date():
    delta = END_DATE - START_DATE
    random_days = random.randint(0, delta.days)
    return START_DATE + timedelta(days=random_days)


def generate_email(name, country):
    clean_name = name.lower().replace(" ", ".").replace("-", "")
    return f"{clean_name}@{DOMAINS[country]}"


def generate_data():
    records = []
    used_names = set()
    
    for i in range(NUM_CUSTOMERS):
        customer_id = 501 + i
        country = random.choice(list(COUNTRIES_DATA.keys()))
        
        name = random.choice(NAMES_BY_COUNTRY[country])
        while name in used_names and len(used_names) < 50:
            name = random.choice(NAMES_BY_COUNTRY[country])
        used_names.add(name)
        
        if name in used_names:
            name = f"{name} {random.randint(1, 99)}"
        
        email = generate_email(name, country)
        city = random.choice(COUNTRIES_DATA[country])
        registration_date = random_date().strftime("%Y-%m-%d")
        segment = random.choice(SEGMENTS)
        
        records.append({
            "customer_id": customer_id,
            "customer_name": name,
            "email": email,
            "country": country,
            "city": city,
            "registration_date": registration_date,
            "customer_segment": segment
        })
    
    df = pd.DataFrame(records)
    df = df.sort_values("customer_id").reset_index(drop=True)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Generated {len(df)} customers to {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_data()
