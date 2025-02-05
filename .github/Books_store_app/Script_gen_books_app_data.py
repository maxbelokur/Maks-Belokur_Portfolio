import pandas as pd
import random
import os
import json
from datetime import datetime, timedelta

data_file = ".github/Books_store_app/books_data_main.csv"
profiles_file = ".github/Books_store_app/user_profiles.json"
library_file = ".github/Books_store_app/library.json"

cities = ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань", "Нижний Новгород",
          "Челябинск", "Самара", "Омск", "Ростов-на-Дону", "Уфа", "Красноярск"]
book_categories = ["Фантастика", "Научная литература", "Роман", "Бизнес", "Детектив", "История", "Психология",
                   "Проза", "Саморазвитие", "Классика", "Фэнтези", "Здоровье", "Комикс"]
devices = ["iOS", "Android", "E-Reader"]
book_types = ["audio", "reading"]
purchase_types = ["monthly_subscription", "yearly_subscription", "one_time_purchase"]

# Блок с функциями для генерации повторяющихся и новых ID пользователей с привязкой к устройству и городу.
# После каждого запуска библиотека пополняется новыми пользователями.
def load_user_profiles():
    if os.path.exists(profiles_file):
        with open(profiles_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_user_profiles():
    with open(profiles_file, "w", encoding="utf-8") as f:
        json.dump(user_profiles, f, ensure_ascii=False, indent=4)

def get_or_create_user(user_profiles, existing_user_count):
    if random.random() < 0.55 and user_profiles:
        user_id = random.choice(list(user_profiles.keys()))
        profile = user_profiles[user_id]
    else:
        user_id = str(existing_user_count + len(user_profiles) + 1)
        profile = {"device": random.choice(devices), "city": random.choice(cities)}
        user_profiles[user_id] = profile
    return user_id, profile["device"], profile["city"]

# Блок с функциями для генерации повторяющихся и новых ID книг с привязкой по категориям.
# После каждого запуска библиотека пополняется новыми книгами.
def load_library():
    if os.path.exists(library_file):
        with open(library_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_library():
    with open(library_file, "w", encoding="utf-8") as f:
        json.dump(library, f, ensure_ascii=False, indent=4)

def get_or_create_library(library):
    if random.random() < 0.7 and library:
        book_id = random.choice(list(library.keys()))
        library_category = library[book_id]
    else:
        book_id = str(100 + len(library) + 1)
        library_category = {"category": random.choice(book_categories)}
        library[book_id] = library_category
    return book_id, library_category["category"]
    
# Функция для расчета скидки цены взависимости от наличия подписки. 
def generate_price(action, purchase_type, category):
    base_price = random.uniform(5, 100)
    discount = 0.08 if purchase_type == "monthly_subscription" else 0.15 if purchase_type == "yearly_subscription" else 0
    return round(base_price * (1 - discount), 2) if action == "purchase" else 0

# Функция для учета время чтения, только для купленной книги. 
def generate_timespent(action):
    return random.randint(1, 500) if action == "purchase" else 0

# Функция которая ограничивает появление аудио книги для устройства E-Reader. 
def generate_book_type(device):
    return random.choice(book_types) if device != "E-Reader" else "reading"

# Функция генерирующая новые данные.
def generate_daily_data(existing_user_count):
    global user_profiles, library

    user_profiles = load_user_profiles()
    library = load_library()
    
    current_date = datetime.now().strftime("%Y-%m-%d")
    user_growth_rate = random.randint(100, 250)

    daily_data = {
        "date": [current_date] * user_growth_rate,
        "user_id": [],
        "book_id": [],
        "category": [],
        "action": [random.choice(["purchase", "wishlist"]) for _ in range(user_growth_rate)],
        "purchase_type": [random.choice(purchase_types) for _ in range(user_growth_rate)],
        "time_spent_minutes": [],
        "purchase_price": [],
        "book_type": [],
        "device": [],
        "city": []
    }

    for i in range(user_growth_rate):
        user_id, device, city = get_or_create_user(user_profiles, 1000)
        daily_data["user_id"].append(user_id)
        daily_data["device"].append(device)
        daily_data["city"].append(city)

        book_id, category = get_or_create_library(library)
        daily_data["book_id"].append(book_id)
        daily_data['category'].append(category)
        
        action = daily_data["action"][i]
        purchase_type = daily_data["purchase_type"][i]
        
        daily_data["purchase_price"].append(generate_price(action, purchase_type, category))
        daily_data["time_spent_minutes"].append(generate_timespent(action))
        daily_data["book_type"].append(generate_book_type(device))

    return pd.DataFrame(daily_data)

# Функция для дополнение существующего датафрейма новыми данными. 
def update_data_file():
    load_user_profiles()
    load_library()

    if os.path.exists(data_file):
        existing_data = pd.read_csv(data_file)
        existing_user_count = existing_data['user_id'].max()
    else:
        print(f"Existing data file not found. Script not executed.")
        existing_user_count = 1000

    daily_data = generate_daily_data(existing_user_count)

    if os.path.exists(data_file): 
        updated_data = pd.concat([existing_data, daily_data], ignore_index=True)
    else:
        print(f"Script failed - existing file not updated with daily data from {datetime.now().strftime('%Y-%m-%d')}.")

    updated_data.to_csv(data_file, index=False)
    print(f"Данные за {datetime.now().strftime('%Y-%m-%d')} добавлены.")

    save_user_profiles()
    save_library()

if __name__ == "__main__":
    update_data_file()
