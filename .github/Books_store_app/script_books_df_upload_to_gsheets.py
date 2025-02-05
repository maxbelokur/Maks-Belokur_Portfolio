import os
import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Путь к CSV-файлу
CSV_FILE_PATH = ".github/Books_store_app/books_data_FORMATED.csv"

# Проверяем наличие CSV-файла
if not os.path.exists(CSV_FILE_PATH):
    raise FileNotFoundError(f"Файл {CSV_FILE_PATH} не найден! Проверьте путь к файлу.")

# Загружаем учетные данные Google из GitHub Secrets
GOOGLE_CREDENTIALS_FILE = "google_credentials.json"

if not os.path.exists(GOOGLE_CREDENTIALS_FILE):
    raise FileNotFoundError("Файл google_credentials.json не найден! Проверьте GitHub Secrets.")

# Аутентификация через сервисный аккаунт
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
credentials = Credentials.from_service_account_file(GOOGLE_CREDENTIALS_FILE, scopes=SCOPES)

# Подключение к Google Sheets API
service = build("sheets", "v4", credentials=credentials)

# ID вашей Google Таблицы (замените на свой)
SPREADSHEET_ID = "1rSdrMjDxwAbpwvwYQ9WRUWSbw9d7g84uqtQdHRx_lKo"

# Загружаем данные из CSV
df = pd.read_csv(CSV_FILE_PATH)

# Преобразуем DataFrame в список списков (Google Sheets API требует такой формат)
values = [df.columns.tolist()] + df.values.tolist()

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
