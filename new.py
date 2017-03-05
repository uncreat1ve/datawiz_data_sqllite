cur.executemany("INSERT INTO shop VALUES('%s','%s');"%(shop, shops[shop]))
cur.executescript("INSERT INTO receipts VALUES('%s','%s','%s','%s','%s','%s');" % (receipt, receipts[receipt][0], receipts[receipt][1], receipts[receipt][2], receipts[receipt][3], receipts[receipt][4]))
cur.executescript("INSERT INTO products VALUES('%s','%s','%s','%s','%s');" % (produc, products[produc][0], products[produc][1], products[produc][2], products[produc][3]))
cur.executescript("INSERT INTO product VALUES('%s','%s');" % (pro, product[pro]))
