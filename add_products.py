import sqlite3

DATABASE_NAME = "products.db"

def add_sample_products():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    products = [
        ("Product1", "Описание 1", 100),
        ("Product2", "Описание 2", 200),
        ("Product3", "Описание 3", 300),
        ("Product4", "Описание 4", 400),
    ]

    cursor.executemany('''
        INSERT INTO Products (title, description, price)
        VALUES (?, ?, ?)
    ''', products)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    add_sample_products()
    print("Продукты добавлены в базу данных.")