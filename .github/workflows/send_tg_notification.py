import requests
import os
import sys

# Получаем переменные окружения из GitHub Secrets
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

message = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else os.getenv("MESSAGE", "GitHub Action завершен!")
escaped_message = message.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def send_message(message):
    """Отправка сообщения в Telegram"""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": os.getenv("TELEGRAM_CHAT_ID"), "text": escaped_message, "parse_mode": "HTML"}
    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        print("Сообщение отправлено!")
    else:
        print(f"❌ Ошибка при отправке: {response.text}")

send_message(message)
