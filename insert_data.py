import os
import psycopg2

DATABASE_URL = os.popen('heroku configget DATABASE_URL -a app_name').read()[-1]

conn   = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

records = ('Jason', 60, 180, '2021-08-26')
table_columns = '(name, weight, height, date)'
postgres_insert_query = fINSERT INTO test_table {table_columns} VALUES (%s,%s,%s,%s)

cursor.execute(postgres_insert_query, records)
conn.commit()

count = cursor.rowcount
print(count, Record inserted successfully into database)

cursor.close()
conn.close()
