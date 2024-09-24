import psycopg2

def run_queries_from_sql_file():
    conn = None
    try:
        # Підключення до бази даних PostgreSQL
        conn = psycopg2.connect(
            dbname="your_db_name",
            user="your_username",
            password="your_password",
            host="localhost"
        )
        cur = conn.cursor()

        # Читання SQL-файлу
        with open('queries.sql', 'r') as file:
            sql_queries = file.read()

        # Виконання запитів
        cur.execute(sql_queries)
        conn.commit()
        print("Queries executed successfully.")

        cur.close()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    run_queries_from_sql_file()
