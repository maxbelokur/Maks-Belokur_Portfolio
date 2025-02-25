import pandas as pd
import numpy as np

# Фиксация значений генерации.
np.random.seed(42)

# Кол-во сессий в датафрейме.
num_sessions = 1000000

# Генерация ИД пользователей.
user_ids = np.random.randint(100000, 350000, size=num_sessions)

# Генерация времени сессий.
time_range = pd.date_range(start="2024-01-01 06:00:00", end="2024-12-31 23:59:00", freq='min').to_series().sample(500000).values

# Генерация времени начала и конца сессий.
session_start = np.random.choice(time_range, size=num_sessions)
session_end = session_start + pd.to_timedelta(np.random.randint(1, 1000, num_sessions), unit='s')

devices = ['iOS', 'Android', 'Chrome', 'InternetExplorer', 'YandexBrowser']

# Симуляция воронки.
level_1 = np.random.choice([1, 0], size=num_sessions, p=[0.9, 0.1])  # 90% reach level 1
level_2 = np.where(level_1 == 1, np.random.choice([1, 0], size=num_sessions, p=[0.82, 0.18]), 0)  # 70% of L1 reach L2
level_3 = np.where(level_2 == 1, np.random.choice([1, 0], size=num_sessions, p=[0.63, 0.37]), 0)  # 50% of L2 reach L3
level_4 = np.where(level_3 == 1, np.random.choice([1, 0], size=num_sessions, p=[0.5, 0.5]), 0)  # 30% of L3 reach L4
level_5 = np.where(level_4 == 1, np.random.choice([1, 0], size=num_sessions, p=[0.33, 0.67]), 0)  # 20% of L4 reach L5

# Сведение данных в датафрейм.
df = pd.DataFrame({
    'user_id': user_ids,
    'device': np.random.choice(devices, size=num_sessions, p=[0.385, 0.285, 0.135, 0.085, 0.110]),
    'session_start': session_start,
    'session_end': session_end,
    'funnel_level_1': level_1,
    'funnel_level_2': level_2,
    'funnel_level_3': level_3,
    'funnel_level_4': level_4,
    'funnel_level_5': level_5
})

# Запись получившегося датасета в CSV файл.
df.to_csv('.github/Python__sessions_dataset/sessions_dataset.csv' , sep=';', index=False)
