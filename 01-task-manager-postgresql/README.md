# Task Management System (PostgreSQL + Python)

Цей проєкт представляє базову систему управління завданнями на базі PostgreSQL з використанням Python для створення таблиць, наповнення бази даними та виконання SQL-запитів.

## Передумови

1. Встановлений **Python 3.7+**
2. Встановлений **PostgreSQL**
3. Підключення до PostgreSQL бази даних

## Встановлення

### 1. Створення та активація віртуального середовища Python

Рекомендується використовувати віртуальне середовище для ізоляції залежностей проєкту.

#### Для Windows:

1. Створіть віртуальне середовище:
   
   ```bash
   python -m venv venv
    ```
2. Активуйте його:

    ```bash
    .\venv\Scripts\activate
    ``` 

#### Для MacOS/Linux:

1. Створіть віртуальне середовище:

    ```bash
    python3 -m venv venv
    ```

2. Активуйте його:

    ```bash
    source venv/bin/activate
    ```

###  2. Склонуйте репозиторій або скопіюйте файли проєкту:

    ```bash
    git clone
    ```

###  3. Встановіть всі залежності з requirements.txt:

    ```bash
    pip install -r requirements.txt
    ```

###  4. Впевніться, що ви налаштували вашу базу даних PostgreSQL, створивши нову базу:

    ```bash
    psql -U postgres
    CREATE DATABASE your_db_name;
    ```


##  Конфігурація

    ```python
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_username",
        password="your_password",
        host="localhost"
    )
    ```

## Використання

1. Створення таблиць:

Для створення таблиць у базі даних, виконайте скрипт create_tables.py:

    ```bash
    python create_tables.py
    ```

2. Заповнення бази даними:

Для наповнення бази випадковими даними за допомогою бібліотеки Faker, виконайте скрипт seed.py:

    ```bash
    python seed.py
    ```

3. Запуск SQL-запитів:

Виконайте SQL-запити, які зберігаються у файлі queries.sql за допомогою run_queries.py:

    ```bash
    python run_queries.py
    ```

4. Запуск всіх кроків одразу:
Для автоматичного запуску всіх кроків (створення таблиць, заповнення даними та виконання запитів), скористайтесь скриптом main.py:

```bash
python main.py
```

##  SQL-запити
Файл queries.sql містить усі необхідні SQL-запити, які можуть бути виконані за допомогою run_queries.py. 
Деякі приклади запитів:

```sql
-- Отримати всі завдання певного користувача
SELECT * FROM tasks WHERE user_id = 1;

-- Оновити статус завдання
UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 1;
```

## Залежності
Проєкт використовує такі залежності:

psycopg2-binary – для підключення до PostgreSQL
Faker – для генерації випадкових даних