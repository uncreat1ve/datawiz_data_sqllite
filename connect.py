import sqlite3
import json


def readFile(path):
    with open(path) as data_file:
        data = json.load(data_file)

    shops = {}
    receipts = {}
    product = {}
    products = []
    for row in data:
        for prod in row['products']:
            products.append((row['id'], prod['order_no'], prod['product_id'], prod['qty'], prod['price']))
        if row['shop_id'] not in shops.keys():
            shops[row['shop_id']] = (row['shop_id'], row['shop__name'])
        if row['id'] not in receipts.keys():
            receipts[row['id']] = (row['id'], row['date'], row['items_qty'], row['week_day'], row['total_price'], row['shop_id'])
        if row['products'][0]['product_id'] not in product.keys():
            product[row['products'][0]['product_id']] = (row['products'][0]['product_id'], row['products'][0]['product__name'])

    cur.executemany("INSERT INTO shop VALUES(?,?)", shops.values())
    cur.executemany("INSERT INTO receipts VALUES(?, ?, ?, ?, ?, ?) ;", receipts.values())
    cur.executemany("INSERT INTO products VALUES(?, ?, ?, ?, ?) ;", products)
    cur.executemany("INSERT INTO product VALUES(?, ?) ;", product.values())

db = sqlite3.connect('db/datawizDB')
cur = db.cursor()

cur.executescript("""CREATE TABLE shop (id_shop INTEGER PRIMARY KEY, name VARCHAR);
CREATE TABLE receipts (id INTEGER PRIMARY KEY,
                      date DATETIME,
                      items_qty INTEGER,
                      week_day INTEGER,
                      total_price REAL,
                      shop_id INTEGER,
                      FOREIGN KEY(shop_id) REFERENCES shop(id_shop));
CREATE TABLE product (id_product INTEGER PRIMARY KEY,
                      name VARCHAR);
CREATE TABLE products (receipts_id INTEGER,
                      order_no INTEGER,
                      product_id INTEGER,
                      qty REAL,
                      price REAL,
                      FOREIGN KEY(product_id) REFERENCES product(id_product),
                      FOREIGN KEY(receipts_id) REFERENCES receipts(id));
""")

readFile('data.json')

db.commit()
db.close()