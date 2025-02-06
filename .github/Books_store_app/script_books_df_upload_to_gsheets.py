import os
import json
import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Путь к CSV-файлу
CSV_FILE_PATH = ".github/Books_store_app/books_data_FORMATED.csv"

# Проверяем наличие CSV-файла
if not os.path.exists(CSV_FILE_PATH):
    raise FileNotFoundError(f"Файл {CSV_FILE_PATH} не найден! Проверьте путь к файлу.")

# Загружаем учетные данные из GitHub Secrets
GOOGLE_CREDENTIALS_JSON = os.getenv("GOOGLE_CREDENTIALS")

if not GOOGLE_CREDENTIALS_JSON:
    raise ValueError("Переменная GOOGLE_CREDENTIALS не найдена! Проверьте GitHub Secrets.")

# Преобразуем JSON-строку в словарь
credentials_info = json.loads(GOOGLE_CREDENTIALS_JSON)

# Аутентификация через сервисный аккаунт
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
credentials = Credentials.from_service_account_info(credentials_info, scopes=SCOPES)

# Подключение к Google Sheets API
service = build("sheets", "v4", credentials=credentials)

# ID Google Таблицы
SPREADSHEET_ID = "1rSdrMjDxwAbpwvwYQ9WRUWSbw9d7g84uqtQdHRx_lKo"

# Загружаем данные из CSV
df = pd.read_csv(CSV_FILE_PATH)

# Преобразуем DataFrame в список списков (Google Sheets API требует такой формат)
values = [df.columns.tolist()] + df.astype(str).values.tolist()

# Обновление данных в Google Sheets (лист "Books_data_final")
body = {"values": values}
sheet = service.spreadsheets()
sheet.values().update(
    spreadsheetId=SPREADSHEET_ID,
    range="Books_data_final!A1",
    valueInputOption="RAW",
    body=body,
).execute()

print(f"Данные из {CSV_FILE_PATH} успешно загружены в Google Sheets (лист 'Books_data_final')!")
