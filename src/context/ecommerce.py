# src/context/ecommerce.py
from datetime import datetime

def get_ecommerce_queries():
    current_month_year = datetime.now().strftime("%B %Y")
    return [
        f"upcoming e-commerce sale events {current_month_year}",
        f"global shopping trends Q{ (datetime.now().month-1)//3 + 1 } {datetime.now().year}",
        "major supply chain disruptions affecting retail current status"
    ]