import os
import pandas as pd

input_file = "Python__Books_store_app/books_data_main.csv"
output_file = "Python__Books_store_app/books_data_FORMATED.csv"

df = pd.read_csv(input_file, sep=',')

# Заполнение пропущенных (NaN) значение 
df.fillna({'purchase_price': 0, 'city': 'Неизвестно'}, inplace = True)

# Сортировка датафрейма по возрастанию даты и ID пользователя 
df = df.sort_values(['date', 'user_id'], ascending=True)

# Запись отформатированного датафрейма в новый файл.
print(f"Размер датафрейма перед записью: {df.shape}")
df.to_csv(output_file, index=False)
print(f"Файл {output_file} успешно сохранен!")
