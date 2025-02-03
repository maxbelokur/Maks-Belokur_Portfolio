import requests
import os

# Получаем переменные окружения из GitHub Secrets
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_message(message):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("❌ Ошибка: TELEGRAM_BOT_TOKEN или TELEGRAM_CHAT_ID не найдены!")
        return
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, data=data)
    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        print("Сообщение отправлено!")
    else:
        print(f"❌ Ошибка при отправке: {response.text}")

send_message("*Форматирование CSV успешно завершено!* \n\nИзменения загружены в репозиторий.")
