import os
import psycopg2

DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a app_name').read()[:-1]

conn   = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

records = [
    ('David', 45, 170, '2021-08-26'),
    ('Johny', 60, 168, '2021-08-26'),
    ('Marry', 50, 170, '2021-08-26'),
    ('Curry', 80, 200, '2021-08-26'),
    ('Fredd', 90, 188, '2021-08-26')
]

table_columns = '(name, weight, height, date)'
postgres_insert_query = f"""INSERT INTO test_table {table_columns} VALUES (%s,%s,%s,%s)"""

cursor.executemany(postgres_insert_query, records)
conn.commit()

count = cursor.rowcount
print(count, "Record inserted successfully into database")

cursor.close()
conn.close()
