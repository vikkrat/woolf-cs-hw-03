from pymongo import MongoClient, errors
from bson.objectid import ObjectId

# Підключення до MongoDB (локального чи віддаленого сервера MongoDB Atlas)
client = MongoClient('mongodb://localhost:27017/')
db = client['cats_database']
collection = db['cats_collection']


# Функція для додавання кота (Create)
def create_cat(name, age, features):
    try:
        cat = {
            "name": name,
            "age": age,
            "features": features
        }
        result = collection.insert_one(cat)
        print(f"Кота додано з _id: {result.inserted_id}")
    except errors.PyMongoError as e:
        print(f"Помилка при створенні кота: {e}")


# Функція для отримання всіх котів (Read)
def get_all_cats():
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except errors.PyMongoError as e:
        print(f"Помилка при отриманні котів: {e}")


# Функція для отримання кота за ім'ям (Read)
def get_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"Кота з ім'ям {name} не знайдено.")
    except errors.PyMongoError as e:
        print(f"Помилка при пошуку кота: {e}")


# Функція для оновлення віку кота за ім'ям (Update)
def update_cat_age(name, new_age):
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.matched_count > 0:
            print(f"Вік кота {name} оновлено.")
        else:
            print(f"Кота з ім'ям {name} не знайдено.")
    except errors.PyMongoError as e:
        print(f"Помилка при оновленні віку кота: {e}")


# Функція для додавання нової характеристики коту (Update)
def add_cat_feature(name, new_feature):
    try:
        result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
        if result.matched_count > 0:
            print(f"Характеристику '{new_feature}' додано коту {name}.")
        else:
            print(f"Кота з ім'ям {name} не знайдено.")
    except errors.PyMongoError as e:
        print(f"Помилка при додаванні характеристики: {e}")


# Функція для видалення кота за ім'ям (Delete)
def delete_cat_by_name(name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Кота з ім'ям {name} видалено.")
        else:
            print(f"Кота з ім'ям {name} не знайдено.")
    except errors.PyMongoError as e:
        print(f"Помилка при видаленні кота: {e}")


# Функція для видалення всіх котів (Delete)
def delete_all_cats():
    try:
        result = collection.delete_many({})
        print(f"Видалено {result.deleted_count} записів.")
        if result.deleted_count == 0:
            print("У колекції не було записів.")
    except errors.PyMongoError as e:
        print(f"Помилка при видаленні всіх котів: {e}")


# Функція для почергового додавання 5 котів
def add_five_cats():
    # Створюємо 5 різних котів
    cats = [
        {"name": "barsik", "age": 3, "features": ["ходить в капці", "дає себе гладити", "рудий"]},
        {"name": "murzik", "age": 4, "features": ["чорний", "грайливий"]},
        {"name": "pushok", "age": 2, "features": ["білий", "маленький"]},
        {"name": "simba", "age": 5, "features": ["смугастий", "великий", "спить цілий день"]},
        {"name": "kuzya", "age": 1, "features": ["маленький", "бігає за м'ячиком", "дуже активний"]}
    ]
    
    # Додаємо кожного кота
    for cat in cats:
        create_cat(cat['name'], cat['age'], cat['features'])


if __name__ == '__main__':
    # Додаємо п'ятьох котів
    add_five_cats()

    # Читаємо всі записи після додавання
    print("\nВсі коти після додавання:")
    get_all_cats()

    # Оновлюємо вік кота
    print("\nОновлення віку кота 'barsik':")
    update_cat_age("barsik", 5)

    # Додаємо нову характеристику
    print("\nДодавання нової характеристики коту 'murzik':")
    add_cat_feature("murzik", "любить рибу")

    # Видаляємо одного кота
    print("\nВидалення кота 'pushok':")
    delete_cat_by_name("pushok")

    # Читаємо всі записи після видалення одного кота
    print("\nВсі коти після видалення кота 'pushok':")
    get_all_cats()

    # Видаляємо всіх котів
    print("\nВидалення всіх котів:")
    delete_all_cats()
