"""Sintetik (saxta) musteri melumati. Real sexsi melumat YOXDUR."""
import csv
import random

random.seed(42)
first = ["Aysel", "Elnur", "Leyla", "Resad", "Nermin", "Tural", "Gunel", "Orxan", "Sebine", "Kamran"]
last = ["Memmedov", "Eliyeva", "Huseynov", "Quliyeva", "Nebiyev", "Rehimova", "Ceferov", "Abbasova"]

with open("customers_synthetic.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["customer_id", "full_name", "email", "phone", "card_last4", "order_total_azn"])
    for i in range(1, 51):
        w.writerow([
            f"C{i:04d}",
            f"{random.choice(first)} {random.choice(last)}",
            f"customer{i:04d}@example.com",
            f"+994-00-{random.randint(100,999)}-{random.randint(10,99)}-{random.randint(10,99)}",
            f"{random.randint(0,9999):04d}",
            round(random.uniform(10, 500), 2),
        ])
print("customers_synthetic.csv hazirdir (50 setir)")