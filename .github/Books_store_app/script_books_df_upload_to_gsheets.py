import os
import json
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Загружаем учетные данные из файла, который был создан в GitHub Actions
GOOGLE_CREDENTIALS_FILE = "google_credentials.json"

if not os.path.exists(GOOGLE_CREDENTIALS_FILE):
    raise FileNotFoundError("Файл google_credentials.json не найден! Убедитесь, что он был создан в GitHub Actions.")

# Аутентификация с использованием учетных данных
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]  # Пример: доступ к Google Sheets
credentials = Credentials.from_service_account_file(GOOGLE_CREDENTIALS_FILE, scopes=SCOPES)

# Подключение к Google API (пример: работа с Google Sheets)
service = build("sheets", "v4", credentials=credentials)

# ID Google Таблицы (замените на свой)
SPREADSHEET_ID = "your_google_sheet_id"

# Чтение данных из Google Sheets
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range="Sheet1!A1:E10").execute()
rows = result.get("values", [])

# Вывод данных
for row in rows:
    print(row)
