import subprocess

def run_create_tables():
    try:
        print("Creating tables...")
        subprocess.run(["python", "create_tables.py"], check=True)
        print("Tables created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating tables: {e}")

def run_seed_data():
    try:
        print("Seeding data...")
        subprocess.run(["python", "seed.py"], check=True)
        print("Data seeded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error seeding data: {e}")

def run_queries():
    try:
        print("Running queries...")
        subprocess.run(["python", "queries.py"], check=True)
        print("Queries executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running queries: {e}")

if __name__ == "__main__":
    run_create_tables()
    run_seed_data()
    run_queries()
