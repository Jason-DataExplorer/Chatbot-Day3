import os
import psycopg2


DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a app_name').read()[:-1]

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

postgres_delete_query = f"""DELETE FROM test_table WHERE id > 5"""

cursor.execute(postgres_delete_query)
conn.commit()

count = cursor.rowcount
print(count, "Record delete successfully into database")

cursor.close()
conn.close()
