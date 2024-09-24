import psycopg2
from faker import Faker

def seed_data():
    fake = Faker()

    try:
        conn = psycopg2.connect(
            dbname="your_db_name",
            user="your_username",
            password="your_password",
            host="localhost"
        )
        cur = conn.cursor()

        # Додавання статусів
        statuses = ['new', 'in progress', 'completed']
        for status in statuses:
            cur.execute("INSERT INTO status (name) VALUES (%s) ON CONFLICT (name) DO NOTHING;", (status,))

        # Додавання випадкових користувачів та завдань
        for _ in range(10):
            fullname = fake.name()
            email = fake.email()

            # Додавання користувача
            cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s) RETURNING id;", (fullname, email))
            user_id = cur.fetchone()[0]

            # Додавання завдань для користувача
            for _ in range(5):
                title = fake.sentence(nb_words=6)
                description = fake.text()
                status_id = fake.random_int(min=1, max=3)

                cur.execute("""
                    INSERT INTO tasks (title, description, status_id, user_id)
                    VALUES (%s, %s, %s, %s);
                """, (title, description, status_id, user_id))

        conn.commit()
        cur.close()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    seed_data()
