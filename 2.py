import sqlite3


db = sqlite3.connect('db/datawizDB')
cur = db.cursor()

cur.execute("""(
SELECT r.week_day AS day, pd.product_id AS product, Sum(pd.qty) AS sum
      FROM products AS pd
        INNER JOIN receipts AS r
          ON pd.receipts_id = r.id
      GROUP BY r.week_day, pd.product_id;
""")
sel = cur.fetchall()
print sel