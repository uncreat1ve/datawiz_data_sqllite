import sqlite3

db = sqlite3.connect('db/datawizDB')
cur = db.cursor()

cur.execute("""SELECT r.shop_id AS id, pd.product_id AS product,  Sum(pd.qty) AS sum
FROM products AS pd
INNER JOIN receipts AS r
ON pd.receipts_id=r.id
GROUP BY r.shop_id, pd.product_id

""")
sel = cur.fetchall()
print sel

# cur.execute(""" (SELECT r.selshop_id, pd.product_id,  Sum(pd.qty) FROM products AS pd
# INNER JOIN receipts AS r
# ON pd.receipts_id=r.id
# GROUP BY r.shop_id, pd.product_id)
# """)
#
# new = cur.fetchall()
# print new
db.close()

# SELECT shop.name, DATE(receipts.date) FROM receipts
# INNER JOIN receipts ON
# INNER JOIN shop ON shop.id_shop = receipts.shop_id
#
#
# SELECT r.shop_id,
# (SELECT
#   r.shop_id,
#   pd.product_id,
#   Sum(pd.qty) AS suma
# FROM products AS pd
#   INNER JOIN receipts AS r
#     ON pd.receipts_id = r.id
# GROUP BY r.shop_id, pd.product_id)
# FROM receipts AS r


# SELECT ROUND(AVG(VALUE), 2) AS VALUE datepart(hours, convert(VARCHAR, CAST()))