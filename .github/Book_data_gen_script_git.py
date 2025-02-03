import pandas as pd
import random
import os
from datetime import datetime, timedelta

data_file = ".github/books_database_main.csv"

cities = ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань", "Нижний Новгород",
    "Челябинск", "Самара", "Омск", "Ростов-на-Дону", "Уфа", "Красноярск"]
book_categories = ["Фантастика", "Научная литература", "Роман", "Бизнес", "Детектив", "История", "Психология",
    "Проза", "Саморазвитие", "Классика", "Фэнтези", "Здоровье", "Комикс"]
devices = ["iOS", "Android", "E-Reader"]
book_types = ["audio", "reading"]
purchase_types = ["monthly_subscription", "yearly_subscription", "one_time_purchase"]


start_user_id = 1000
user_growth_rate = random.randint(100,200)  

def generate_price(action, purchase_type, category):
    base_price = random.uniform(5, 100)  

    if purchase_type == "monthly_subscription":
        discount = 0.08
    elif purchase_type == "yearly_subscription":
        discount = 0.15
    else:
        discount = 0

    if category in ["Фантастика", "Детектив"] and random.random() < 0.2: 
        discount += 0.1

    final_price = base_price * (1 - discount) if action == "purchase" else 0
    return round(final_price, 2)

def generate_timespent(action):
    timespent = random.randint(1, 500) if action == "purchase" else 0
    return timespent

def generate_book_type(device):
    final_book_type = random.choice(book_types) if device != "E-Reader" else "reading"
    return final_book_type

def generate_daily_data(existing_user_count):
    current_date = datetime.now().strftime("%Y-%m-%d")
    new_users = existing_user_count + user_growth_rate

    daily_data = {
        "date": [current_date] * user_growth_rate,
        "user_id": [random.randint(1, 1000) for _ in range(user_growth_rate)],
        "book_id": [random.randint(1, 500) for _ in range(user_growth_rate)],
        "category": [random.choice(book_categories) for _ in range(user_growth_rate)],
        "action": [random.choice(["purchase", "wishlist"]) for _ in range(user_growth_rate)],
        "purchase_type": [random.choice(purchase_types) for _ in range(user_growth_rate)],
        "time_spent_minutes": [],
        "purchase_price": [],
        "book_type": [],
        "device": [random.choice(devices) for _ in range(user_growth_rate)],
        "city": [random.choice(cities) for _ in range(user_growth_rate)]
        }

    for i in range(user_growth_rate):
        action = daily_data["action"][i]
        purchase_type = daily_data["purchase_type"][i]
        category = daily_data["category"][i]
        daily_data["purchase_price"].append(generate_price(action, purchase_type, category))

    for i in range(user_growth_rate):
        action = daily_data["action"][i]
        daily_data["time_spent_minutes"].append(generate_timespent(action))

    for i in range(user_growth_rate):
        device = daily_data["device"][i]
        daily_data["book_type"].append(generate_book_type(device))
    
    return pd.DataFrame(daily_data)

def update_data_file():
    if os.path.exists(data_file):
        existing_data = pd.read_csv(data_file)
        existing_user_count = existing_data['user_id'].max()
    else:
        print(f"Existing data file 'book_app_v2' not found. Script not executed.")
        existing_user_count = start_user_id

    daily_data = generate_daily_data(existing_user_count)

    if os.path.exists(data_file): 
        updated_data = pd.concat([existing_data, daily_data], ignore_index=True)
    else:
        print(f"Script failed - existing file not update with daily data from {datetime.now().strftime('%Y-%m-%d')}.")

    updated_data.to_csv(data_file, index=False)
    print(f"Данные за {datetime.now().strftime('%Y-%m-%d')} добавлены.")

if __name__ == "__main__":
    update_data_file()
