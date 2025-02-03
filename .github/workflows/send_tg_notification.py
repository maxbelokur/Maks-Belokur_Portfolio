import requests
import os

# Получаем переменные окружения из GitHub Secrets
TELEGRAM_BOT_TOKEN = os.getenv("7993106648:AAG4PW_3pKZr6nnYg3Mhl1l937utNTeKv3w")
TELEGRAM_CHAT_ID = os.getenv("179526632")

def send_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, data=data)

# Отправка уведомления
send_message("*Форматирование CSV успешно завершено!* \n\nИзменения загружены в репозиторий.")
