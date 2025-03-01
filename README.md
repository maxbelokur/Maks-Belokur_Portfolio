# ПОРТФОЛИО: PET-Проекты

______________________________________________________
## PostgreSQL

### **1. Online_retail: Продуктовый анализ данных онлайн ретайла.** [/PostgreSQL__Online_retail/](https://github.com/maxbelokur/Maks-Belokur_Portfolio/tree/main/PostgreSQL__Online_retail)
_Датафрей: Online Retail (https://archive.ics.uci.edu/dataset/352/online+retail)_

Задачи:
1. Построить когортный анализ. Определить долю пользователей, который вернулись после 30, 60 и 90 дней. 
2. Определите среднее количество уникальных активных пользователей за день (DAU) и за месяц (MAU).
3. Определить уникальных активных пользователей за день (DAU) для каждой недели в 2011 году.


______________________________________________________
## Python.

### **1. Book store app** [/Python__Book_app_store/](https://github.com/maxbelokur/Maks-Belokur_Portfolio/tree/main/Python__Books_store_app):
#### Цель проекта: Создание базы данных для продуктового анализа и визуализации. 
Задачи:
- Создать скрипт для рандомного ежедневного пополнения базы данных онлайн магазина книг действиями существующих и новых клиентов.
- Настроить автоматическое выполнение скрипта через Git Action.
- Настройка загрузки отформатированного датафрейма .CSV в Google Sheets для создания Dashboard в Tableu. 
- Настроить отправку автоматических уведомлений в Телеграм Бот.

Выполнение:
1. Скрипт генерирующий данные новых действий клиентов - **Python__Books_store_app/script_gen_books_app_data.py**
2. Скрипт форматирующий полученный данные перед выгрузкой в Google Sheets - **Python__Books_store_app/script_format_books_df.py**
3. Скрипт выгружает CSV файл в Google Sheets - **Python__Books_store_app/script_books_df_upload_to_gsh.py**
4. Скрипты Git Action для запуска скриптов выше: .github/workflow/...  action_run_books_app_data_updater.yml => action_format_books_data_main.yml => action_upload_books_df_to_gsheets.yml
5. Скрипт отправки уведомлений в Телеграм бот: .github/workflow/send_tg_notification.py
6. [Dashboard Tableu](https://public.tableau.com/app/profile/maksim.belokur/viz/Book_app_dashboarv_v_1/Dashboard1)

### **2. Анализ результатов А/В-теста** [/Python__ABtest_analysis/]():
Задание:
Имеются результаты A/B теста, в котором двум группам пользователей предлагались различные наборы акционных предложений. 
Известно, что ARPU в тестовой группе выше на 5%, чем в контрольной. При этом в контрольной группе 1928 игроков из 202103 оказались платящими, а в тестовой – 1805 из 202667.
Какой набор предложений можно считать лучшим? Какие метрики стоит проанализировать для принятия правильного решения и как?



