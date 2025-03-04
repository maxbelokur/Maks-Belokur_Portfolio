
### **Book store app**
#### Цель проекта: Создание базы данных для продуктового анализа и визуализации. 

Задачи:
- Создать скрипт для рандомного ежедневного пополнения базы данных онлайн магазина книг действиями существующих и новых клиентов.
- Настроить автоматическое выполнение скрипта через Git Action.
- Настройка загрузки отформатированного датафрейма .CSV в Google Sheets для создания Dashboard в Tableu. 
- Настроить отправку автоматических уведомлений в Телеграм Бот.

Выполнение:
1. Создал скрипт генерирующий данные новых действий клиентов. При генерации сверяется, использует и дополняет библиотеки с пользователями и книгами. => **[Python__Books_store_app/script_gen_books_app_data.py](https://github.com/maxbelokur/Maks-Belokur_Portfolio/blob/main/Python__Books_store_app/script_gen_books_app_data.py)**
2. Создал скрипт форматирующий полученный данные перед выгрузкой в Google Sheets. => **[Python__Books_store_app/script_format_books_df.py](https://github.com/maxbelokur/Maks-Belokur_Portfolio/blob/main/Python__Books_store_app/script_format_books_df.py)**
3. Создал скрипт, которые выгружает CSV файл в Google Sheets. => **[Python__Books_store_app/script_books_df_upload_to_gsh.py](https://github.com/maxbelokur/Maks-Belokur_Portfolio/blob/main/Python__Books_store_app/script_books_df_upload_to_gsheets.py)**
4. Реализовал автоматизацию последовательного выполнения Python скриптов через Git Action:
          I. Запуск скрипта 1: и обновление CSV файла + отправка уведомления в TG. => **[action_run_books_app_data_updater.yml]**
          II. Запуск скрипат 2 после успешного выполнения (I): Форматирования датасета на GIT + отправка уведомления в TG. => **[action_format_books_data_main.yml]**
          III. Запуск скрипат 3 после успешного выполнения (II): Загрузка отформатированного CSV файла на Google Sheet + отправка уведомления в TG. => **[action_upload_books_df_to_gsheets.yml]**
6. Создал Dashboard в Tableu Public, который берет датасет с Google Sheet. => [Dashboard Tableu](https://public.tableau.com/app/profile/maksim.belokur/viz/Book_app_dashboarv_v_1/Dashboard1)
