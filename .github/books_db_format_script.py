import os
import pandas as pd

input_file = ".github/books_database_main.csv"
output_file = ".github/books_database_FORMATED.csv"

df = pd.read_csv(input_file, sep=',')

# Заполнение пропущенных (NaN) значение 
df.fillna({'purchase_price': 0, 'city': 'Неизвестно'}, inplace = True)

# Форматирование типов данных для более удобнойработой с данными и сокращение размера файла.
df['date'] = pd.to_datetime(df['date'])
df['user_id'] = df['user_id'].astype('int16')
df['book_id'] = df['book_id'].astype('int16')
df['time_spent_minutes'] = df['time_spent_minutes'].astype('int16')
df['purchase_price'] = df['purchase_price'].astype('float16')

# Сортировка датафрейма по возрастанию даты и ID пользователя 
df = df.sort_values(['date', 'user_id'], ascending=True)

# Запись отформатированного датафрейма в новый файл.
print(f"Размер датафрейма перед записью: {df.shape}")
df.to_csv(output_file, index=False)
print(f"Файл {output_file} успешно сохранен!")
