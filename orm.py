import sqlite3
con = sqlite3.connect('chinnok.db')

cur = con.cursor()

sql_query = '''
SELECT * FROM customers;
'''

cur.execute(sql_query)

customers = cur.fetchall()

con.close()

for customer in customers:
    print()