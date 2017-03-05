import sqlite3


db = sqlite3.connect('db/datawizDB')
cur = db.cursor()

cur.execute("""
SELECT fg.date_day,product.name,  MAX() FROM products AS pd
INNER JOIN receipts AS r
ON pd.receipts_id=r.id
GROUP BY fg.week_day
""")
sel = cur.fetchall()
print sel