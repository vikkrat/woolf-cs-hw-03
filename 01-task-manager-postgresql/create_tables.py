import psycopg2

def create_tables():
    commands = (
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            fullname VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
        )
        """,
        """
        CREATE TABLE status (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE NOT NULL
        )
        """,
        """
        CREATE TABLE tasks (
            id SERIAL PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            description TEXT,
            status_id INTEGER REFERENCES status(id),
            user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
        )
        """
    )
    
    try:
        # Підключення до бази даних PostgreSQL
        conn = psycopg2.connect(
            dbname="your_db_name",
            user="your_username",
            password="your_password",
            host="localhost"
        )
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        conn.commit()
        cur.close()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables()
