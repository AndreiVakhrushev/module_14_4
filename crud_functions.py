import sqlite3

def initiate_db():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products
                 (id INTEGER PRIMARY KEY, 
                 title TEXT NOT NULL, 
                 description TEXT NOT NULL, 
                 price INTEGER NOT NULL)''')
    cursor.execute('DELETE FROM Products')
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.close()
    return products


initiate_db()

def add_product(product_id, title, description, price):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
              (product_id, title, description, price))
    connection.commit()
    connection.close()


products = [
    (1, 'Product 1', 'Железо (65mg) 365 штук', 3100),
    (2, 'Product 2', 'Витамин С (1000mg) 365 штук', 5000),
    (3, 'Product 3', 'Витамин D3 (2000mg) 320 капсул', 3200),
    (4, 'Product 4', 'Комплекс Омега (1200mg) 200 капсул', 5400),
]

for product in products:
    add_product(*product)
